import redis
import sys,time,urllib,os
from django.conf import settings 

class RedisError(Exception):
    def __init__(self, message, *args):
        self.message = message 
        super(RedisError, self).__init__(message, *args) 




def setHost(argv):#imporove this 
    host="127.0.0.1:8000"
    for k,i in enumerate(argv):
        if i =="runserver":
            try:
                n=argv[k+1]
                if ":" in n:
                    host=n;
                    break
            except:
                break
    return host



def on_start_up(host='localhost',port=6379,db=0,protcol='http',*arg,**kwargs):
    os.system('clear')
    if  settings.R_DEBUG:
        d = setHost(sys.argv)
        r = redis.Redis(host, port, db)
        while True:
            try:
                c = r.get('_server_host')
                if c :
                    h=c
                    r=urllib.urlopen(protcol+'://'+h+'/re',data=urllib.urlencode({'client_host':d}))

                break
            except Exception as e:
                pass
            os.system('clear')
            print "[error]  ",e
            print "trying to re connect to monitor at %s ..."%(h)
            time.sleep(3)
