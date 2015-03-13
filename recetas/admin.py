from django.contrib import admin

# Register your models here.

from .models import Receta
from .models import Pedido

class RecetaAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','preview','calorias')
	search_fields = ('nombre','calorias')
	list_filter = ('calorias','nombre','id')
	list_editable = ('nombre','calorias')

admin.site.register(Receta, RecetaAdmin)

class PedidoAdmin(admin.ModelAdmin):
	list_display = ('pk', 'fecha', 'status', 'usuario')
	search_fields = ('usuario', 'status', 'fecha')
	list_filter= ('usuario', 'status', 'fecha')

admin.site.register(Pedido, PedidoAdmin)
