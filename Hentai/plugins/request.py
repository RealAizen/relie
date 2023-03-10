from Hentai import tsoheru 
from telethon import events, Button 
from Hentai.database.client import Users, PremiumCustom

PREM_REQ_CHANNEL_LINK = "https://t.me/+FOT4iNA4Xwk3NGNl"
DEVS_GROUP = -1001685611156

@tsoheru.on(events.NewMessage(incoming=True, pattern="/request"))     
async def updatelink(event): 
    if Users.is_premium(event.sender_id) is False:
        return
    if ' ' not in event.message.message:
        await event.reply(f"Format: /request <channel> <your request>\n\nJoin for More - {PREM_REQ_CHANNEL_LINK}")
        return
    try:
        channel = event.message.message.split(" ", 2)[1]
        request = event.message.message.split(" ", 2)[2]
        sender = await event.get_sender()
        user_id = event.sender_id
    except:
        await event.reply(f"Format: /request <channel> <your request>\n\nJoin for More - {PREM_REQ_CHANNEL_LINK}")
        return
    msg = f"#REQUEST #{channel.upper()}\n"
    msg += f"[{sender.first_name}](tg://user?id={user_id}) (`{user_id}`)\n\n"
    msg += f"`{request}`"
    await tsoheru.send_message(DEVS_GROUP, msg)
    await event.reply('Request Sent Successfully.', buttons=[[Button.url('Join Here', url=PREM_REQ_CHANNEL_LINK)]])
   