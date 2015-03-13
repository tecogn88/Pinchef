# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
	nombre=models.CharField(max_length=255)
	apellidos=models.CharField(max_length=255,blank=True)
	username=models.CharField(max_length=100)
	password=models.CharField(max_length=50)
	telefono=models.CharField(max_length=255)
	status=models.IntegerField(max_length=11)
	tipo=models.IntegerField(max_length=11)

	def __unicode__(self):
		return self.nombre

class Direccion(models.Model):
	calle=models.CharField(max_length=255)
	colonia=models.CharField(max_length=255)
	municipio=models.CharField(max_length=255)
	estado=models.CharField(max_length=255)
	cp=models.CharField(max_length=255,verbose_name='Código postal')
	dia=models.CharField(max_length=255)
	hora=models.CharField(max_length=255)
	referencias=models.TextField(blank=True)
	usuario=models.OneToOneField(User)

class Preferencia(models.Model):
	TYPE_CHOICES = (
       ('vegetariano', 'Vegetariano(a)'),
       ('vegano', 'Vegano(a)'),
       ('ninguno', 'Ninguno de los Anteriores'),
    )
	res=models.BooleanField('¿Come Carne de Res?', default=False)
	cerdo=models.BooleanField('¿Come Carne de Cerdo?', default=False)	
	pollo=models.BooleanField('¿Come Pollo/Aves?', default=False)
	pescado=models.BooleanField('¿Come Pescado?', default=False)
	mariscos=models.BooleanField('¿Come Mariscos', default=False)
	cordero=models.BooleanField('¿Come Cordero?', default=False)
	alimentacion=models.CharField(max_length=100, choices=TYPE_CHOICES, default='ninguno')
	restriccion=models.TextField(blank=True)
	usuario=models.OneToOneField(User)
