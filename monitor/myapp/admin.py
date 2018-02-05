# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from models import open_instances,delay_track

class OpenInstanceAdmin(admin.ModelAdmin):
	list_display =  ( '_adress','_status')
	list_display_links = ('_adress',)


class delaytimeAdmin(admin.ModelAdmin):
	list_display =  ( 'adress','_timing')
	list_display_links = ('adress',)

admin.site.register(open_instances,OpenInstanceAdmin)
admin.site.register(delay_track,delaytimeAdmin)