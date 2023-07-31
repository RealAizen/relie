from Hentai import psoheru as app, LOG_CHANNEL
from pyrogram import filters
from Hentai.utils.string_constant import PRICING_TEXT
from Hentai.database.client import Users, ban, unban

@app.on_message(filters.text & filters.command("ban"))
async def bannnnn(_, message):
    if Users.is_sudo(message.from_user.id) is False:
        return
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    else:
        user_id = message.text.split()[-1]
    try:
        uwu = ban(user_id)
        if uwu == False:
            await message.reply_text("Hehe, Good luck with that.", quote=True)
        await message.reply_text("Done.", quote=True)
    except Exception as e:
        await message.reply_text(f"Some error occurred. Probably that user doesn't exist.\n\n`{e}`", quote=True)
    
    text = f"#BANNED!"
    text += f"\n\nID - `{user_id}`"
    await app.send_message(LOG_CHANNEL, text)


@app.on_message(filters.text & filters.command("unban"))
async def unbamn(_, message):
    if Users.is_sudo(message.from_user.id) is False:
        return
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    else:
        user_id = message.text.split()[-1]
    if Users.is_sudo(user_id) is True:
        return
    uwu = unban(user_id)
    if uwu == True:
        await message.reply_text("Ok.", quote=True)
    text = f"#UNBANNED"
    text += f"\n\nID - `{user_id}`"
    await app.send_message(LOG_CHANNEL, text)
