# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('suscripciones.views',
		url(r'^crear-suscripcion/$', 'crear_suscripcion', name='crear'),
		url(r'^notifications/$', 'notifications', name='notifications'),
		url(r'^datos-suscripcion/$', 'datos_suscripcion', name='datos-suscripcion'),
	)