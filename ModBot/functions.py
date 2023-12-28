from supabase import create_client, Client
import random
import config as c
supabase: Client = create_client(c.surl, c.skey)

class functions:
    def delwarn(warnid):            
        data = supabase.table('warns').delete().eq('warnid', warnid).execute()
        print(data)
        if data.data:
            print()

    def getWarnings(userid):            
        data = supabase.table('warns').select('userid, reason, by, warnid').eq('userid', userid).execute()
        if data.data:
            return data.data
                
        else:
            return "No Warns"
    def GiveWarns(userid, reason, by):
        warnid = random.randint(10000000000000,999999999999999)
        x = supabase.table('warns').insert({"userid": userid, "reason": reason, "by": by,"warnid": warnid}).execute()
