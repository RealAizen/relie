from pymongo import MongoClient 
from Hentai import DATABASE_URL, OWNER_ID
from Hentai.utils.premium import Generate 
from telethon import Button
import string, random

def id_generator(size=6, chars= string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

clientdb = MongoClient(DATABASE_URL)
typedb = clientdb['SoheruGroup']
users = typedb['userstwo']
data = typedb['custom']
bannedb = typedb['banned']

def ban(userid):
    if Users.is_sudo(userid) is True:
        return False
    bannedb.insert_one({'user':int(userid)})
    return True 

def unban(userid):
    if Users.is_sudo(userid) is True:
        return False
    bannedb.delete_many({'user':int(userid)})
    return True 

def banned():
    x = []
    y = bannedb.find()  
    for a in y:
        x.append(a['user'])
    return x
        
def increase(animeid):
    PremiumCustom.increment(animeid)
    return

class PremiumCustom:
    def add(animeid, oldlink, custom_link, channel):
        if 't.me' in oldlink: 
            link = oldlink.replace('t.me', 'telegram.me')
        data.insert_one({'serial_id':int(animeid), 'old':oldlink, 'custom':custom_link, "channel": channel})
        return True 
    def increment(animeid):
        x = data.update_one({'serial_id':int(animeid)}, {"$inc":{'count':1}})
    def update(animeid, old, custom):
        if 't.me' in old: 
            old = old.replace('t.me', 'telegram.me')
        x = data.update_one({'serial_id':int(animeid)}, {"$set":{'old':old, 'custom':custom}})
    def remove(animeid):
        data.find_one_and_delete({'serial_id':int(animeid)})
        return True 
    def total_count(animeid):
        x = data.find_one({'serial_id':int(animeid)})
        if x is not None:
            try:
                return x['count']
            except:
                return None
        else:
            return None
    def find(animeid, old=True):
        x = data.find_one({'serial_id':int(animeid)})
        if x is not None:
            increase(animeid)
            if old is True:
                return x['old']
            else:
                return x['custom']
        else:
            return None


class Users:
    def add(userid):
        users.insert_one(
            {'user':int(userid), 
             'is_sudo':False, 
             'platinum': None, 
             'brazzers': None, 
             'onlyfans': None, 
             'japanese':  None, 
             'desi': None, 
             'hentai': None, 
             'anime': None,
             'movies': None,
             'premium':False,
             '3dhentai': None,
             'cosplay': None,
             'stepfamily': None,
             'milfs': None,
             'celebrity': None,
             'sexcam': None}
            )
        return True 
    def is_premium(user_id):
        x = users.find_one({'user':int(user_id)})
        return x['premium']
    def total_stats():
        return users.count_documents({'is_sudo':False})
    def total_special():
        x = users.count_documents({'platinum':None}) 
        y = users.count_documents({'is_sudo':False})
        return int(y)-int(x)
    def total_premium():
        return users.count_documents({'premium':True})
    def premiumuser():
        plist = []
        for user in users.find({'premium': True}):
            user_id = user['user']
            premium_services = [
                ('platinum', 'Platinum'),
                ('movies', 'Movies'),
                ('brazzers', 'Brazzers'),
                ('onlyfans', 'Onlyfans'),
                ('desi', 'Desi'),
                ('japanese', 'Japanese'),
                ('anime', 'Anime'),
                ('hentai', 'Hentai'),
            ]
            user_status = []
            
            for service, label in premium_services:
                expire_date = user.get(service)
                if expire_date:
                    expiring = str(Generate.expirein(expire_date)).split(',', 1)[0].strip()
                    user_status.append(f'{label} {expiring}')
            
            if user_status:
                status_text = ', '.join(user_status)
                textt = f"[{user_id}](tg://user?id={user_id}) - {status_text}"
                plist.append(textt)
        
        return plist

    def all_user():
        x = []
        y = users.find({'is_sudo':False})  
        for a in y:
            x.append(a['user'])
        return x
    def premium(userid, _type, expire):
        print(f"user {userid} channel {_type} expired {expire}")
        users.update_one({'user':int(userid)}, {"$set":{str(_type):str(expire), "premium":True}})
        return True
    def remium(userid, _type):
        users.update_one({'user':int(userid)}, {"$set":{_type:None}})
        return True
    def check_premium(userid, taaipe):
        x = users.find_one({'user':int(userid)})
        if x is not None:
            if x[taaipe] is not None:
                return True
            else:
                if x["platinum"] is not None:
                    return True
                return False
        else:
            return False
    def expire_date(userid, _type):
        x = users.find_one({'user':int(userid)})    
        if x is not None:
            return x[_type]
        else:
            return None      
    def promote(userid):
        print(f"no promote {userid}")
        return True
    def demote(userid):
        users.update_one({'user':int(userid)}, {"$set":{'is_sudo':False}})        
        return True
    def is_sudo(userid):
        if int(userid) in [720518864, 669641125, 5459039279, 1135084367, 6188312425]:
            return True
        else:
            return False
    def is_reg(userid):
        x = users.find_one({'user':int(userid)})    
        if x is None:
            return False
        else:
            return True
                
