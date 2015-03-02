from django.contrib import admin

# Register your models here.

from .models import Receta
from .models import Ingrediente

class IngredienteInline(admin.StackedInline):
	model = Ingrediente
	extra = 1

class RecetaAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','preview','calorias')
	search_fields = ('nombre','calorias')
	list_filter = ('calorias','nombre','id')
	list_editable = ('nombre','calorias')
	inlines = [IngredienteInline, ] 

admin.site.register(Receta, RecetaAdmin)


# class IngredienteAdmin(admin.ModelAdmin):
# 	list_display = ('pk','nombre', 'receta')
# 	search_fields = ('nombre', 'receta')
# 	list_editable = ('receta','nombre')

# admin.site.register(Ingrediente, IngredienteAdmin)