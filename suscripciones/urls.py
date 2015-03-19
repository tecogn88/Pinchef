# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('suscripciones.views',
		url(r'^crear-suscripcion/$', 'crear_suscripcion', name='crear'),
		url(r'^notifications/$', 'notifications', name='notifications'),
		url(r'^datos-suscripcion/$', 'datos_suscripcion', name='datos-suscripcion'),
		url(r'^login/$', 'login', name='login'),
		url(r'^suspender/$', 'pausar_suscripcion', name='suspender'),
		url(r'^reanudar/$', 'reanudar_suscripcion', name='reanudar'),
		url(r'^cancelar/$', 'cancelar_suscripcion', name='cancelar'),
	)