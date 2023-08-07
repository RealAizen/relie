import string, random 
from telethon import events, Button 
from Hentai import tsoheru, BOT_USERNAME, LOG_CHANNEL
from Hentai.database.client import Users, PremiumCustom


def id_generator(size=9, chars= string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@tsoheru.on(events.NewMessage(incoming=True, pattern="/ul"))     
async def updatelink(event): 
    if Users.is_sudo(event.sender_id) is False:
        return 
    text = event.message.message.split()
    id = text[1]
    old = text[2]
    custom = text[3]
    PremiumCustom.update(id, old, custom)    
    await event.reply('Updated New Link', buttons=[[Button.url('New Link', url=old)]])
    text = f"#UPDATE-LINK"
    text += f"\n\nID - `{id}`"
    text += f"\nOldlink - `{old}`"
    text += f"\nNewlink - `{custom}`"
    await tsoheru.send_message(LOG_CHANNEL, text)

@tsoheru.on(events.NewMessage(incoming=True, pattern="/custom"))     
async def link_custom(event): 
    if Users.is_sudo(event.sender_id) is False:
        return
    link_types = ["anime", "hentai", "brazzers", "japanese", "onlyfans", "desi", "movies", "3dhentai", "cosplay", "stepfamily", "milfs", "celebrity", "animemovies", "mms"]
    try:
        msg = event.message.message.split(' ', 3)
        channel = msg[1].strip().lower()
        old = msg[2].strip()
        custom = msg[3].strip()
        id_gen = id_generator()
        if channel not in link_types:
            raise Exception
    except:
        await event.reply(f"Format: /custom <linktype> <oldlink> <shortenerlink>\n\nLinkType: {','.join((x.capitalize()+' ') for x in link_types)}")
        return
    PremiumCustom.add(id_gen, old, custom, channel)
    text = f'[Custom Link](https://t.me/{BOT_USERNAME}?start=custom_{channel}{id_gen})\n'
    await event.reply(f'[Custom Link](https://t.me/{BOT_USERNAME}?start=custom_{channel}_{id_gen})', buttons=[[Button.url('Custom Link', url=f'https://t.me/{BOT_USERNAME}?start=custom_{channel}_{id_gen}')]])
    text = f"#NEW-LINK #{channel.upper()}"
    text += f"\n\nID - `{id_gen}`"
    text += f"\nOldlink - `{old}`"
    text += f"\nNewlink - `{custom}`"
    await tsoheru.send_message(LOG_CHANNEL, text)