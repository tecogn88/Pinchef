# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Suscripcion(models.Model):

    class Meta:
        verbose_name = u"Suscripción"
        verbose_name_plural = u"Suscripciones"

    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, related_name='suscripciones')
    id_cliente = models.CharField(max_length=25)
    id_suscripcion = models.CharField(max_length=25)
    status = models.CharField(max_length=15)
    activo = models.BooleanField(default=False)

    def __unicode__(self):
        return self.usuario.get_full_name()
    

# class Log(models.Model):
# 	class Meta:
# 		verbose_name = u'Log'
# 		verbose_name_plural = u'Logs'

# 	fecha = models.DateTimeField(auto_now_add=True)
# 	suscripcion = models.ForeignKey(Suscripcion, related_name='logs')
# 	monto = models.FloatField()
# 	status = models.CharField(max_length=25)

class Historial(models.Model):
    class Meta:
        verbose_name='Historial'
        verbose_name_plural='Historial'

    fecha = models.DateTimeField(auto_now_add=True)
    suscripcion = models.ForeignKey(Suscripcion, related_name='movimientos')
    movimiento = models.CharField(max_length=55)

    def __unicode__(self):
        return self.movimiento

class Event(models.Model):
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    fecha = models.DateTimeField(auto_now_add=True)
    id_evento = models.CharField(max_length=25)
    objeto = models.CharField(max_length=25)
    livemode = models.BooleanField(default=True)
    created_at = models.CharField(max_length=25)
    event_type = models.CharField(max_length=25)
    data = models.TextField()

    def __unicode__(self):
        return self.id_evento

