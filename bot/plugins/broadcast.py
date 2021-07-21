from pyrogram import filters, Client
from bot.database import Database

db = Database()

ADMINS = [597102833, 241413457, 475173147]

@Client.on_message(filters.command("broadcast") & filters.private & filters.user(ADMINS), group=2)
async def start_broadcast(client, message):
    if msg := message.reply_to_message:
        mes = await msg.reply_text("Broadcasting started", True)
        success = 0
        failed = 0
        msg_text = "**--Done--**\n` Total: {}\n Success: {}\n Failed: {}\n`"
        async for user in db.users.find():
            try:
                await msg.copy(user['user_id'])
                success += 1
            except Exception:
                failed += 1
            if success % 10 == 0:
                try:
                    await mes.edit(msg_text.format(success + failed, success, failed), parse_mode="md")
                except Exception:
                    pass
        await mes.edit(f"**Broadcasting completed** \n {msg_text.format(success + failed, success, failed)}",  parse_mode="md")

    else:
        await message.reply_text("Should be a reply to message")


@Client.on_message(filters.command("stats") & filters.private & filters.user(ADMINS), group=1)
async def get_count(client, message):
    count = await db.users.estimated_document_count()
    await message.reply_text(f"User count: {count}")
