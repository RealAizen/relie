from time import mktime, strftime
import datetime 
    
class Generate: 
    def expire_date(expirein=30):
        day = datetime.datetime.today() + datetime.timedelta(days=expirein)
        current = datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d'), '%Y-%m-%d')
        expire_date = datetime.datetime.strptime(day.strftime('%Y-%m-%d'), '%Y-%m-%d')
        return current, expire_date
    def from_str(expire_date):
        expire_date = datetime.datetime.strptime(str(expire_date), ('%Y-%m-%d'))
        current = str(datetime.datetime.now()).split(' ', 1)[0]
        current = datetime.datetime.strptime(current, ('%Y-%m-%d'))
        return expire_date, current
    def expirein(expire_date):
        expire_date = datetime.datetime.strptime(str(expire_date), ('%Y-%m-%d'))
        current = str(datetime.datetime.now()).split(' ', 1)[0]
        current = datetime.datetime.strptime(current, ('%Y-%m-%d'))
        result = expire_date - current 
        return result
    def expired(expire_date):
        if expire_date==None:
            return False
        expire_date = datetime.datetime.strptime(str(expire_date), ('%Y-%m-%d'))
        current = str(datetime.datetime.now()).split(' ', 1)[0]
        current = datetime.datetime.strptime(current, ('%Y-%m-%d'))
        if expire_date >= current:
            return True 
        else:
            return False 
        
               
