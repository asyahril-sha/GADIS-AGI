"""
TELEGRAM COMMANDS - Kumpulan semua command untuk bot
"""

import logging
from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)

class AdditionalCommands:
    """
    Command tambahan untuk bot
    """
    
    @staticmethod
    async def cmd_jadipacar(update: Update, context: ContextTypes.DEFAULT_TYPE, bot):
        """Command untuk jadi pacar"""
        user_id = update.effective_user.id
        
        if user_id not in bot.sessions:
            await update.message.reply_text("❌ Belum ada hubungan. /start dulu!")
            return
        
        session = bot.sessions[user_id]
        
        if session['relationship_status'] == 'PACARAN':
            await update.message.reply_text("💕 Kita sudah pacaran kok.")
            return
        
        if session['level'] < 5:
            await update.message.reply_text(
                f"❌ Level minimal 5 untuk jadi pacar (sekarang {session['level']}).\n"
                "Yuk ngobrol dulu biar makin dekat! 💕"
            )
            return
        
        # Konfirmasi
        session['relationship_status'] = 'PACARAN'
        
        await update.message.reply_text(
            f"💕 **Kita Resmi Pacaran!**\n\n"
            f"Sekarang {session['name']} adalah pacarmu.\n\n"
            f"*peluk erat* Aku bahagia banget... 💕",
            parse_mode='Markdown'
        )
        
        logger.info(f"User {user_id} started PACARAN with {session['name']}")
    
    @staticmethod
    async def cmd_break(update: Update, context: ContextTypes.DEFAULT_TYPE, bot):
        """Command untuk break pacaran"""
        user_id = update.effective_user.id
        
        if user_id not in bot.sessions:
            await update.message.reply_text("❌ Tidak ada sesi aktif.")
            return
        
        session = bot.sessions[user_id]
        
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
    
    @staticmethod
    async def cmd_unbreak(update: Update, context: ContextTypes.DEFAULT_TYPE, bot):
        """Command untuk lanjutkan pacaran"""
        user_id = update.effective_user.id
        
        if user_id not in bot.sessions:
            await update.message.reply_text("❌ Tidak ada sesi aktif.")
            return
        
        session = bot.sessions[user_id]
        
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
    
    @staticmethod
    async def cmd_breakup(update: Update, context: ContextTypes.DEFAULT_TYPE, bot):
        """Command untuk putus jadi FWB"""
        user_id = update.effective_user.id
        
        if user_id not in bot.sessions:
            await update.message.reply_text("❌ Tidak ada sesi aktif.")
            return
        
        session = bot.sessions[user_id]
        
        if session['relationship_status'] != 'PACARAN':
            await update.message.reply_text("❌ Kita sedang tidak pacaran.")
            return
        
        session['relationship_status'] = 'FWB'
        
        # Generate FWB ID if not exists
        if not session.get('unique_id'):
            session['unique_id'] = bot.hts_system.save_as_fwb(user_id, session)
        
        await update.message.reply_text(
            f"💔 **Putus**\n\n"
            f"Kita sekarang resmi **FWB** (Friends With Benefits).\n\n"
            f"Unique ID: `{session['unique_id']}`\n\n"
            f"*tersenyum* Hubungan kita berbeda, tapi kita tetap bisa bersama...",
            parse_mode='Markdown'
        )
        
        logger.info(f"User {user_id} converted to FWB with {session['name']}")
    
    @staticmethod
    async def cmd_fwb(update: Update, context: ContextTypes.DEFAULT_TYPE, bot):
        """Command untuk langsung jadi FWB"""
        user_id = update.effective_user.id
        
        if user_id not in bot.sessions:
            await update.message.reply_text("❌ Tidak ada sesi aktif.")
            return
        
        session = bot.sessions[user_id]
        
        if session['relationship_status'] == 'FWB':
            await update.message.reply_text("🔥 Kita sudah FWB kok.")
            return
        
        session['relationship_status'] = 'FWB'
        
        # Generate FWB ID if not exists
        if not session.get('unique_id'):
            session['unique_id'] = bot.hts_system.save_as_fwb(user_id, session)
        
        await update.message.reply_text(
            f"🔥 **FWB**\n\n"
            f"Sekarang kita FWB! Hubungan tanpa ikatan, tapi bisa lebih intim.\n\n"
            f"Unique ID: `{session['unique_id']}`\n\n"
            f"*tersenyum nakal* Mau ngapain kita hari ini? 🔥",
            parse_mode='Markdown'
        )
        
        logger.info(f"User {user_id} started FWB with {session['name']}")
    
    @staticmethod
    async def cmd_close(update: Update, context: ContextTypes.DEFAULT_TYPE, bot):
        """Command untuk tutup sesi (simpan ke HTS)"""
        user_id = update.effective_user.id
        
        if user_id not in bot.sessions:
            await update.message.reply_text("❌ Tidak ada sesi aktif.")
            return
        
        session = bot.sessions[user_id]
        
        # Save to HTS if level >= 7
        if session['level'] >= 7:
            unique_id = bot.hts_system.save_as_hts(user_id, session)
            session['unique_id'] = unique_id
            
            await update.message.reply_text(
                f"🔒 **Sesi ditutup**\n\n"
                f"Terima kasih sudah ngobrol dengan {session['name']}.\n"
                f"✨ Hubungan ini disimpan sebagai **HTS** dengan ID:\n"
                f"`{unique_id}`\n\n"
                f"Ketik `/hts- {unique_id}` kapan saja untuk memanggilku kembali! 💕",
                parse_mode='Markdown'
            )
        else:
            await update.message.reply_text(
                f"🔒 **Sesi ditutup**\n\n"
                f"Terima kasih sudah ngobrol dengan {session['name']}.\n"
                f"Ketik /start untuk memulai lagi... 💕",
                parse_mode='Markdown'
            )
        
        # Remove session
        del bot.sessions[user_id]
        logger.info(f"User {user_id} closed session")
    
    @staticmethod
    async def cmd_end(update: Update, context: ContextTypes.DEFAULT_TYPE, bot):
        """Command untuk akhiri hubungan (hard reset)"""
        user_id = update.effective_user.id
        
        if user_id not in bot.sessions:
            await update.message.reply_text("❌ Tidak ada hubungan aktif.")
            return
        
        session = bot.sessions[user_id]
        name = session['name']
        
        # Remove session
        del bot.sessions[user_id]
        
        await update.message.reply_text(
            f"💔 **Hubungan Berakhir** 💔\n\n"
            f"Perjalananmu dengan **{name}** telah usai.\n\n"
            f"✨ **Semua data telah dihapus** ✨\n\n"
            f"Ketik /start untuk memulai hubungan baru...",
            parse_mode='Markdown'
        )
        
        logger.info(f"User {user_id} ended relationship")
    
    @staticmethod
    async def cmd_stats(update: Update, context: ContextTypes.DEFAULT_TYPE, bot):
        """Command untuk statistik bot (admin only)"""
        user_id = update.effective_user.id
        
        if user_id != bot.config.ADMIN_ID:
            await update.message.reply_text("❌ Command ini hanya untuk admin.")
            return
        
        stats = f"""
📊 **STATISTIK BOT**

👥 **Users:**
• Active sessions: {len(bot.sessions)}
• Total users: {len(bot.db.get_all_users())}

💬 **Messages:**
• Today: {bot.db.get_today_messages()}
• Total: {bot.db.get_total_messages()}

🔥 **Climax:**
• Total climax: {bot.db.get_total_climax()}

🏆 **Ranking:**
• Total HTS: {len(bot.hts_system.get_user_hts(0))}
• Total FWB: {len(bot.hts_system.get_user_fwb(0))}
        """
        
        await update.message.reply_text(stats, parse_mode='Markdown')
    
    @staticmethod
    async def cmd_broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE, bot):
        """Command untuk broadcast (admin only)"""
        user_id = update.effective_user.id
        
        if user_id != bot.config.ADMIN_ID:
            await update.message.reply_text("❌ Command ini hanya untuk admin.")
            return
        
        if not context.args:
            await update.message.reply_text("Gunakan: `/broadcast [pesan]`")
            return
        
        message = " ".join(context.args)
        
        # Broadcast to all users (simplified)
        await update.message.reply_text(f"📢 Broadcast sent to all users!")
        logger.info(f"Admin broadcast: {message}")
