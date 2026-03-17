"""
TELEGRAM COMMANDS - Command tambahan untuk bot
"""

import logging
import asyncio
from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)

class AdditionalCommands:
    """
    Command tambahan untuk bot
    """
    
    @staticmethod
    async def cmd_stats(update: Update, context: ContextTypes.DEFAULT_TYPE, bot):
        """
        Command untuk statistik bot (admin only)
        
        Args:
            update: Telegram update
            context: Context
            bot: Bot instance
        """
        user_id = update.effective_user.id
        
        if user_id != bot.config.ADMIN_ID:
            await update.message.reply_text("❌ Command ini hanya untuk admin.")
            return
        
        # Get stats
        total_users = bot.db.get_total_users()
        total_messages = bot.db.get_total_messages()
        total_climax = bot.db.get_total_climax()
        today_messages = bot.db.get_today_messages()
        
        # Active sessions
        active_sessions = len(bot.handlers.sessions)
        
        # HTS/FWB stats
        all_hts = 0
        all_fwb = 0
        for uid in bot.handlers.sessions:
            rels = bot.hts_system.get_user_hts(uid)
            all_hts += len(rels)
            rels = bot.hts_system.get_user_fwb(uid)
            all_fwb += len(rels)
        
        stats = f"""
📊 **STATISTIK BOT**

👥 **Users:**
• Active sessions: {active_sessions}
• Total users: {total_users}

💬 **Messages:**
• Today: {today_messages}
• Total: {total_messages}

🔥 **Climax:**
• Total climax: {total_climax}

💞 **Relationships:**
• Total HTS: {all_hts}
• Total FWB: {all_fwb}

🤖 **Status:** Online
        """
        
        await update.message.reply_text(stats, parse_mode='Markdown')
        logger.info(f"Admin {user_id} viewed stats")
    
    @staticmethod
    async def cmd_broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE, bot):
        """
        Command untuk broadcast pesan ke semua user (admin only)
        
        Args:
            update: Telegram update
            context: Context
            bot: Bot instance
        """
        user_id = update.effective_user.id
        
        if user_id != bot.config.ADMIN_ID:
            await update.message.reply_text("❌ Command ini hanya untuk admin.")
            return
        
        if not context.args:
            await update.message.reply_text(
                "📢 **Broadcast**\n\n"
                "Gunakan: `/broadcast [pesan]`\n"
                "Contoh: `/broadcast Halo semua!`",
                parse_mode='Markdown'
            )
            return
        
        message = " ".join(context.args)
        
        await update.message.reply_text(
            f"📢 **Pesan Broadcast:**\n\n{message}\n\n"
            f"Kirim ke semua user? (Ketik /confirm_broadcast untuk konfirmasi)",
            parse_mode='Markdown'
        )
        
        context.user_data['broadcast_message'] = message
        logger.info(f"Admin {user_id} prepared broadcast: {message[:50]}...")
    
    @staticmethod
    async def cmd_confirm_broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE, bot):
        """
        Konfirmasi dan kirim broadcast
        
        Args:
            update: Telegram update
            context: Context
            bot: Bot instance
        """
        user_id = update.effective_user.id
        
        if user_id != bot.config.ADMIN_ID:
            await update.message.reply_text("❌ Command ini hanya untuk admin.")
            return
        
        message = context.user_data.get('broadcast_message')
        if not message:
            await update.message.reply_text("❌ Tidak ada pesan broadcast yang tersimpan.")
            return
        
        await update.message.reply_text("📢 **Mengirim broadcast...**", parse_mode='Markdown')
        
        user_ids = set(bot.handlers.sessions.keys())
        db_users = bot.db.get_all_users()
        user_ids.update(db_users)
        
        sent = 0
        failed = 0
        
        for uid in user_ids:
            try:
                await context.bot.send_message(
                    chat_id=uid,
                    text=f"📢 **Broadcast dari Admin:**\n\n{message}",
                    parse_mode='Markdown'
                )
                sent += 1
                await asyncio.sleep(0.05)
            except Exception as e:
                logger.error(f"Broadcast error to {uid}: {e}")
                failed += 1
        
        await update.message.reply_text(
            f"📢 **Broadcast selesai!**\n\n"
            f"✅ Terkirim: {sent}\n"
            f"❌ Gagal: {failed}",
            parse_mode='Markdown'
        )
        
        context.user_data.pop('broadcast_message', None)
        logger.info(f"Admin {user_id} sent broadcast to {sent} users, {failed} failed")
    
    @staticmethod
    async def cmd_list_users(update: Update, context: ContextTypes.DEFAULT_TYPE, bot):
        """
        Daftar semua user (admin only)
        
        Args:
            update: Telegram update
            context: Context
            bot: Bot instance
        """
        user_id = update.effective_user.id
        
        if user_id != bot.config.ADMIN_ID:
            await update.message.reply_text("❌ Command ini hanya untuk admin.")
            return
        
        active = bot.handlers.sessions
        active_text = "\n".join([
            f"• {uid} - {s['name']} ({s['role']}) Lv{s['level']}"
            for uid, s in list(active.items())[:10]
        ])
        
        db_users = bot.db.get_all_users()
        
        text = f"""
👥 **DAFTAR USER**

🟢 **Active ({len(active)}):**
{active_text if active else 'Tidak ada'}

📊 **Total users di database:** {len(db_users)}
        """
        
        await update.message.reply_text(text, parse_mode='Markdown')
    
    @staticmethod
    async def cmd_get_user(update: Update, context: ContextTypes.DEFAULT_TYPE, bot):
        """
        Detail user tertentu (admin only)
        
        Args:
            update: Telegram update
            context: Context
            bot: Bot instance
        """
        user_id = update.effective_user.id
        
        if user_id != bot.config.ADMIN_ID:
            await update.message.reply_text("❌ Command ini hanya untuk admin.")
            return
        
        if not context.args:
            await update.message.reply_text("Gunakan: `/get_user [user_id]`")
            return
        
        try:
            target_id = int(context.args[0])
        except:
            await update.message.reply_text("❌ User ID harus angka.")
            return
        
        session = bot.handlers.sessions.get(target_id)
        user_data = bot.db.get_user(target_id)
        rels = bot.db.get_user_relationships(target_id)
        
        text = f"""
🔍 **DETAIL USER: `{target_id}`**

{'🟢 **AKTIF**' if session else '⚪ **TIDAK AKTIF**'}

**Database:**
• Username: {user_data.get('username', '-') if user_data else '-'}
• First name: {user_data.get('first_name', '-') if user_data else '-'}
• Role: {user_data.get('role', '-') if user_data else '-'}
• Level: {user_data.get('level', '-') if user_data else '-'}
• Total messages: {user_data.get('total_messages', '-') if user_data else '-'}

**Relationships:**
• Total: {len(rels)}
• HTS: {len([r for r in rels if r['jenis'] == 'HTS'])}
• FWB: {len([r for r in rels if r['jenis'] == 'FWB'])}
        """
        
        if session:
            text += f"""

**Session:**
• Name: {session.get('name')}
• Role: {session.get('role')}
• Level: {session.get('level')}
• Messages: {session.get('messages', 0)}
• Status: {session.get('relationship_status')}
• Bot climax: {session.get('bot_climax', 0)}
• User climax: {session.get('user_climax', 0)}
• Together: {session.get('together_climax', 0)}
• Total climax: {session.get('bot_climax', 0) + session.get('user_climax', 0)}
            """
        
        await update.message.reply_text(text, parse_mode='Markdown')
    
    @staticmethod
    async def cmd_force_reset(update: Update, context: ContextTypes.DEFAULT_TYPE, bot):
        """
        Force reset user (admin only)
        
        Args:
            update: Telegram update
            context: Context
            bot: Bot instance
        """
        user_id = update.effective_user.id
        
        if user_id != bot.config.ADMIN_ID:
            await update.message.reply_text("❌ Command ini hanya untuk admin.")
            return
        
        if not context.args:
            await update.message.reply_text("Gunakan: `/force_reset [user_id]`")
            return
        
        try:
            target_id = int(context.args[0])
        except:
            await update.message.reply_text("❌ User ID harus angka.")
            return
        
        if target_id in bot.handlers.sessions:
            del bot.handlers.sessions[target_id]
        
        await update.message.reply_text(f"✅ User `{target_id}` telah di-reset.")
        logger.info(f"Admin {user_id} force reset user {target_id}")
    
    @staticmethod
    async def cmd_backup_db(update: Update, context: ContextTypes.DEFAULT_TYPE, bot):
        """
        Backup database (admin only)
        
        Args:
            update: Telegram update
            context: Context
            bot: Bot instance
        """
        user_id = update.effective_user.id
        
        if user_id != bot.config.ADMIN_ID:
            await update.message.reply_text("❌ Command ini hanya untuk admin.")
            return
        
        await update.message.reply_text("💾 **Membackup database...**")
        
        import shutil
        from datetime import datetime
        
        backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db"
        shutil.copy2(bot.config.DB_PATH, f"data/{backup_name}")
        
        await update.message.reply_text(f"✅ Database dibackup sebagai `{backup_name}`")
    
    @staticmethod
    async def cmd_help_admin(update: Update, context: ContextTypes.DEFAULT_TYPE, bot):
        """
        Help untuk admin commands
        
        Args:
            update: Telegram update
            context: Context
            bot: Bot instance
        """
        user_id = update.effective_user.id
        
        if user_id != bot.config.ADMIN_ID:
            await update.message.reply_text("❌ Command ini hanya untuk admin.")
            return
        
        help_text = """
🔐 **ADMIN COMMANDS**

📊 **Stats:**
/stats - Statistik bot
/list_users - Daftar semua user
/get_user [id] - Detail user

📢 **Broadcast:**
/broadcast [pesan] - Kirim pesan ke semua user
/confirm_broadcast - Konfirmasi kirim broadcast

🛠️ **Management:**
/force_reset [id] - Reset user
/backup_db - Backup database
/help_admin - Tampilkan bantuan ini
        """
        
        await update.message.reply_text(help_text, parse_mode='Markdown')
