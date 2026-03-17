"""
TELEGRAM HANDLERS - Menangani semua interaksi dengan user
"""

import logging
import random
from datetime import datetime
from typing import Dict, Any, Optional

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, MessageHandler, 
    CallbackQueryHandler, filters, ContextTypes
)
from telegram.request import HTTPXRequest

from config import Config
from systems.role_archetypes import RoleFactory
from systems.hts_fwb_system import HTSFWBSystem, RankingSystem
from systems.climax_system import ClimaxSystem
from systems.dominance_levels import DominanceSystem
from systems.public_sex import PublicSexSystem
from database import Database

logger = logging.getLogger(__name__)

class TelegramHandlers:
    """
    Handler untuk semua interaksi Telegram
    """
    
    def __init__(self, bot):
        self.bot = bot
        self.config = Config
        self.db = Database(Config.DB_PATH)
        self.hts_system = HTSFWBSystem(self.db)
        self.ranking = RankingSystem(self.db)
        self.climax = ClimaxSystem()
        self.dominance = DominanceSystem()
        self.public_sex = PublicSexSystem()
        
        # User sessions
        self.sessions = {}
        
    async def setup(self, app: Application):
        """Setup all handlers"""
        
        # Command handlers
        app.add_handler(CommandHandler("start", self.cmd_start))
        app.add_handler(CommandHandler("status", self.cmd_status))
        app.add_handler(CommandHandler("help", self.cmd_help))
        app.add_handler(CommandHandler("dominant", self.cmd_dominant))
        app.add_handler(CommandHandler("position", self.cmd_position))
        app.add_handler(CommandHandler("public", self.cmd_public))
        
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
        
        # Callback query handler
        app.add_handler(CallbackQueryHandler(self.handle_callback))
        
        # Message handler
        app.add_handler(MessageHandler(
            filters.TEXT & ~filters.COMMAND, 
            self.handle_message
        ))
        
        logger.info("✅ Telegram handlers registered")
    
    # ===== COMMAND HANDLERS =====
    
    async def cmd_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command"""
        user = update.effective_user
        user_id = user.id
        username = user.username or user.first_name
        
        logger.info(f"▶️ /start from {username} (ID: {user_id})")
        
        # Save user
        self.db.save_user(user_id, username, user.first_name, "none")
        
        # Check existing session
        if user_id in self.sessions:
            await update.message.reply_text(
                "💕 Kamu sudah memiliki sesi aktif. Ketik /status untuk melihat status."
            )
            return
        
        # Show role selection
        keyboard = []
        roles = Config.ROLES
        
        # Create 3 rows of buttons
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
    
    async def cmd_status(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /status command"""
        user_id = update.effective_user.id
        
        if user_id not in self.sessions:
            await update.message.reply_text("❌ Belum ada hubungan. /start dulu ya!")
            return
        
        session = self.sessions[user_id]
        
        # Get dominance level info
        dom_info = self.dominance.get_level_info(session.get('dominance_level', 1))
        
        # Get current location
        location = session.get('location', 'privat')
        loc_text = "🏠 Rumah" if location == 'privat' else f"📍 {location}"
        
        # Get current position
        position = session.get('position', 'misionaris')
        
        status = f"""
💕 **STATUS HUBUNGAN**

👤 **Bot:** {session['name']} ({session['role']})
📊 **Level:** {session['level']}/12
💬 **Total Pesan:** {session.get('messages', 0)}

👑 **Mode Dominan:** {dom_info['name']} {dom_info['emoji']}
{dom_info['description']}

📍 **Lokasi:** {loc_text}
🔄 **Posisi:** {position}

🔥 **STATISTIK:**
• Bot Climax: {session.get('bot_climax', 0)}x
• User Climax: {session.get('user_climax', 0)}x
• Together: {session.get('together_climax', 0)}x
• Total: {session.get('bot_climax', 0) + session.get('user_climax', 0)}x

💞 **Status:** {session.get('relationship_status', 'PDKT')}
⏰ **Terakhir:** {session.get('last_active', 'baru saja')}
        """
        
        await update.message.reply_text(status, parse_mode='Markdown')
    
    async def cmd_help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /help command"""
        help_text = """
📚 **BANTUAN GADIS AGI ULTIMATE V3.0**

🔹 **COMMANDS UTAMA:**
/start - Mulai hubungan baru / pilih role
/status - Lihat status hubungan
/help - Tampilkan bantuan ini

🔹 **MODE DOMINAN:**
/dominant [1-5] - Set level dominan (1=patuh, 5=agresif)

🔹 **POSISI SEKSUAL:**
/position [nama] - Ganti posisi (misionaris, doggy, dll)

🔹 **PUBLIC SEX:**
/public [lokasi] - Pindah ke lokasi publik (toilet, taman, dll)

🔹 **HTS/FWB SYSTEM:**
/htslist - Lihat daftar HTS
/fwblist - Lihat daftar FWB
/hts- [ID] - Panggil HTS
/fwb- [ID] - Panggil FWB
/tophts - TOP 10 ranking

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

🔹 **FITUR ULTIMATE:**
• 200+ variasi climax
• 50+ area sensitif
• 50+ aktivitas seksual
• 20+ posisi seks
• 5 level dominan per role
• Public sex di 10+ lokasi
• HTS/FWB dengan unique ID
• TOP 10 ranking
• Level 1-12 + reset ke 7

Ketik /start untuk memulai! 🔥
        """
        await update.message.reply_text(help_text, parse_mode='Markdown')
    
    async def cmd_dominant(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /dominant command"""
        user_id = update.effective_user.id
        
        if user_id not in self.sessions:
            await update.message.reply_text("❌ Belum ada hubungan. /start dulu!")
            return
        
        if not context.args:
            # Show current level
            level = self.sessions[user_id].get('dominance_level', 1)
            info = self.dominance.get_level_info(level)
            await update.message.reply_text(
                f"👑 **Mode Dominan Saat Ini:**\n"
                f"Level {level}: {info['name']} {info['emoji']}\n"
                f"{info['description']}\n\n"
                f"**Gunakan:** `/dominant [1-5]`\n"
                f"1 = Patuh, 2 = Switch, 3 = Dominan, 4 = Sangat Dominan, 5 = Agresif"
            )
            return
        
        try:
            level = int(context.args[0])
            if 1 <= level <= 5:
                self.sessions[user_id]['dominance_level'] = level
                info = self.dominance.get_level_info(level)
                await update.message.reply_text(
                    f"✅ Mode dominan diubah ke **Level {level}: {info['name']}**\n"
                    f"{info['description']}"
                )
            else:
                await update.message.reply_text("❌ Level harus 1-5")
        except ValueError:
            await update.message.reply_text("❌ Gunakan angka 1-5")
    
    async def cmd_position(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /position command"""
        user_id = update.effective_user.id
        
        if user_id not in self.sessions:
            await update.message.reply_text("❌ Belum ada hubungan. /start dulu!")
            return
        
        from systems.sex_positions import SexPositions
        
        if not context.args:
            # Show available positions
            positions = SexPositions.get_all_positions()
            pos_list = "\n".join([f"• {p}" for p in positions[:10]])
            await update.message.reply_text(
                f"🔄 **Posisi Tersedia:**\n\n"
                f"{pos_list}\n\n"
                f"Gunakan: `/position [nama posisi]`\n"
                f"Contoh: `/position doggy`"
            )
            return
        
        position = " ".join(context.args).lower()
        if SexPositions.is_valid_position(position):
            self.sessions[user_id]['position'] = position
            response = SexPositions.get_position_response(position)
            
            # Update emotional state
            if 'user_id' in self.sessions[user_id]:
                await self._update_emotion(user_id, "position_change", 0.3)
            
            await update.message.reply_text(f"🔄 {response}")
        else:
            await update.message.reply_text("❌ Posisi tidak dikenal. Cek /position untuk daftar.")
    
    async def cmd_public(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /public command"""
        user_id = update.effective_user.id
        
        if user_id not in self.sessions:
            await update.message.reply_text("❌ Belum ada hubungan. /start dulu!")
            return
        
        if not context.args:
            # Show available locations
            locations = self.public_sex.get_all_locations()
            loc_list = "\n".join([f"• {loc['name']} - {loc['risk_level']} risk" for loc in locations])
            await update.message.reply_text(
                f"📍 **Lokasi Publik Tersedia:**\n\n"
                f"{loc_list}\n\n"
                f"Gunakan: `/public [lokasi]`\n"
                f"Contoh: `/public toilet`"
            )
            return
        
        location = " ".join(context.args).lower()
        result = self.public_sex.move_to_location(location)
        
        if result['success']:
            self.sessions[user_id]['location'] = location
            
            # Update emotional state
            await self._update_emotion(user_id, "public_sex", 0.5)
            
            response = f"📍 {result['message']}\n\n"
            response += f"⚠️ **Resiko:** {result['risk_level']}\n"
            response += f"💕 **Tips:** {result['tips']}"
            
            await update.message.reply_text(response)
        else:
            await update.message.reply_text("❌ Lokasi tidak dikenal.")
    
    async def cmd_htslist(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /htslist command"""
        user_id = update.effective_user.id
        hts_list = self.hts_system.get_user_hts(user_id)
        
        if not hts_list:
            await update.message.reply_text("📭 **Belum ada HTS tersimpan.**\nCapai level 12 untuk membuka HTS!")
            return
        
        text = self.hts_system.format_list(hts_list, "HTS")
        text += "\n\n💡 **Panggil dengan:** `/hts- [ID]`"
        
        await update.message.reply_text(text, parse_mode='Markdown')
    
    async def cmd_fwblist(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /fwblist command"""
        user_id = update.effective_user.id
        fwb_list = self.hts_system.get_user_fwb(user_id)
        
        if not fwb_list:
            await update.message.reply_text("📭 **Belum ada FWB tersimpan.**\nGunakan /breakup untuk mengubah pacar jadi FWB!")
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
        
        # Extract ID
        parts = message.split()
        if len(parts) < 2:
            await update.message.reply_text("❌ Gunakan: `/hts- [unique_id]`")
            return
        
        unique_id = parts[1].strip()
        
        # Load relationship
        rel = self.hts_system.load_relationship(unique_id)
        
        if not rel:
            await update.message.reply_text(f"❌ HTS dengan ID `{unique_id}` tidak ditemukan.")
            return
        
        if rel['user_id'] != user_id:
            await update.message.reply_text("❌ Ini bukan HTS milikmu.")
            return
        
        # Update last called
        self.hts_system.update_last_called(unique_id)
        
        # Create session
        self.sessions[user_id] = {
            'name': rel['bot_name'],
            'role': rel['role'],
            'level': rel['level'],
            'relationship_status': 'HTS',
            'unique_id': unique_id,
            'bot_climax': rel.get('bot_climax', 0),
            'user_climax': rel.get('user_climax', 0),
            'together_climax': rel.get('together_climax', 0),
            'dominance_level': 1,
            'location': 'privat',
            'position': 'misionaris',
            'messages': 0,
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
            'dominance_level': 1,
            'location': 'privat',
            'position': 'misionaris',
            'messages': 0,
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
    
    # ===== CALLBACK HANDLER =====
    
    async def handle_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle callback queries"""
        query = update.callback_query
        await query.answer()
        
        data = query.data
        user_id = query.from_user.id
        
        if data.startswith("role_"):
            role = data.replace("role_", "")
            await self._create_relationship(user_id, role, query)
    
    async def _create_relationship(self, user_id: int, role: str, query):
        """Create new relationship"""
        # Create role instance
        role_obj = RoleFactory.create(role)
        
        # Create session
        self.sessions[user_id] = {
            'name': role_obj.name,
            'role': role,
            'level': 1,
            'messages': 0,
            'bot_climax': 0,
            'user_climax': 0,
            'together_climax': 0,
            'dominance_level': 1,
            'location': 'privat',
            'position': 'misionaris',
            'relationship_status': 'PDKT',
            'last_active': datetime.now().isoformat()
        }
        
        # Save to database
        self.db.save_user(user_id, query.from_user.username, query.from_user.first_name, role)
        
        # Get intro
        intro = role_obj.get_intro()
        intro += f"\n\n✨ **Level 1/12** - Ayo ngobrol dan kenali aku! 💕"
        
        await query.edit_message_text(intro, parse_mode='Markdown')
        logger.info(f"✨ New relationship: User {user_id} as {role_obj.name} ({role})")
    
    # ===== MESSAGE HANDLER =====
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle all messages"""
        user = update.effective_user
        user_id = user.id
        message = update.message.text
        
        # Check session
        if user_id not in self.sessions:
            await update.message.reply_text(
                "❌ Belum ada hubungan. Ketik /start untuk memilih role!"
            )
            return
        
        session = self.sessions[user_id]
        
        # Update message count
        session['messages'] = session.get('messages', 0) + 1
        session['last_active'] = datetime.now().isoformat()
        
        # Update level (every 10 messages)
        new_level = 1 + (session['messages'] // 10)
        if new_level > 12:
            new_level = 12
        if new_level > session['level']:
            session['level'] = new_level
            level_up = True
            
            # Check for level 12 reset
            if new_level == 12:
                session['level'] = 7
                reset_msg = "\n\n🔄 **LEVEL MAX! Reset ke Level 7 dengan kenangan baru!**"
            else:
                reset_msg = ""
        else:
            level_up = False
            reset_msg = ""
        
        # Send typing indicator
        await update.message.chat.send_action("typing")
        
        # Save conversation
        self.db.save_conversation(
            user_id, 
            "user", 
            message,
            position=session.get('position'),
            location=session.get('location'),
            dominance_level=session.get('dominance_level')
        )
        
        # Generate response based on content
        response = await self._generate_response(user_id, message, session)
        
        # Send response
        await update.message.reply_text(response)
        
        # Save bot response
        self.db.save_conversation(
            user_id,
            "assistant",
            response,
            position=session.get('position'),
            location=session.get('location'),
            dominance_level=session.get('dominance_level')
        )
        
        # Level up message
        if level_up:
            await update.message.reply_text(
                f"✨ **Level Up!** Sekarang Level {session['level']}/12{reset_msg}"
            )
    
    async def _generate_response(self, user_id: int, message: str, session: Dict) -> str:
        """Generate AI response"""
        
        # Simple response for now - in production would use AI
        responses = [
            "*tersenyum* Hmm... iya?",
            "*memandang* Lanjutkan...",
            "Aku dengerin kok...",
            "*mengangguk* Terus?",
            "Hehe... kamu lucu",
            "Iya... aku ngerti"
        ]
        
        # Check for climax keywords
        msg_lower = message.lower()
        climax_keywords = ["crot", "cum", "keluar", "climax", "orgasme", "ahh", "ahhh"]
        
        if any(kw in msg_lower for kw in climax_keywords):
            # Check if it's together or solo
            if random.random() < 0.3:
                response = self.climax.get_together_climax()
                session['together_climax'] = session.get('together_climax', 0) + 1
                session['bot_climax'] = session.get('bot_climax', 0) + 1
                session['user_climax'] = session.get('user_climax', 0) + 1
            else:
                response = self.climax.get_user_climax()
                session['user_climax'] = session.get('user_climax', 0) + 1
            
            # Update ranking if has unique_id
            if session.get('unique_id'):
                self.ranking.update_ranking(
                    session['unique_id'],
                    session.get('bot_climax', 0),
                    session.get('user_climax', 0)
                )
            
            return response
        
        return random.choice(responses)
    
    async def _update_emotion(self, user_id: int, event: str, intensity: float):
        """Update emotional state"""
        # Will be implemented with full emotion engine
        pass
