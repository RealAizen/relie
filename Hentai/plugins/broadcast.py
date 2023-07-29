import asyncio, json, ast
from Hentai import psoheru as Client, LOG_CHANNEL
from pyrogram import filters 
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Hentai.database.client import Users
from Hentai.utils.string_constant import UPLOAD_TEXT

HENTAI_CHATID = -1001832743903

@Client.on_message(filters.command('broadcast', '/'))
async def bot_broadcast(bot:Client, message:Message):
    if Users.is_sudo(message.from_user.id) is False:
        return 
    successs = []
    successs.clear()
    status = await message.reply('Processing')
    filename = message.text.split()[-1]
    if not filename.endswith(".txt"):
        filename = f"{filename}.txt"
    if '-f' in message.text:
        if message.reply_to_message: 
            x = Users.all_user()
            for a in x:
                try:
                    x = await message.reply_to_message.forward(a) 
                    successs.append(a)
                    await asyncio.sleep(1)
                    await status.edit(f'**Sent** `{len(successs)}` **broadcast**`....`')
                except:
                    pass
            with open(filename, "w") as file:
                json.dump(successs, file)
            await status.edit(f'**Total Broadcast Sent** : `{len(successs)}`\n\nBroadcast ID : `{filename}`')
        else:
            await status.edit('Heyy Reply Message Tag Please')
    elif '-c' in message.text:
        if message.reply_to_message: 
            x = Users.all_user()
            for a in x:
                try:
                    x = await message.reply_to_message.copy(a)
                    successs.append((a, x.id))
                    await asyncio.sleep(1)
                    await status.edit(f'**Sent** `{len(successs)}` **broadcast**`....`')
                except:
                    pass    
            with open(filename, "w") as file:
                json.dump(successs, file)
            await status.edit(f'**Total Broadcast Sent** : `{len(successs)}`\n\nBroadcast ID : `{filename}`')
        else:
            await status.edit('Heyy Reply Message Tag Please')
    else:
        await status.edit('**Use Flags Please**\n**-f** - `To broadcast with quote`\n**-c** - `To broadcast without quote`')
    text = f"#BROADCAST"
    text += f"\n\nID - `{filename}`"
    await Client.send_message(LOG_CHANNEL, text)
    await Client.send_document(
                LOG_CHANNEL,
                filename,
                caption=filename,
            )
    await asyncio.sleep(24*60*60)
    
    with open(FILENAME, "r") as file:
        stored_list = json.load(file)
        
    for item, key in stored_list:
        await app.delete_messages(item, key)

@Client.on_message(filters.command('rmbroadcast', '/'))
async def rmbroadcast(bot:Client, message:Message):
    try:
        filename = message.text.split()[-1]
    except:
        return
    if not filename.endswith(".txt"):
        filename = f"{filename}.txt"
    try:
        with open(filename, "r") as file:
            stored_list = ast.literal_eval(file.read())
    except Exception as e:
        await message.reply_text(f"Error Occured!\n\n{e}")
        return
    for item, key in stored_list:
        await Client.delete_messages(item, key)
    
    await message.reply_text("Done.", quote=True)
    text = f"#RM-BROADCAST"
    text += f"\n\nID - `{filename}`"
    await app.send_message(LOG_CHANNEL, text)
    

@Client.on_message(filters.command('m', '/'))
async def checkuser(bot:Client, message:Message):
    if Users.is_sudo(message.from_user.id) is False:
        return
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        name = message.reply_to_message.from_user.first_name
    else:
        user_id = int(message.text.split()[-1])
        name = f"[User](tg://user?id={user_id})"
    TYPES = ["anime", "hentai", "platinum", "brazzers", "japanese", "onlyfans", "desi"]
    subscriptions = f"User's Name: {name}\nUser's Id: {user_id}\n\n"
    for typ in TYPES:
        check_premium = Users.check_premium(user_id, typ)
        if check_premium is True:
            expire_date = Users.expire_date(user_id, typ)
            if expire_date==None:
                    continue
            subscriptions+=f"**{typ.capitalize()}** : {expire_date}\n"
        else:
            continue
    await message.reply(subscriptions)


@Client.on_message(filters.command('upl', '/'))
async def upload_idk(bot:Client, message:Message):
    if message.from_user.id not in [1135084367, 720518864]:
        return
    msg = message.text.split(" | ")
    
    title = msg[1]
    episodes = msg[2]
    language = msg[3]
    tags = msg[4]
    link = msg[5]
    
    text = UPLOAD_TEXT.format(title, episodes, language, tags)
    photo_id = message.reply_to_message.photo.file_id
    buttons = InlineKeyboardMarkup([[InlineKeyboardButton("Download",  url=link), InlineKeyboardButton("Join Here",  url="https://t.me/NSFW_hub")]])
    
    await Client.send_photo(HENTAI_CHATID, photo=photo_id, caption=text, reply_markup=buttons)
    await message.reply("Done Posted!")
