# -*- encoding: utf-8 -*-
from django.db import models

# Create your models here.

class Usuario(models.Model):
	nombre=models.CharField(max_length=255)
	apellidos=models.CharField(max_length=255,blank=True)
	email=models.CharField(max_length=255)
	telefono=models.CharField(max_length=255)
	status=models.IntegerField(max_length=11)
	tipo=models.IntegerField(max_length=11)

	def __unicode__(self):
		return self.nombre

class Direccion(models.Model):
	calle=models.CharField(max_length=255)
	numero=models.CharField(max_length=255)
	colonia=models.CharField(max_length=255)
	ciudad=models.CharField(max_length=255)
	estado=models.CharField(max_length=255)
	cp=models.CharField(max_length=255,verbose_name='Código postal')
	usuario=models.ForeignKey(Usuario)