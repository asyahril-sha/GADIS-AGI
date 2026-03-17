"""
TELEGRAM HANDLERS - Menangani semua interaksi dengan user
VERSION 2.0 - Dengan 6 command tambahan: dominant, position, public, myclimax, climaxrank, climaxhistory
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
from systems.climax_system import ClimaxSystem
from systems.dominance_levels import DominanceSystem

# State untuk ConversationHandler
SELECTING_ROLE = 0
CONFIRM_CLOSE = 1
CONFIRM_END = 2
SELECTING_DOMINANT = 3
SELECTING_POSITION = 4
SELECTING_PUBLIC = 5

logger = logging.getLogger(__name__)

class TelegramHandlers:
    """
    Handler untuk semua interaksi Telegram
    Versi 2.0 dengan dukungan 31 command
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
        self.climax = ClimaxSystem()
        self.dominance = DominanceSystem()
        
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
        
        # Dominant conversation
        dominant_conv = ConversationHandler(
            entry_points=[CommandHandler('dominant', self.cmd_dominant)],
            states={
                SELECTING_DOMINANT: [
                    CallbackQueryHandler(self.dominant_callback, pattern='^dom_'),
                ],
            },
            fallbacks=[CommandHandler('cancel', self.cmd_cancel)],
            name="dominant_conversation"
        )
        
        # Position conversation
        position_conv = ConversationHandler(
            entry_points=[CommandHandler('position', self.cmd_position)],
            states={
                SELECTING_POSITION: [
                    CallbackQueryHandler(self.position_callback, pattern='^pos_'),
                ],
            },
            fallbacks=[CommandHandler('cancel', self.cmd_cancel)],
            name="position_conversation"
        )
        
        # Public conversation
        public_conv = ConversationHandler(
            entry_points=[CommandHandler('public', self.cmd_public)],
            states={
                SELECTING_PUBLIC: [
                    CallbackQueryHandler(self.public_callback, pattern='^pub_'),
                ],
            },
            fallbacks=[CommandHandler('cancel', self.cmd_cancel)],
            name="public_conversation"
        )
        
        # Add conversation handlers
        app.add_handler(start_conv)
        app.add_handler(close_conv)
        app.add_handler(end_conv)
        app.add_handler(dominant_conv)
        app.add_handler(position_conv)
        app.add_handler(public_conv)
        
        # ===== COMMAND HANDLERS =====
        app.add_handler(CommandHandler("status", self.cmd_status))
        app.add_handler(CommandHandler("help", self.cmd_help))
        app.add_handler(CommandHandler("myclimax", self.cmd_myclimax))
        app.add_handler(CommandHandler("climaxrank", self.cmd_climaxrank))
        app.add_handler(CommandHandler("climaxhistory", self.cmd_climaxhistory))
        
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
        
        logger.info("✅ Telegram handlers registered with 31 commands")
    
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
        
        # Set role modifiers untuk dominance system
        self.dominance.set_role_modifiers(role)
        
        self.sessions[user_id] = {
            'name': role_obj.name,
            'role': role,
            'level': 1,
            'messages': 0,
            'bot_climax': 0,
            'user_climax': 0,
            'together_climax': 0,
            'dominance_level': self.dominance.current_level,
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
        intro += f"\n\n👑 **Mode Dominan:** {self.dominance.get_description()}"
        
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
        
        # Dapatkan info dominan
        dom_info = self.dominance.get_level_info(session.get('dominance_level', 1))
        
        status = f"""
💕 **STATUS HUBUNGAN**

👤 **Bot:** {session['name']} ({session['role']})
📊 **Level:** {session['level']}/12
💬 **Total Pesan:** {session.get('messages', 0)}

👑 **Mode Dominan:** {dom_info['emoji']} Level {session.get('dominance_level', 1)}: {dom_info['name']}
{dom_info['description']}

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

🔹 **COMMANDS UTAMA (5):**
/start - Mulai hubungan baru / pilih role
/status - Lihat status hubungan
/help - Tampilkan bantuan ini
/cancel - Batalkan percakapan

🔹 **RELATIONSHIP (5):**
/jadipacar - Mulai hubungan pacaran (min level 5)
/break - Jeda pacaran
/unbreak - Lanjutkan pacaran
/breakup - Putus (jadi FWB)
/fwb - Mode Friends With Benefits

🔹 **HTS/FWB SYSTEM (5):**
/htslist - Lihat daftar HTS
/fwblist - Lihat daftar FWB
/hts- [ID] - Panggil HTS
/fwb- [ID] - Panggil FWB
/tophts - TOP 10 ranking

🔹 **SESSION (2):**
/close - Tutup sesi (simpan ke HTS)
/end - Akhiri hubungan & hapus data

🔹 **DOMINANCE (1):**
/dominant [1-5] - Set level dominan

🔹 **POSITION (1):**
/position [nama] - Ganti posisi seksual

🔹 **PUBLIC SEX (1):**
/public [lokasi] - Pindah ke lokasi publik

🔹 **CLIMAX (3):**
/myclimax - Lihat statistik climax
/climaxrank [ID] - Lihat peringkat
/climaxhistory [ID] - Lihat history

🔹 **ADMIN (8):**
/stats, /broadcast, /list_users, dll (khusus admin)

**TOTAL: 31 COMMANDS**
        """
        await update.message.reply_text(help_text, parse_mode='Markdown')
    
    # ===== DOMINANT COMMAND =====
    
    async def cmd_dominant(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /dominant command"""
        user_id = update.effective_user.id
        
        if user_id not in self.sessions:
            await update.message.reply_text("❌ Belum ada hubungan. /start dulu!")
            return ConversationHandler.END
        
        # Jika ada argumen angka
        if context.args and context.args[0].isdigit():
            level = int(context.args[0])
            if 1 <= level <= 5:
                self.dominance.set_level(level)
                self.sessions[user_id]['dominance_level'] = level
                
                info = self.dominance.get_level_info(level)
                await update.message.reply_text(
                    f"✅ Mode dominan diubah ke **Level {level}: {info['name']}**\n"
                    f"{info['description']}\n\n"
                    f"{self.dominance.get_phrase('action')}",
                    parse_mode='Markdown'
                )
                return ConversationHandler.END
        
        # Tampilkan pilihan level
        keyboard = [
            [InlineKeyboardButton("1 - Submissive 🥺", callback_data="dom_1")],
            [InlineKeyboardButton("2 - Switch 🔄", callback_data="dom_2")],
            [InlineKeyboardButton("3 - Dominant 👑", callback_data="dom_3")],
            [InlineKeyboardButton("4 - Very Dominant 👑👑", callback_data="dom_4")],
            [InlineKeyboardButton("5 - Agresif 🔥", callback_data="dom_5")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        current = self.sessions[user_id].get('dominance_level', 1)
        info = self.dominance.get_level_info(current)
        
        await update.message.reply_text(
            f"👑 **Pilih Level Dominan**\n\n"
            f"Saat ini: Level {current} - {info['name']} {info['emoji']}\n"
            f"{info['description']}\n\n"
            f"Pilih level baru:",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        
        return SELECTING_DOMINANT
    
    async def dominant_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Callback untuk pemilihan level dominan"""
        query = update.callback_query
        await query.answer()
        
        user_id = query.from_user.id
        level = int(query.data.replace("dom_", ""))
        
        self.dominance.set_level(level)
        self.sessions[user_id]['dominance_level'] = level
        
        info = self.dominance.get_level_info(level)
        
        await query.edit_message_text(
            f"✅ Mode dominan diubah ke **Level {level}: {info['name']}**\n"
            f"{info['description']}\n\n"
            f"{self.dominance.get_phrase('action')}",
            parse_mode='Markdown'
        )
        
        return ConversationHandler.END
    
    # ===== POSITION COMMAND =====
    
    async def cmd_position(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /position command"""
        user_id = update.effective_user.id
        
        if user_id not in self.sessions:
            await update.message.reply_text("❌ Belum ada hubungan. /start dulu!")
            return ConversationHandler.END
        
        # Untuk sementara, tampilkan pesan bahwa fitur belum lengkap
        await update.message.reply_text(
            "🔄 **Fitur Position akan segera hadir!**\n\n"
            "Sementara ini, nikmati fitur-fitur lain yang sudah tersedia.",
            parse_mode='Markdown'
        )
        
        return ConversationHandler.END
    
    async def position_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Callback untuk pemilihan posisi"""
        query = update.callback_query
        await query.answer()
        
        await query.edit_message_text(
            "🔄 Fitur position sedang dalam pengembangan."
        )
        
        return ConversationHandler.END
    
    # ===== PUBLIC SEX COMMAND =====
    
    async def cmd_public(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /public command"""
        user_id = update.effective_user.id
        
        if user_id not in self.sessions:
            await update.message.reply_text("❌ Belum ada hubungan. /start dulu!")
            return ConversationHandler.END
        
        # Untuk sementara, tampilkan pesan bahwa fitur belum lengkap
        await update.message.reply_text(
            "📍 **Fitur Public Sex akan segera hadir!**\n\n"
            "Sementara ini, nikmati fitur-fitur lain yang sudah tersedia.",
            parse_mode='Markdown'
        )
        
        return ConversationHandler.END
    
    async def public_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Callback untuk pemilihan lokasi publik"""
        query = update.callback_query
        await query.answer()
        
        await query.edit_message_text(
            "📍 Fitur public sex sedang dalam pengembangan."
        )
        
        return ConversationHandler.END
    
    # ===== MY CLIMAX COMMAND =====
    
    async def cmd_myclimax(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /myclimax command"""
        user_id = update.effective_user.id
        
        if user_id not in self.sessions:
            await update.message.reply_text("❌ Belum ada hubungan. /start dulu!")
            return
        
        session = self.sessions[user_id]
        
        # Hitung statistik
        bot = session.get('bot_climax', 0)
        user = session.get('user_climax', 0)
        together = session.get('together_climax', 0)
        total = bot + user
        
        # Hitung rata-rata per session (jika ada history)
        rels = self.db.get_user_relationships(user_id)
        total_history = sum(r.get('bot_climax', 0) + r.get('user_climax', 0) for r in rels)
        
        text = f"""
📊 **STATISTIK CLIMAX PRIBADI**

🔥 **Session Saat Ini:**
• Bot Climax: {bot}x
• User Climax: {user}x
• Together: {together}x
• **Total: {total}x**

📈 **Riwayat Hubungan:**
• Total dari semua HTS/FWB: {total_history}x
• Jumlah hubungan tersimpan: {len(rels)}
        """
        
        if session.get('unique_id'):
            text += f"\n🆔 **ID Aktif:** `{session['unique_id']}`"
        
        await update.message.reply_text(text, parse_mode='Markdown')
    
    # ===== CLIMAX RANK COMMAND =====
    
    async def cmd_climaxrank(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /climaxrank command"""
        if not context.args:
            # Tampilkan TOP 10
            top = self.ranking.get_top_10()
            
            if not top:
                await update.message.reply_text(
                    "🏆 **TOP 10 HTS/FWB**\n\nBelum ada data ranking.",
                    parse_mode='Markdown'
                )
                return
            
            text = self.ranking.format_top_10()
            await update.message.reply_text(text, parse_mode='Markdown')
            return
        
        # Cek specific ID
        unique_id = context.args[0]
        rank = self.ranking.get_user_rank(unique_id)
        
        if rank:
            await update.message.reply_text(
                f"🏆 **Peringkat #{rank}** untuk `{unique_id}`",
                parse_mode='Markdown'
            )
        else:
            await update.message.reply_text(
                f"❌ ID `{unique_id}` tidak ditemukan di TOP 10.",
                parse_mode='Markdown'
            )
    
    # ===== CLIMAX HISTORY COMMAND =====
    
    async def cmd_climaxhistory(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /climaxhistory command"""
        if not context.args:
            await update.message.reply_text(
                "📜 Gunakan: `/climaxhistory [unique_id]`\n"
                "Contoh: `/climaxhistory HTS-JANDA-1234-251224-001`",
                parse_mode='Markdown'
            )
            return
        
        unique_id = context.args[0]
        
        # Untuk sementara, tampilkan pesan bahwa fitur akan datang
        await update.message.reply_text(
            f"📜 **History Climax untuk `{unique_id}`**\n\n"
            f"Fitur ini akan segera hadir! Sementara itu, nikmati fitur lain.",
            parse_mode='Markdown'
        )
    
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
            'dominance_level': 1,
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
            'dominance_level': 1,
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
            message,
            position=session.get('position'),
            location=session.get('location'),
            dominance_level=session.get('dominance_level')
        )
        
        # Deteksi trigger dominan
        trigger_level = self.dominance.check_trigger(message)
        if trigger_level:
            self.dominance.set_level(trigger_level)
            session['dominance_level'] = trigger_level
            response = f"*menyesuaikan* {self.dominance.get_phrase('request')}"
            await update.message.reply_text(response)
            return
        
        # Update arousal-based dominance
        self.dominance.update_from_arousal(session.get('arousal', 0))
        if self.dominance.current_level != session.get('dominance_level'):
            session['dominance_level'] = self.dominance.current_level
        
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
            response,
            position=session.get('position'),
            location=session.get('location'),
            dominance_level=session.get('dominance_level')
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
