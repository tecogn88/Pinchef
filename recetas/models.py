from django.db import models
from autoslug import AutoSlugField
from usuarios.models import Usuario
from django.contrib.auth.models import User

# Create your models here.

class Receta(models.Model):
	nombre=models.CharField(max_length=255)
	# slug=AutoSlugField(unique=True, populate_from='nombre', editable=True)
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

class Pedido(models.Model):
	usuario=models.ForeignKey(User, related_name='usuarios')
	fecha=models.DateTimeField(auto_now=True)
	status=models.CharField(max_length=255)
	recetas=models.ManyToManyField(Receta,related_name='recetas')
