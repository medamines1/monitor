# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.

class open_instances(models.Model):
	_adress = models.CharField(primary_key=True,default='xxx.xxx.xxx.xxx:ffff',max_length=25,null=False)
	_status = models.CharField(default='active',max_length=10,null=False)
	_date = models.DateTimeField(auto_now_add=True)
	#_data = models.CharField(leng)
	def _host(self):
		return self._adress 

class delay_track(models.Model):
	_id = models.IntegerField(primary_key=True)
	adress = models.ForeignKey(open_instances)
	date = models.DateTimeField(auto_now_add=True)
	_timing = models.DecimalField(null=True,max_digits=10,decimal_places=7)
	
	
	def save(self, *args, **kwargs):
		c =delay_track.objects.all().order_by('date')
		if len(c) > settings.MAX_TIMING:
			firsts = len(c)-settings.MAX_TIMING
			for i in range(firsts):
				c[i].delete()
		super(delay_track, self).save(*args, **kwargs)
	def pack(self):
		return float(self._timing)
	

