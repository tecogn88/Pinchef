from django.contrib import admin
from .models import Suscripcion, Log

class SuscripcionAdmin(admin.ModelAdmin):
	list_display = ('id_cliente','id_suscripcion','__str__','status','activo','fecha')

admin.site.register(Suscripcion, SuscripcionAdmin)
admin.site.register(Log)
