from Hentai import tsoheru , LOG_CHANNEL
from Hentai.database.client import Users 
from Hentai.utils.premium import Generate 
from telethon import events, Button

@tsoheru.on(events.NewMessage(incoming=True, pattern="/premium"))     
async def premiumhandler(event):
    if Users.is_sudo(event.sender_id) is False:
        return 
    id_ = event.message.message.split(' ', 3)[1]
    _type = (event.message.message.split(' ', 3)[2]).lower()
    days = int(event.message.message.split(' ', 3)[3])
    expire_date = Generate.expire_date(int(days))
    Users.premium(id_,_type, str(expire_date[1]).split(' ', 1)[0])
    await event.reply(f'Activated Premium for {_type}')
    text = f'''
Hello **Buddy**,

Thank you for purchasing our premium subscription.

Your premium membership for **{_type.capitalize()}** has been activated for **{days}** days.

Renew your subscription **01** day before expiry to get uninterrupted experience.

You can always check your membership status using the `/profile` command in the bot

Thanks,
Anime Heaven Network    
    '''
    btn = [[Button.url('Help', url='https://t.me/realaizen'), Button.inline('Links', data='query1'), Button.inline('Close', 'disable')]]
    await tsoheru.send_message(int(id_), text, buttons=btn)
    text = f"#PREMIUM #{_type.upper()}"
    text += f"\n\nID - `{id_}`"
    text += f"\n\nDays - `{days}`"
    await tsoheru.send_message(LOG_CHANNEL, text)
    
    
@tsoheru.on(events.NewMessage(incoming=True, pattern="/remium"))     
async def premiumhandler(event):
    if Users.is_sudo(event.sender_id) is False:
        return 
    id = event.message.message.split(' ', 2)[1]
    _type = event.message.message.split(' ', 2)[2]
    Users.remium(id, _type)
    await event.reply(f'Deactivated Premium for {_type}')
    text = f"#REMIUM #{_type.upper()}"
    text += f"\n\nID - `{id}`"
    await tsoheru.send_message(LOG_CHANNEL, text)
    
@tsoheru.on(events.NewMessage(incoming=True, pattern="/profile"))     
async def profile(event):
    if ' ' not in event.message.message:
        sender = await event.get_sender()
        user_id = event.sender_id
        profile_info = f"**Your Name**: `{sender.first_name}`\n**Your ID**: `{user_id}`\n\n"
        TYPES = ["anime", "hentai", "platinum", "brazzers", "japanese", "onlyfans", "desi", "movies", "3dhentai", "cosplay", "stepfamily", "milfs", "celebrity", "sexcam"]
        subs = []
        for typ in TYPES:
            check_premium = Users.check_premium(user_id, typ)
            if check_premium is True:
                expire_date = Users.expire_date(user_id, typ)
                if expire_date==None:
                    continue
                subs.append(typ)
                profile_info+=f"**{typ.capitalize()}** : {expire_date}\n"
            else:
                continue
        if (len(subs))<1:
            profile_info += "\n**Ad Link** : `Enabled`\n"
            profile_info += "**Direct Links** : `Disabled`\n"
            profile_info += "**Requests** : `Disabled`\n"
        if (len(subs))>0:
            profile_info += "\n**Ad Link** : `Disabled`\n"
            profile_info += "**Direct Links** : `Enabled`\n"
            profile_info += "**Requests** : `Enabled`\n"
        if "platinum" in subs:
            profile_info += "**On-Demand Movies/Anime/Series** : `Enabled`\n"
        await event.reply(profile_info)
    else:
        await event.reply("Use /m instead, if you're a Sudo User")