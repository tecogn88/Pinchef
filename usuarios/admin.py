from django.contrib import admin

# Register your models here.

from .models import Usuario
from .models import Direccion
from .models import Membresia
from .models import Preferencia

class UsuarioAdmin(admin.ModelAdmin):
	list_display = ('pk', 'nombre', 'status')

admin.site.register(Usuario, UsuarioAdmin)

class DireccionAdmin(admin.ModelAdmin):
	list_display = ('usuario', 'cp')
	search_fields = ('usuario', 'cp')

admin.site.register(Direccion, DireccionAdmin)

class PreferenciaAdmin(admin.ModelAdmin):
	list_display = ('usuario','res', 'cerdo', 'pollo', 'pescado', 'mariscos', 'cordero', 'alimentacion', 'restriccion')
	search_fields = ('usuario',)

admin.site.register(Preferencia, PreferenciaAdmin)