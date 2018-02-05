# django instances monitor

![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg) ![django 1.11](https://img.shields.io/badge/django-1.11-yellow.svg)


Django monitor create a control panel that detect automaticaly all the 
new instance and control wether they are still active along with some 
static like time to response 
There is another feature wish send a signal to nginx to tell when an 
instance is down and other one to send msg to the dev using twilio...
# Installing
``` 
  GIT: sudo pip install git+https://github.com/medamines1/monitor/
```
create link to monitor project for fast access :

  ```
  cd your_project

  ln -s path_to/monitor . 
  ```
  

Then append to you're application settings.py file  these lines :

```  
  from monitor.myapp import client

    R_DEBUG= True
     
    if R_DEBUG:
      client.on_start_up()
    
```
if you're just testing you're app and don't won't to run monitor just change R_DEBUG to False

Migrate :
  ```python location/monitor.py migrate```
  
Create a normal superuser 'nothing fancy'

  ```python location/monitor.py createsuperuser```
 
 add x to rcelery and run 
   ```
      chmod u+x rcelery
      chmod u+x run
      ```
Run celery  ==> `./rcelery`
Run monitor ==> ` ./run `

You can alse change the some param : 
- Redis-Server:
  def on_start_up(host='localhost',port=6379,db=0,protcol='http',*arg,**kwargs)
- Celery: 
  uses the default config...

# Requirement
 In order for each instance to declare it's exisitance it must get the 
ip of the monitor using redis server
  *Redis server
  *Celery
# Next
 Enter the ip:port shown in the terminal and connect using the user created above .



# ps :  this app is still under developement
