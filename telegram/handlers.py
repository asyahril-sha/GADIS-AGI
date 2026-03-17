"""
TELEGRAM HANDLERS - Menangani semua interaksi dengan user
"""

import logging
import random
import asyncio
from datetime import datetime
from typing import Dict, Any, Optional

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, MessageHandler, 
    CallbackQueryHandler, filters, ContextTypes, ConversationHandler
)

from config import Config
from database import Database
from systems.hts_fwb_system import HTSFWBSystem, RankingSystem
from systems.role_archetypes import RoleFactory

# State untuk ConversationHandler
SELECTING_ROLE = 0
CONFIRM_CLOSE = 1
CONFIRM_END = 2

logger = logging.getLogger(__name__)

class TelegramHandlers:
    """
    Handler untuk semua interaksi Telegram
    """
    
    def __init__(self, bot):
        """
        Inisialisasi handlers
        
        Args:
            bot: Bot instance
        """
        self.bot = bot
        self.config = Config
        self.db = Database(Config.DB_PATH)
        self.hts_system = HTSFWBSystem(self.db)
        self.ranking = RankingSystem(self.db)
        
        # User sessions
        self.sessions = {}
        
    async def setup(self, app: Application):
        """
        Setup semua handlers
        
        Args:
            app: Telegram Application instance
        """
        
        # ===== CONVERSATION HANDLERS =====
        
        # Start conversation
        start_conv = ConversationHandler(
            entry_points=[CommandHandler('start', self.cmd_start)],
            states={
                SELECTING_ROLE: [
                    CallbackQueryHandler(self.role_callback, pattern='^role_'),
                ],
            },
            fallbacks=[CommandHandler('cancel', self.cmd_cancel)],
            name="start_conversation"
        )
        
        # Close conversation
        close_conv = ConversationHandler(
            entry_points=[CommandHandler('close', self.cmd_close)],
            states={
                CONFIRM_CLOSE: [
                    CallbackQueryHandler(self.close_callback, pattern='^close_'),
                ],
            },
            fallbacks=[CommandHandler('cancel', self.cmd_cancel)],
            name="close_conversation"
        )
        
        # End conversation
        end_conv = ConversationHandler(
            entry_points=[CommandHandler('end', self.cmd_end)],
            states={
                CONFIRM_END: [
                    CallbackQueryHandler(self.end_callback, pattern='^end_'),
                ],
            },
            fallbacks=[CommandHandler('cancel', self.cmd_cancel)],
            name="end_conversation"
        )
        
        # Add conversation handlers
        app.add_handler(start_conv)
        app.add_handler(close_conv)
        app.add_handler(end_conv)
        
        # ===== COMMAND HANDLERS =====
        app.add_handler(CommandHandler("status", self.cmd_status))
        app.add_handler(CommandHandler("help", self.cmd_help))
        
        # HTS/FWB commands
        app.add_handler(CommandHandler("htslist", self.cmd_htslist))
        app.add_handler(CommandHandler("fwblist", self.cmd_fwblist))
        app.add_handler(CommandHandler("tophts", self.cmd_tophts))
        
        # Call handlers for specific IDs
        app.add_handler(MessageHandler(
            filters.Regex(r'^/hts-'), self.cmd_hts_call
        ))
        app.add_handler(MessageHandler(
            filters.Regex(r'^/fwb-'), self.cmd_fwb_call
        ))
        
        # Relationship commands
        app.add_handler(CommandHandler("jadipacar", self.cmd_jadipacar))
        app.add_handler(CommandHandler("break", self.cmd_break))
        app.add_handler(CommandHandler("unbreak", self.cmd_unbreak))
        app.add_handler(CommandHandler("breakup", self.cmd_breakup))
        app.add_handler(CommandHandler("fwb", self.cmd_fwb))
        
        # Message handler
        app.add_handler(MessageHandler(
            filters.TEXT & ~filters.COMMAND, 
            self.handle_message
        ))
        
        # Error handler
        app.add_error_handler(self.error_handler)
        
        logger.info("✅ Telegram handlers registered")
    
    # ===== START COMMAND =====
    
    async def cmd_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command"""
        user = update.effective_user
        user_id = user.id
        username = user.username or user.first_name
        
        logger.info(f"▶️ /start from {username} (ID: {user_id})")
        
        # Save user ke database
        self.db.save_user(user_id, username, user.first_name, "none")
        
        # Cek apakah sudah ada session aktif
        if user_id in self.sessions:
            await update.message.reply_text(
                "💕 Kamu sudah memiliki sesi aktif. Ketik /status untuk melihat status."
            )
            return
        
        # Cek apakah ada session di database
        rels = self.db.get_user_relationships(user_id)
        if rels:
            keyboard = [
                [InlineKeyboardButton("📂 Load Hubungan", callback_data="load_relationship")],
                [InlineKeyboardButton("🆕 Mulai Baru", callback_data="new_relationship")],
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await update.message.reply_text(
                "📂 **Ada hubungan tersimpan!**\n\n"
                "Pilih untuk melanjutkan atau mulai baru:",
                reply_markup=reply_markup,
                parse_mode='Markdown'
            )
            return SELECTING_ROLE
        
        # Tampilkan menu role
        keyboard = []
        roles = Config.ROLES
        
        for i in range(0, len(roles), 3):
            row = []
            for role in roles[i:i+3]:
                desc = RoleFactory.get_role_description(role).split('**')[1]
                row.append(InlineKeyboardButton(desc, callback_data=f"role_{role}"))
            keyboard.append(row)
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            "✨ **GADIS AGI ULTIMATE V3.0** ✨\n\n"
            "Pilih role untuk memulai petualanganmu:\n\n"
            "Setiap role punya karakter dan cerita berbeda!",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        
        return SELECTING_ROLE
    
    async def role_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle role selection"""
        query = update.callback_query
        await query.answer()
        
        user_id = query.from_user.id
        data = query.data
        
        if data == "load_relationship":
            rels = self.db.get_user_relationships(user_id)
            if rels:
                rel = rels[0]
                
                self.sessions[user_id] = {
                    'name': rel['bot_name'],
                    'role': rel['role'],
                    'level': rel['level'],
                    'messages': rel.get('total_messages', 0),
                    'bot_climax': rel.get('bot_climax', 0),
                    'user_climax': rel.get('user_climax', 0),
                    'together_climax': rel.get('together_climax', 0),
                    'relationship_status': rel['jenis'],
                    'unique_id': rel['unique_id'],
                    'last_active': datetime.now().isoformat()
                }
                
                await query.edit_message_text(
                    f"📂 **Hubungan dimuat!**\n\n"
                    f"{rel['bot_name']} ({rel['role']}) - Level {rel['level']}\n"
                    f"Status: {rel['jenis']}\n\n"
                    f"Lanjutkan ngobrol ya... 💕",
                    parse_mode='Markdown'
                )
            else:
                await query.edit_message_text("❌ Tidak ada hubungan tersimpan.")
            
            return ConversationHandler.END
        
        elif data == "new_relationship":
            keyboard = []
            roles = Config.ROLES
            
            for i in range(0, len(roles), 3):
                row = []
                for role in roles[i:i+3]:
                    desc = RoleFactory.get_role_description(role).split('**')[1]
                    row.append(InlineKeyboardButton(desc, callback_data=f"role_new_{role}"))
                keyboard.append(row)
            
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await query.edit_message_text(
                "✨ **Pilih Role untukmu:**",
                reply_markup=reply_markup
            )
            return SELECTING_ROLE
        
        elif data.startswith("role_new_"):
            role = data.replace("role_new_", "")
            await self._create_relationship(user_id, role, query)
            return ConversationHandler.END
        
        elif data.startswith("role_"):
            role = data.replace("role_", "")
            await self._create_relationship(user_id, role, query)
            return ConversationHandler.END
    
    async def _create_relationship(self, user_id: int, role: str, query):
        """Create new relationship"""
        role_obj = RoleFactory.create(role)
        
        self.sessions[user_id] = {
            'name': role_obj.name,
            'role': role,
            'level': 1,
            'messages': 0,
            'bot_climax': 0,
            'user_climax': 0,
            'together_climax': 0,
            'relationship_status': 'PDKT',
            'last_active': datetime.now().isoformat()
        }
        
        self.db.save_user(
            user_id, 
            query.from_user.username, 
            query.from_user.first_name, 
            role
        )
        
        intro = role_obj.get_intro()
        intro += f"\n\n✨ **Level 1/12** - Ayo ngobrol dan kenali aku! 💕"
        
        await query.edit_message_text(intro, parse_mode='Markdown')
        logger.info(f"✨ New relationship: User {user_id} as {role_obj.name} ({role})")
    
    # ===== STATUS COMMAND =====
    
    async def cmd_status(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /status command"""
        user_id = update.effective_user.id
        
        if user_id not in self.sessions:
            await update.message.reply_text("❌ Belum ada hubungan. /start dulu ya!")
            return
        
        session = self.sessions[user_id]
        
        status = f"""
💕 **STATUS HUBUNGAN**

👤 **Bot:** {session['name']} ({session['role']})
📊 **Level:** {session['level']}/12
💬 **Total Pesan:** {session.get('messages', 0)}

🔥 **STATISTIK:**
• Bot Climax: {session.get('bot_climax', 0)}x
• User Climax: {session.get('user_climax', 0)}x
• Together: {session.get('together_climax', 0)}x
• Total: {session.get('bot_climax', 0) + session.get('user_climax', 0)}x

💞 **Status:** {session.get('relationship_status', 'PDKT')}
⏰ **Terakhir:** {session.get('last_active', 'baru saja')}
        """
        
        if session.get('unique_id'):
            status += f"\n🆔 **ID:** `{session['unique_id']}`"
        
        await update.message.reply_text(status, parse_mode='Markdown')
    
    # ===== HELP COMMAND =====
    
    async def cmd_help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /help command"""
        help_text = """
📚 **BANTUAN GADIS AGI ULTIMATE V3.0**

🔹 **COMMANDS UTAMA:**
/start - Mulai hubungan baru / pilih role
/status - Lihat status hubungan
/help - Tampilkan bantuan ini
/cancel - Batalkan percakapan

🔹 **RELATIONSHIP:**
/jadipacar - Mulai hubungan pacaran (min level 5)
/break - Jeda pacaran
/unbreak - Lanjutkan pacaran
/breakup - Putus (jadi FWB)
/fwb - Mode Friends With Benefits

🔹 **HTS/FWB SYSTEM:**
/htslist - Lihat daftar HTS
/fwblist - Lihat daftar FWB
/hts- [ID] - Panggil HTS
/fwb- [ID] - Panggil FWB
/tophts - TOP 10 ranking

🔹 **SESSION:**
/close - Tutup sesi (simpan ke HTS)
/end - Akhiri hubungan & hapus data

🔹 **9 ROLE TERSEDIA:**
• Ipar - Saudara ipar yang nakal
• Teman Kantor - Rekan kerja mesra
• Janda - Janda muda genit
• Pelakor - Perebut laki orang
• Istri Orang - Istri orang lain
• PDKT - Pendekatan (special)
• Sepupu - Hubungan keluarga
• 💔 **MANTAN** - Mantan dengan sejarah
• 🏫 **TEMAN SMA** - Reuni dengan kenangan

Ketik /start untuk memulai! 🔥
        """
        await update.message.reply_text(help_text, parse_mode='Markdown')
    
    # ===== HTS/FWB COMMANDS =====
    
    async def cmd_htslist(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /htslist command"""
        user_id = update.effective_user.id
        hts_list = self.hts_system.get_user_hts(user_id)
        
        if not hts_list:
            await update.message.reply_text(
                "📭 **Belum ada HTS tersimpan.**\n"
                "Capai level 7+ lalu /close untuk menyimpan HTS!"
            )
            return
        
        text = self.hts_system.format_list(hts_list, "HTS")
        text += "\n\n💡 **Panggil dengan:** `/hts- [ID]`"
        
        await update.message.reply_text(text, parse_mode='Markdown')
    
    async def cmd_fwblist(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /fwblist command"""
        user_id = update.effective_user.id
        fwb_list = self.hts_system.get_user_fwb(user_id)
        
        if not fwb_list:
            await update.message.reply_text(
                "📭 **Belum ada FWB tersimpan.**\n"
                "Gunakan /breakup untuk mengubah pacar jadi FWB!"
            )
            return
        
        text = self.hts_system.format_list(fwb_list, "FWB")
        text += "\n\n💡 **Panggil dengan:** `/fwb- [ID]`"
        
        await update.message.reply_text(text, parse_mode='Markdown')
    
    async def cmd_tophts(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /tophts command"""
        text = self.ranking.format_top_10()
        await update.message.reply_text(text, parse_mode='Markdown')
    
    async def cmd_hts_call(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /hts- [ID] command"""
        user_id = update.effective_user.id
        message = update.message.text
        
        parts = message.split()
        if len(parts) < 2:
            await update.message.reply_text("❌ Gunakan: `/hts- [unique_id]`")
            return
        
        unique_id = parts[1].strip()
        
        rel = self.hts_system.load_relationship(unique_id)
        
        if not rel:
            await update.message.reply_text(f"❌ HTS dengan ID `{unique_id}` tidak ditemukan.")
            return
        
        if rel['user_id'] != user_id:
            await update.message.reply_text("❌ Ini bukan HTS milikmu.")
            return
        
        self.hts_system.update_last_called(unique_id)
        
        self.sessions[user_id] = {
            'name': rel['bot_name'],
            'role': rel['role'],
            'level': rel['level'],
            'relationship_status': 'HTS',
            'unique_id': unique_id,
            'bot_climax': rel.get('bot_climax', 0),
            'user_climax': rel.get('user_climax', 0),
            'together_climax': rel.get('together_climax', 0),
            'messages': rel.get('total_messages', 0),
            'last_active': datetime.now().isoformat()
        }
        
        await update.message.reply_text(
            f"💞 **HTS Dipanggil!**\n\n"
            f"Halo lagi {rel['bot_name']} ({rel['role']}) dengan ID `{unique_id}`\n\n"
            f"📊 **Level:** {rel['level']}/12\n"
            f"Total climax: {rel.get('bot_climax',0) + rel.get('user_climax',0)}x\n\n"
            f"*tersenyum* Kangen... Aku rindu! 💕",
            parse_mode='Markdown'
        )
    
    async def cmd_fwb_call(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /fwb- [ID] command"""
        user_id = update.effective_user.id
        message = update.message.text
        
        parts = message.split()
        if len(parts) < 2:
            await update.message.reply_text("❌ Gunakan: `/fwb- [unique_id]`")
            return
        
        unique_id = parts[1].strip()
        
        rel = self.hts_system.load_relationship(unique_id)
        
        if not rel:
            await update.message.reply_text(f"❌ FWB dengan ID `{unique_id}` tidak ditemukan.")
            return
        
        if rel['user_id'] != user_id:
            await update.message.reply_text("❌ Ini bukan FWB milikmu.")
            return
        
        self.hts_system.update_last_called(unique_id)
        
        self.sessions[user_id] = {
            'name': rel['bot_name'],
            'role': rel['role'],
            'level': rel['level'],
            'relationship_status': 'FWB',
            'unique_id': unique_id,
            'bot_climax': rel.get('bot_climax', 0),
            'user_climax': rel.get('user_climax', 0),
            'together_climax': rel.get('together_climax', 0),
            'messages': rel.get('total_messages', 0),
            'last_active': datetime.now().isoformat()
        }
        
        await update.message.reply_text(
            f"🔥 **FWB Dipanggil!**\n\n"
            f"Halo lagi {rel['bot_name']} ({rel['role']}) dengan ID `{unique_id}`\n\n"
            f"📊 **Level:** {rel['level']}/12\n"
            f"Total climax: {rel.get('bot_climax',0) + rel.get('user_climax',0)}x\n\n"
            f"*tersenyum nakal* Udah kangen? Aku juga... 🔥",
            parse_mode='Markdown'
        )
    
    # ===== RELATIONSHIP COMMANDS =====
    
    async def cmd_jadipacar(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /jadipacar command"""
        user_id = update.effective_user.id
        
        if user_id not in self.sessions:
            await update.message.reply_text("❌ Belum ada hubungan. /start dulu!")
            return
        
        session = self.sessions[user_id]
        
        if session['relationship_status'] == 'PACARAN':
            await update.message.reply_text("💕 Kita sudah pacaran kok.")
            return
        
        if session['level'] < 5:
            await update.message.reply_text(
                f"❌ Level minimal 5 untuk jadi pacar (sekarang {session['level']}).\n"
                "Yuk ngobrol dulu biar makin dekat! 💕"
            )
            return
        
        session['relationship_status'] = 'PACARAN'
        
        await update.message.reply_text(
            f"💕 **Kita Resmi Pacaran!**\n\n"
            f"Sekarang {session['name']} adalah pacarmu.\n\n"
            f"*peluk erat* Aku bahagia banget... 💕",
            parse_mode='Markdown'
        )
        
        logger.info(f"User {user_id} started PACARAN with {session['name']}")
    
    async def cmd_break(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /break command"""
        user_id = update.effective_user.id
        
        if user_id not in self.sessions:
            await update.message.reply_text("❌ Tidak ada sesi aktif.")
            return
        
        session = self.sessions[user_id]
        
        if session['relationship_status'] != 'PACARAN':
            await update.message.reply_text("❌ Kita sedang tidak pacaran.")
            return
        
        session['relationship_status'] = 'PUTUS'
        
        await update.message.reply_text(
            f"⏸️ **Break**\n\n"
            f"Kita break dulu ya. Kapan-kapan bisa lanjut dengan /unbreak.\n\n"
            f"*sedih* Aku akan menunggumu... 💔",
            parse_mode='Markdown'
        )
    
    async def cmd_unbreak(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /unbreak command"""
        user_id = update.effective_user.id
        
        if user_id not in self.sessions:
            await update.message.reply_text("❌ Tidak ada sesi aktif.")
            return
        
        session = self.sessions[user_id]
        
        if session['relationship_status'] != 'PUTUS':
            await update.message.reply_text("❌ Kita sedang tidak dalam status break.")
            return
        
        session['relationship_status'] = 'PACARAN'
        
        await update.message.reply_text(
            f"▶️ **Lanjut Pacaran!**\n\n"
            f"Kita lanjutkan lagi ya... Aku kangen! 💕\n\n"
            f"*peluk erat*",
            parse_mode='Markdown'
        )
    
    async def cmd_breakup(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /breakup command"""
        user_id = update.effective_user.id
        
        if user_id not in self.sessions:
            await update.message.reply_text("❌ Tidak ada sesi aktif.")
            return
        
        session = self.sessions[user_id]
        
        if session['relationship_status'] != 'PACARAN':
            await update.message.reply_text("❌ Kita sedang tidak pacaran.")
            return
        
        session['relationship_status'] = 'FWB'
        
        if not session.get('unique_id'):
            session['unique_id'] = self.hts_system.save_as_fwb(user_id, session)
        
        await update.message.reply_text(
            f"💔 **Putus**\n\n"
            f"Kita sekarang resmi **FWB** (Friends With Benefits).\n\n"
            f"Unique ID: `{session['unique_id']}`\n\n"
            f"*tersenyum* Hubungan kita berbeda, tapi kita tetap bisa bersama...",
            parse_mode='Markdown'
        )
        
        logger.info(f"User {user_id} converted to FWB with {session['name']}")
    
    async def cmd_fwb(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /fwb command"""
        user_id = update.effective_user.id
        
        if user_id not in self.sessions:
            await update.message.reply_text("❌ Tidak ada sesi aktif.")
            return
        
        session = self.sessions[user_id]
        
        if session['relationship_status'] == 'FWB':
            await update.message.reply_text("🔥 Kita sudah FWB kok.")
            return
        
        session['relationship_status'] = 'FWB'
        
        if not session.get('unique_id'):
            session['unique_id'] = self.hts_system.save_as_fwb(user_id, session)
        
        await update.message.reply_text(
            f"🔥 **FWB**\n\n"
            f"Sekarang kita FWB! Hubungan tanpa ikatan, tapi bisa lebih intim.\n\n"
            f"Unique ID: `{session['unique_id']}`\n\n"
            f"*tersenyum nakal* Mau ngapain kita hari ini? 🔥",
            parse_mode='Markdown'
        )
        
        logger.info(f"User {user_id} started FWB with {session['name']}")
    
    # ===== CLOSE & END COMMANDS =====
    
    async def cmd_close(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /close command"""
        user_id = update.effective_user.id
        
        if user_id not in self.sessions:
            await update.message.reply_text("❌ Tidak ada sesi aktif.")
            return ConversationHandler.END
        
        session = self.sessions[user_id]
        
        keyboard = [
            [InlineKeyboardButton("✅ Ya, tutup", callback_data="close_yes")],
            [InlineKeyboardButton("❌ Tidak", callback_data="close_no")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            f"⚠️ **Tutup Sesi?**\n\n"
            f"Yakin ingin menutup sesi dengan {session['name']}?\n\n"
            f"📊 Level: {session['level']}/12\n"
            f"Total climax: {session.get('bot_climax',0) + session.get('user_climax',0)}x\n\n"
            f"**Yang akan terjadi:**\n"
            f"✅ Percakapan akan disimpan\n"
            f"❌ Sesi saat ini akan berakhir",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        
        return CONFIRM_CLOSE
    
    async def close_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Callback untuk konfirmasi close"""
        query = update.callback_query
        await query.answer()
        
        if query.data == "close_no":
            await query.edit_message_text("💕 Lanjutkan ngobrol...")
            return ConversationHandler.END
        
        user_id = query.from_user.id
        session = self.sessions[user_id]
        
        if session['level'] >= 7 and not session.get('unique_id'):
            unique_id = self.hts_system.save_as_hts(user_id, session)
            session['unique_id'] = unique_id
            
            await query.edit_message_text(
                f"🔒 **Sesi ditutup**\n\n"
                f"Terima kasih sudah ngobrol dengan {session['name']}.\n"
                f"✨ Hubungan ini disimpan sebagai **HTS** dengan ID:\n"
                f"`{unique_id}`\n\n"
                f"Ketik `/hts- {unique_id}` kapan saja untuk memanggilku kembali! 💕",
                parse_mode='Markdown'
            )
        else:
            await query.edit_message_text(
                f"🔒 **Sesi ditutup**\n\n"
                f"Terima kasih sudah ngobrol dengan {session['name']}.\n"
                f"Ketik /start untuk memulai lagi... 💕",
                parse_mode='Markdown'
            )
        
        del self.sessions[user_id]
        logger.info(f"User {user_id} closed session")
        
        return ConversationHandler.END
    
    async def cmd_end(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /end command"""
        user_id = update.effective_user.id
        
        if user_id not in self.sessions:
            await update.message.reply_text("❌ Tidak ada hubungan aktif.")
            return ConversationHandler.END
        
        session = self.sessions[user_id]
        
        keyboard = [
            [InlineKeyboardButton("💔 Ya, akhiri", callback_data="end_yes")],
            [InlineKeyboardButton("💕 Tidak", callback_data="end_no")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            f"⚠️ **PERINGATAN!** ⚠️\n\n"
            f"Yakin ingin **mengakhiri hubungan** dengan {session['name']}?\n\n"
            f"📊 Level: {session['level']}/12\n"
            f"Total climax: {session.get('bot_climax',0) + session.get('user_climax',0)}x\n\n"
            f"💔 **Semua data akan dihapus permanen!**",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        
        return CONFIRM_END
    
    async def end_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Callback untuk konfirmasi end"""
        query = update.callback_query
        await query.answer()
        
        if query.data == "end_no":
            await query.edit_message_text("💕 Lanjutkan...")
            return ConversationHandler.END
        
        user_id = query.from_user.id
        session = self.sessions[user_id]
        name = session['name']
        
        del self.sessions[user_id]
        
        await query.edit_message_text(
            f"💔 **Hubungan Berakhir** 💔\n\n"
            f"Perjalananmu dengan **{name}** telah usai.\n\n"
            f"✨ **Semua data telah dihapus** ✨\n\n"
            f"Ketik /start untuk memulai hubungan baru...",
            parse_mode='Markdown'
        )
        
        logger.info(f"User {user_id} ended relationship")
        return ConversationHandler.END
    
    # ===== CANCEL COMMAND =====
    
    async def cmd_cancel(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /cancel command"""
        await update.message.reply_text("❌ Dibatalkan.")
        return ConversationHandler.END
    
    # ===== MESSAGE HANDLER =====
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle all messages"""
        user = update.effective_user
        user_id = user.id
        message = update.message.text
        
        if user_id not in self.sessions:
            await update.message.reply_text(
                "❌ Belum ada hubungan. Ketik /start untuk memilih role!"
            )
            return
        
        session = self.sessions[user_id]
        
        session['messages'] = session.get('messages', 0) + 1
        session['last_active'] = datetime.now().isoformat()
        
        new_level = 1 + (session['messages'] // 10)
        if new_level > 12:
            new_level = 12
        if new_level > session['level']:
            session['level'] = new_level
            level_up = True
            
            if new_level == 12:
                session['level'] = 7
                reset_msg = "\n\n🔄 **LEVEL MAX! Reset ke Level 7 dengan kenangan baru!**"
            else:
                reset_msg = ""
        else:
            level_up = False
            reset_msg = ""
        
        await update.message.chat.send_action("typing")
        
        self.db.save_conversation(
            user_id, 
            "user", 
            message
        )
        
        # Simple response
        responses = [
            "*tersenyum* Hmm... iya?",
            "*memandang* Lanjutkan...",
            "Aku dengerin kok...",
            "*mengangguk* Terus?",
            "Hehe... kamu lucu",
            "Iya... aku ngerti"
        ]
        
        response = random.choice(responses)
        
        await update.message.reply_text(response)
        
        self.db.save_conversation(
            user_id,
            "assistant",
            response
        )
        
        if level_up:
            await update.message.reply_text(
                f"✨ **Level Up!** Sekarang Level {session['level']}/12{reset_msg}"
            )
    
    # ===== ERROR HANDLER =====
    
    async def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Global error handler"""
        logger.error(f"Error: {context.error}", exc_info=True)
        
        try:
            if update and update.effective_message:
                await update.effective_message.reply_text(
                    "😔 Maaf, ada error kecil. Coba lagi ya!"
                )
        except:
            pass
