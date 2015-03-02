from django.contrib import admin

# Register your models here.

from .models import Usuario
from .models import Direccion

admin.site.register(Usuario)

class DireccionAdmin(admin.ModelAdmin):
	list_display = ('usuario', 'cp')
	search_fields = ('usuario', 'cp')

admin.site.register(Direccion, DireccionAdmin)