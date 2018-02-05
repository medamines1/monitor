# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import redirect as re
from myapp.models import open_instances as o
from myapp.models import delay_track as d

from django.shortcuts import render
import json 

# Create your views here.
def _redirect(request):
	return re('/admin/')
def _register(request):
	try:
		d= request.POST['client_host']#create controle -_-
		new = o(_adress=d,_status='active')
		print new._status
		new.save()
		return HttpResponse("done")		
	except:
		return HttpResponse('missing POST')


def  _getservers(request):
	servers = o.objects.all()
	servers_data = {}
	for i in servers:
		data = []
		for k in d.objects.filter(adress=i):
			data.append(k.pack())
		servers_data[i._adress]=[i._status,data]
	return HttpResponse(json.dumps(servers_data),content_type="application/json")


