# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('suscripciones.views',
		url(r'^crear-suscripcion/$', 'crear_suscripcion', name='crear'),
	)