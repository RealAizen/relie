from Hentai import tsoheru 
from Hentai.database.client import Users 
from telethon import events 

@tsoheru.on(events.NewMessage(incoming=True, pattern="/stats"))     
async def stats(event):
    if Users.is_sudo(event.sender_id) is False:
        return 
    await event.reply(f'**Total Users**: `{Users.total_stats()}`')
    
@tsoheru.on(events.NewMessage(incoming=True, pattern="/pstats"))     
async def premiumstats(event):
    if Users.is_sudo(event.sender_id) is False:
        return 
    await event.reply(f'**Total Premium Users**: `{Users.total_premium()}`')
    
@tsoheru.on(events.NewMessage(incoming=True, pattern="/pusers"))     
async def premiumuserlist(event):    
    if Users.is_sudo(event.sender_id) is False:
        return 
    await event.reply("\n".join(sorted(Users.premiumuser())))
