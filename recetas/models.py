from django.db import models
from autoslug import AutoSlugField

# Create your models here.

class Receta(models.Model):
	nombre=models.CharField(max_length=255)
	slug=AutoSlugField(unique=True, populate_from='nombre', editable=True)
	descripcion=models.TextField(blank=False)
	imagen=models.ImageField(upload_to='recetas')
	calorias=models.CharField(max_length=255)

	def preview(self):
		return """
		<img src="%s" width="100px" />
		""" % self.imagen.url

	preview.allow_tags = True
	preview.admin_order_field = 'imagen'

	def __unicode__(self):
		return self.nombre

class Ingrediente(models.Model):
	nombre=models.CharField(max_length=255)
	cantidad=models.CharField(max_length=255)
	receta=models.ForeignKey(Receta,related_name='ingredientes')

	def __unicode__(self):
		return self.nombre

class Pedido(models.Model):
	fecha=models.DateTimeField(auto_now=True)
	status=models.IntegerField(max_length=11)
