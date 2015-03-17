# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Suscripcion(models.Model):

    class Meta:
        verbose_name = u"Suscripción"
        verbose_name_plural = u"Suscripciones"

    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.OneToOneField(User)
    id_cliente = models.CharField(max_length=25)
    id_suscripcion = models.CharField(max_length=25)
    status = models.CharField(max_length=15)
    activo = models.BooleanField(default=False)

    def __str__(self):
        return self.usuario.get_full_name()
    

class Log(models.Model):
	class Meta:
		verbose_name = u'Log'
		verbose_name_plural = u'Logs'

	fecha = models.DateTimeField(auto_now_add=True)
	suscripcion = models.ForeignKey(Suscripcion, related_name='logs')
	monto = models.FloatField()
	status = models.CharField(max_length=25)


