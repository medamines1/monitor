import redis
from myapp.models import open_instances as o
from myapp.models import delay_track as t

import uuid,time,requests
from django.conf import settings #change loc to header on production
from twilio.rest import Client


def send_msg(host):

	account = settings.TWILIO_ACCOUNT
	token =  settings.TWILIO_TOEKN
	client = Client(account, token)

	message = client.messages.create(to=settings.TO, from_=settings.FROM,
                                 body="[Urgent] the instance at %s has stoped ... "%(host))


def setHost(argv):#imporove this before deploy
    host="127.0.0.1:8000"
    for k,i in enumerate(argv):
        if i == "runserver":
            try:
                n=argv[k+1]
                print n
                if ":" in n:
                    host=n;
                    break
            except:
                break
    return host



def update_db():
	for i in o.objects.all():

		host = i._adress
		try:
			resp=requests.get('http://'+host)
			i._status='active'
			try:
				new= t(adress=i,_timing=resp.elapsed.total_seconds()) 
				new.save()
			except Exception as e:
				if i._status == 'active':
					continue
				i.save()


		except Exception as e:		
			if i._status == 'close':
				continue
			i._status='close'
			i.save()
			try:
				send_msg(host)
			except:
				pass
			print "alert server with id %s stopped  . . . because %s"%(i._adress,e)


def _run_server(m_host='',host='localhost',port=6379,db=0,*arg,**kwargs):
	signed= []
	r = redis.Redis(host, port, db)
	r.set('_server_host',m_host)
	while True:
		print settings.REQUEST_TIME_OUT
		time.sleep(settings.REQUEST_TIME_OUT)
		update_db()



