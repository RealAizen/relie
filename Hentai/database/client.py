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
             'premium':False}
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
        x = users.find({'premium':True})
        plist = []
        plist.clear()
        for i in x:
            id = i['user']
            try:
                platinum_expire_date = i['platinum']
            except:
                continue
            brazzers_expire_date = i['brazzers']
            onlyfans_expire_date = i['onlyfans']
            desi_expire_date = i['desi']
            japanese_expire_date = i['japanese']
            anime_expire_date = i['anime']
            hentai_expire_date = i['hentai']
            movies_expire_date = i['movies']
            
            textt = f"[{id}](tg://user?id={id}) -"
            if not platinum_expire_date==None:
                expiring = str(Generate.expirein(platinum_expire_date)).split(',', 1)[0].strip()
                textt+= (" Platinum " + expiring + ",")
            if not movies_expire_date==None:
                expiring = str(Generate.expirein(movies_expire_date)).split(',', 1)[0].strip()
                textt+= (" Movies " + expiring + ",")
            if not brazzers_expire_date==None:
                expiring = str(Generate.expirein(brazzers_expire_date)).split(',', 1)[0].strip()
                textt+= (" Brazzers " + expiring + ",")
            if not onlyfans_expire_date==None:
                expiring = str(Generate.expirein(onlyfans_expire_date)).split(',', 1)[0].strip()
                textt+= (" Onlyfans " + expiring + ",")
            if not desi_expire_date==None:
                expiring = str(Generate.expirein(desi_expire_date)).split(',', 1)[0].strip()
                textt+= (" Desi " + expiring + ",")
            if not japanese_expire_date==None:
                expiring = str(Generate.expirein(japanese_expire_date)).split(',', 1)[0].strip()
                textt+= (" Japanese " + expiring + ",")
            if not anime_expire_date==None:
                expiring = str(Generate.expirein(anime_expire_date)).split(',', 1)[0].strip()
                textt+= (" Anime " + expiring + ",")
            if not hentai_expire_date==None:
                expiring = str(Generate.expirein(hentai_expire_date)).split(',', 1)[0].strip()
                textt+= (" Hentai " + expiring + ",")
            
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
        users.update_one({'user':int(userid)}, {"$set":{'is_sudo':True}})        
        return True
    def demote(userid):
        users.update_one({'user':int(userid)}, {"$set":{'is_sudo':False}})        
        return True
    def is_sudo(userid):
        x = users.find_one({'user':int(userid)})    
        if x is not None:
            return x['is_sudo']
        else:
            return False
    def is_reg(userid):
        x = users.find_one({'user':int(userid)})    
        if x is None:
            return False
        else:
            return True
                
