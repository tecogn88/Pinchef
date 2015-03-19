# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Suscripcion, Event, Historial

class SuscripcionAdmin(admin.ModelAdmin):
	list_display = ('__str__','id_cliente','id_suscripcion','__str__','status','activo','fecha')

admin.site.register(Suscripcion, SuscripcionAdmin)
admin.site.register(Event)
admin.site.register(Historial)
