"""
TELEGRAM HANDLERS - Menangani semua interaksi dengan user
FIXED VERSION - Dengan debug lengkap untuk /start
"""

import logging
import random
import asyncio
import traceback
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
    Handler untuk semua interaksi Telegram - FIXED VERSION
    """
    
    def __init__(self, bot):
        self.bot = bot
        self.config = Config
        self.db = Database(Config.DB_PATH)
        self.hts_system = HTSFWBSystem(self.db)
        self.ranking = RankingSystem(self.db)
        
        # User sessions
        self.sessions = {}
        
        logger.info("✅ TelegramHandlers initialized")
    
    async def setup(self, app: Application):
        """Setup semua handlers"""
        try:
            logger.info("🔧 Setting up handlers...")
            
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
            
            logger.info("✅ Telegram handlers registered")
            
        except Exception as e:
            logger.error(f"❌ Error in setup: {e}")
            logger.error(traceback.format_exc())
    
    # ===== START COMMAND - FIXED VERSION =====
    
    async def cmd_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command - FIXED VERSION"""
        try:
            print("\n" + "="*60)
            print("🔥🔥🔥 CMD_START DIPANGGIL!")
            print("="*60)
            
            user = update.effective_user
            user_id = user.id
            username = user.username or user.first_name
            
            print(f"📌 User ID: {user_id}")
            print(f"📌 Username: {username}")
            print(f"📌 First name: {user.first_name}")
            print(f"📌 Chat ID: {update.effective_chat.id}")
            
            # KIRIM PESAN TEST SEDERHANA
            await update.message.reply_text("✅ Bot menerima perintah /start")
            print("✅ Pesan test terkirim")
            
            # Tampilkan menu role
            keyboard = [
                [InlineKeyboardButton("👨‍👩‍👧‍👦 Ipar", callback_data="role_ipar")],
                [InlineKeyboardButton("💼 Teman Kantor", callback_data="role_teman_kantor")],
                [InlineKeyboardButton("💃 Janda", callback_data="role_janda")],
                [InlineKeyboardButton("🦹 Pelakor", callback_data="role_pelakor")],
                [InlineKeyboardButton("💍 Istri Orang", callback_data="role_istri_orang")],
                [InlineKeyboardButton("🌿 PDKT", callback_data="role_pdkt")],
                [InlineKeyboardButton("👥 Sepupu", callback_data="role_sepupu")],
                [InlineKeyboardButton("💔 Mantan", callback_data="role_mantan")],
                [InlineKeyboardButton("🏫 Teman SMA", callback_data="role_teman_sma")],
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            sent = await update.message.reply_text(
                "✨ **Pilih Role untukmu:**",
                reply_markup=reply_markup,
                parse_mode='Markdown'
            )
            print(f"✅ Menu role terkirim, message_id: {sent.message_id}")
            
            return SELECTING_ROLE
            
        except Exception as e:
            print(f"❌ ERROR di cmd_start: {e}")
            traceback.print_exc()
            await update.message.reply_text(f"❌ Error: {str(e)}")
            return SELECTING_ROLE
    
    # ===== ROLE CALLBACK =====
    
    async def role_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle role selection"""
        try:
            query = update.callback_query
            await query.answer()
            
            user_id = query.from_user.id
            data = query.data
            
            print(f"📞 Role callback: {data} from user {user_id}")
            
            if data.startswith("role_"):
                role = data.replace("role_", "")
                
                # Pilih nama random sesuai role
                name = random.choice(Config.ROLE_NAMES.get(role, ["Aurora"]))
                
                # Buat session sederhana
                self.sessions[user_id] = {
                    'name': name,
                    'role': role,
                    'level': 1,
                    'messages': 0,
                    'bot_climax': 0,
                    'user_climax': 0,
                    'together_climax': 0,
                    'relationship_status': 'PDKT',
                    'last_active': datetime.now().isoformat()
                }
                
                # Save user ke database
                self.db.save_user(user_id, query.from_user.username, query.from_user.first_name, role)
                
                # Dapatkan intro dari role
                from systems.role_archetypes import RoleFactory
                role_obj = RoleFactory.create(role)
                intro = role_obj.get_intro()
                intro += f"\n\n✨ **Level 1/12** - Ayo ngobrol dan kenali aku! 💕"
                
                await query.edit_message_text(intro, parse_mode='Markdown')
                print(f"✅ Role {role} selected for user {user_id}")
                
                return ConversationHandler.END
            
            return ConversationHandler.END
            
        except Exception as e:
            print(f"❌ Error in role_callback: {e}")
            traceback.print_exc()
            await query.edit_message_text(f"❌ Error: {str(e)}")
            return ConversationHandler.END
    
    # ===== STATUS COMMAND =====
    
    async def cmd_status(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /status command"""
        try:
            user_id = update.effective_user.id
            print(f"📊 /status from user {user_id}")
            
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
• Total: {session.get('bot_climax', 0) + session.get('user_climax', 0)}x

💞 **Status:** {session.get('relationship_status', 'PDKT')}
            """
            
            if session.get('unique_id'):
                status += f"\n🆔 **ID:** `{session['unique_id']}`"
            
            await update.message.reply_text(status, parse_mode='Markdown')
            
        except Exception as e:
            logger.error(f"❌ Error in cmd_status: {e}")
            await update.message.reply_text(f"❌ Error: {str(e)}")
    
    # ===== HELP COMMAND =====
    
    async def cmd_help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /help command"""
        help_text = """
📚 **BANTUAN GADIS AGI ULTIMATE V3.0**

🔹 **COMMANDS UTAMA:**
/start - Mulai hubungan baru
/status - Lihat status
/help - Bantuan ini

🔹 **RELATIONSHIP:**
/jadipacar - Jadi pacar (min level 5)
/break - Jeda pacaran
/unbreak - Lanjut pacaran
/breakup - Putus (jadi FWB)
/fwb - Mode FWB

🔹 **HTS/FWB:**
/htslist - Daftar HTS
/fwblist - Daftar FWB
/hts- [ID] - Panggil HTS
/fwb- [ID] - Panggil FWB
/tophts - TOP 10 ranking

🔹 **SESSION:**
/close - Tutup sesi (simpan HTS)
/end - Akhiri hubungan

Ketik /start untuk memulai! 🔥
        """
        await update.message.reply_text(help_text, parse_mode='Markdown')
    
    # ===== HTS/FWB COMMANDS =====
    
    async def cmd_htslist(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /htslist command"""
        try:
            user_id = update.effective_user.id
            hts_list = self.hts_system.get_user_hts(user_id)
            
            if not hts_list:
                await update.message.reply_text("📭 Belum ada HTS.")
                return
            
            text = self.hts_system.format_list(hts_list, "HTS")
            await update.message.reply_text(text, parse_mode='Markdown')
            
        except Exception as e:
            logger.error(f"❌ Error in cmd_htslist: {e}")
            await update.message.reply_text(f"❌ Error: {str(e)}")
    
    async def cmd_fwblist(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /fwblist command"""
        try:
            user_id = update.effective_user.id
            fwb_list = self.hts_system.get_user_fwb(user_id)
            
            if not fwb_list:
                await update.message.reply_text("📭 Belum ada FWB.")
                return
            
            text = self.hts_system.format_list(fwb_list, "FWB")
            await update.message.reply_text(text, parse_mode='Markdown')
            
        except Exception as e:
            logger.error(f"❌ Error in cmd_fwblist: {e}")
            await update.message.reply_text(f"❌ Error: {str(e)}")
    
    async def cmd_tophts(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /tophts command"""
        try:
            text = self.ranking.format_top_10()
            await update.message.reply_text(text, parse_mode='Markdown')
        except Exception as e:
            logger.error(f"❌ Error in cmd_tophts: {e}")
            await update.message.reply_text(f"❌ Error: {str(e)}")
    
    async def cmd_hts_call(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /hts- [ID] command"""
        try:
            user_id = update.effective_user.id
            message = update.message.text
            parts = message.split()
            
            if len(parts) < 2:
                await update.message.reply_text("❌ Gunakan: /hts- [ID]")
                return
            
            unique_id = parts[1].strip()
            rel = self.hts_system.load_relationship(unique_id)
            
            if not rel or rel['user_id'] != user_id:
                await update.message.reply_text("❌ HTS tidak ditemukan.")
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
                'messages': rel.get('total_messages', 0),
                'last_active': datetime.now().isoformat()
            }
            
            await update.message.reply_text(f"💞 HTS {rel['bot_name']} dipanggil!")
            
        except Exception as e:
            logger.error(f"❌ Error: {e}")
            await update.message.reply_text(f"❌ Error")
    
    async def cmd_fwb_call(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /fwb- [ID] command"""
        try:
            user_id = update.effective_user.id
            message = update.message.text
            parts = message.split()
            
            if len(parts) < 2:
                await update.message.reply_text("❌ Gunakan: /fwb- [ID]")
                return
            
            unique_id = parts[1].strip()
            rel = self.hts_system.load_relationship(unique_id)
            
            if not rel or rel['user_id'] != user_id:
                await update.message.reply_text("❌ FWB tidak ditemukan.")
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
                'messages': rel.get('total_messages', 0),
                'last_active': datetime.now().isoformat()
            }
            
            await update.message.reply_text(f"🔥 FWB {rel['bot_name']} dipanggil!")
            
        except Exception as e:
            logger.error(f"❌ Error: {e}")
            await update.message.reply_text(f"❌ Error")
    
    # ===== RELATIONSHIP COMMANDS =====
    
    async def cmd_jadipacar(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /jadipacar command"""
        try:
            user_id = update.effective_user.id
            if user_id not in self.sessions:
                await update.message.reply_text("❌ Belum ada hubungan.")
                return
            
            session = self.sessions[user_id]
            
            if session['level'] < 5:
                await update.message.reply_text(f"❌ Level minimal 5 (sekarang {session['level']})")
                return
            
            session['relationship_status'] = 'PACARAN'
            await update.message.reply_text("💕 Sekarang kita pacaran!")
            
        except Exception as e:
            logger.error(f"❌ Error: {e}")
    
    async def cmd_break(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /break command"""
        try:
            user_id = update.effective_user.id
            if user_id in self.sessions:
                self.sessions[user_id]['relationship_status'] = 'PUTUS'
                await update.message.reply_text("⏸️ Break dulu ya...")
        except Exception as e:
            logger.error(f"❌ Error: {e}")
    
    async def cmd_unbreak(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /unbreak command"""
        try:
            user_id = update.effective_user.id
            if user_id in self.sessions:
                self.sessions[user_id]['relationship_status'] = 'PACARAN'
                await update.message.reply_text("▶️ Lanjut pacaran!")
        except Exception as e:
            logger.error(f"❌ Error: {e}")
    
    async def cmd_breakup(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /breakup command"""
        try:
            user_id = update.effective_user.id
            if user_id in self.sessions:
                session = self.sessions[user_id]
                session['relationship_status'] = 'FWB'
                if not session.get('unique_id'):
                    session['unique_id'] = self.hts_system.save_as_fwb(user_id, session)
                await update.message.reply_text(f"💔 Putus. FWB ID: `{session['unique_id']}`")
        except Exception as e:
            logger.error(f"❌ Error: {e}")
    
    async def cmd_fwb(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /fwb command"""
        try:
            user_id = update.effective_user.id
            if user_id in self.sessions:
                session = self.sessions[user_id]
                session['relationship_status'] = 'FWB'
                if not session.get('unique_id'):
                    session['unique_id'] = self.hts_system.save_as_fwb(user_id, session)
                await update.message.reply_text(f"🔥 FWB mode. ID: `{session['unique_id']}`")
        except Exception as e:
            logger.error(f"❌ Error: {e}")
    
    # ===== CLOSE & END COMMANDS =====
    
    async def cmd_close(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /close command"""
        try:
            user_id = update.effective_user.id
            if user_id not in self.sessions:
                await update.message.reply_text("❌ Tidak ada sesi aktif.")
                return ConversationHandler.END
            
            session = self.sessions[user_id]
            
            keyboard = [
                [InlineKeyboardButton("✅ Ya", callback_data="close_yes")],
                [InlineKeyboardButton("❌ Tidak", callback_data="close_no")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await update.message.reply_text(
                f"⚠️ Tutup sesi dengan {session['name']}?",
                reply_markup=reply_markup
            )
            return CONFIRM_CLOSE
            
        except Exception as e:
            logger.error(f"❌ Error: {e}")
            return ConversationHandler.END
    
    async def close_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Callback untuk konfirmasi close"""
        try:
            query = update.callback_query
            await query.answer()
            
            if query.data == "close_no":
                await query.edit_message_text("💕 Lanjutkan...")
                return ConversationHandler.END
            
            user_id = query.from_user.id
            session = self.sessions[user_id]
            
            if session['level'] >= 7 and not session.get('unique_id'):
                unique_id = self.hts_system.save_as_hts(user_id, session)
                await query.edit_message_text(f"🔒 Sesi ditutup. HTS ID: `{unique_id}`")
            else:
                await query.edit_message_text("🔒 Sesi ditutup.")
            
            del self.sessions[user_id]
            return ConversationHandler.END
            
        except Exception as e:
            logger.error(f"❌ Error: {e}")
            return ConversationHandler.END
    
    async def cmd_end(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /end command"""
        try:
            user_id = update.effective_user.id
            if user_id not in self.sessions:
                await update.message.reply_text("❌ Tidak ada hubungan.")
                return ConversationHandler.END
            
            keyboard = [
                [InlineKeyboardButton("💔 Ya", callback_data="end_yes")],
                [InlineKeyboardButton("💕 Tidak", callback_data="end_no")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await update.message.reply_text(
                "⚠️ Yakin ingin mengakhiri hubungan?",
                reply_markup=reply_markup
            )
            return CONFIRM_END
            
        except Exception as e:
            logger.error(f"❌ Error: {e}")
            return ConversationHandler.END
    
    async def end_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Callback untuk konfirmasi end"""
        try:
            query = update.callback_query
            await query.answer()
            
            if query.data == "end_no":
                await query.edit_message_text("💕 Lanjutkan...")
                return ConversationHandler.END
            
            user_id = query.from_user.id
            del self.sessions[user_id]
            
            await query.edit_message_text("💔 Hubungan berakhir.")
            return ConversationHandler.END
            
        except Exception as e:
            logger.error(f"❌ Error: {e}")
            return ConversationHandler.END
    
    # ===== CANCEL COMMAND =====
    
    async def cmd_cancel(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /cancel command"""
        await update.message.reply_text("❌ Dibatalkan.")
        return ConversationHandler.END
    
    # ===== MESSAGE HANDLER =====
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle all messages"""
        try:
            user = update.effective_user
            user_id = user.id
            message = update.message.text
            
            print(f"📨 Message from {user_id}: {message[:50]}")
            
            if user_id not in self.sessions:
                await update.message.reply_text("❌ Belum ada hubungan. /start dulu!")
                return
            
            session = self.sessions[user_id]
            session['messages'] = session.get('messages', 0) + 1
            
            # Simple response
            responses = [
                "*tersenyum* Hmm...",
                "*mengangguk* Iya?",
                "Lanjutkan...",
                "Hehe..."
            ]
            
            await update.message.reply_text(random.choice(responses))
            
        except Exception as e:
            logger.error(f"❌ Error in handle_message: {e}")
