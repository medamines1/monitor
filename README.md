# django instances monitor
Django monitor create a control panel that detect automaticaly all the 
new instance and control wether they are still active along with some 
static like time to response 
There is another feature wish send a signal to nginx to tell when an 
instance is down and other one to send msg to the dev using twilio...
# Installing
``` 
  GIT: sudo pip install git+https://github.com/medamines1/monitor/
```
Then add to you're application  settings file 
```
    from monitor.myapp import client

    R_DEBUG= True
     
    if R_DEBUG:
      client.on_start_up()
    
```
Create a normal superuser 'nothing fancy'
  monitor.py createsuperuser
You can alse change the some param : 
```
-Redis
  def on_start_up(host='localhost',port=6379,db=0,protcol='http',*arg,**kwargs):
-Celery 
  uses the default config...
```
# Requirement
 In order for each instance to declare it's exisitance it must get the 
ip of the monitor using redis server
  *Redis server
  *Celery
# Next
 Enter the ip:port shown in the terminal and connect using the user created above .



ps : 
this app is still under developement
