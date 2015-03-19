# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
import conekta
from django.conf import settings
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Suscripcion, Event, Historial
from django.core.urlresolvers import reverse
conekta.api_key = settings.CONEKTA_PRIVATE_KEY

from django.contrib.auth import login as auth_login, authenticate
def login(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user:
			auth_login(request, user)
			next = request.GET.get('next', False)
			if next:
				return redirect(next)
			else:
				return redirect('/')
	return render(request,'login-suscriptions.html')


@login_required(login_url='/singin/')
def crear_suscripcion(request):
	# Vemos si ya tiene una suscripcion
	suscripciones = Suscripcion.objects.filter(usuario=request.user).exclude(status='canceled')
	if suscripciones.count() > 0:
		# Lo redirijimos a datos de la suscriocion
		return redirect(reverse('suscripciones:datos-suscripcion'))
	if request.method == 'POST':
		customer = conekta.Customer.create({
			 'name':request.user.get_full_name(),
			 'email':request.user.email,
			 'cards':[request.POST['conektaTokenId'],]
		}, settings.CONEKTA_PRIVATE_KEY)
		# Crear suscripcion
		plan = conekta.Plan.find(settings.CONEKTA_PLAN_ID,settings.CONEKTA_PRIVATE_KEY)
		suscripcion = customer.createSubscription({'plan_id':plan.id})
		if suscripcion.status == 'active':
			activo = True
		else:
			activo = False
		# Validacion para ver el status en el que guardaremos al suscriptor
		suscripcion_bk = Suscripcion(
							usuario=request.user,
							id_cliente=customer.id,
							id_suscripcion=suscripcion.id,
							status=suscripcion.status,
							activo=activo
						)
		suscripcion_bk.save()
		return redirect(reverse('suscripciones:datos-suscripcion'))
	return render(request,'crear.html')

@login_required(login_url='/singin/')
def datos_suscripcion(request):
	suscripciones = Suscripcion.objects.filter(usuario=request.user)
	if suscripciones.count() > 0:
		suscripcion = suscripciones.last()
		customer = conekta.Customer.find(suscripcion.id_cliente)
		subscription = customer.subscription
		return render(request,'datos-suscripcion.html',{'suscripcion_conekta':subscription,'suscripcion':suscripcion})
	else:
		return redirect(reverse('suscripciones:crear'))


@login_required(login_url='/singin/')
def cancelar_suscripcion(request):
	suscripciones = Suscripcion.objects.filter(usuario = request.user)
	if suscripciones.count() > 0:
		suscripcion = suscripciones.last()
		customer = conekta.Customer.find(suscripcion.id_cliente)
		suscripcion_conekta = customer.subscription
		suscripcion_conekta.cancel()
		if suscripcion_conekta.status == 'canceled':
			exito = True
			mensaje = u'Se realizó la cancelación correctamente'
	else:
		suscripcion = False
		exito = False
		mensaje = u'No se pudo realizar la cancelación, por favor contacta al administrador'
	return HttpResponse(json.dumps({'exito':exito,'mensaje':mensaje}), content_type="application/json")

@login_required(login_url='/singin/')
def pausar_suscripcion(request):
	suscripciones = Suscripcion.objects.filter(usuario = request.user)
	if suscripciones.count() > 0:
		suscripcion = suscripciones.last()
		customer = conekta.Customer.find(suscripcion.id_cliente)
		suscripcion_conekta = customer.subscription
		suscripcion_conekta.pause()
		if suscripcion_conekta.status == 'paused':
			exito = True
			mensaje = u'La suscripción se pauso correctamente'
		elif suscripcion_conekta.status == 'canceled':
			exito = False
			mensaje = u'La suscripción no se pudo pausar ya que actualmente esta cancelada, por favor contacta al administrador'
	else:
		exito = False
		mensaje = u'No se pudo realizar esta operación, por favor contacta al administrador'
	return HttpResponse(json.dumps({'exito':exito,'mensaje':mensaje}), content_type="application/json")


@login_required(login_url='/singin/')
def reanudar_suscripcion(request):
	suscripciones = Suscripcion.objects.filter(usuario = request.user)
	if suscripciones.count() > 0:
		suscripcion = suscripciones.last()
		customer = conekta.Customer.find(suscripcion.id_cliente)
		suscripcion_conekta = customer.subscription
		suscripcion_conekta.resume()
		if suscripcion_conekta.status == 'active':
			exito = True
			mensaje = u'Se reanudó la suscripción con éxito'
		elif suscripcion_conekta.status == 'canceled':
			exito = False
			mensaje = u'La suscripción no se pudo reanudar ya que actualmente esta cancelada, por favor contacta al administrador'
	else:
		exito = False
		mensaje = u'No se pudo realizar esta operación por favor contacte al administrador'
	return HttpResponse(json.dumps({'exito':exito,'mensaje':mensaje}), content_type="application/json")		


@csrf_exempt
def notifications(request):
	event_json = json.loads(request.body)
	# Creacion del evento
	event = Event()
	event.id_evento = event_json['id']
	event.objeto = event_json['object']
	event.livemode = event_json['livemode']
	event.created_at = event_json['created_at']
	event.event_type = event_json['type']
	event.data = event_json['data']
	event.save()
	# Creamos el historial
	if event_json['data']['object']['object'] == 'subscription':
		id_subscription = event_json['data']['object']['id']
		suscripcion = Suscripcion.objects.get(id_suscripcion=id_subscription)
		# Actualizar status y active de suscripcion dependdiendo del estatus en el evento
		if event.event_type != 'subscription.created':
			suscripcion.status = event_json['data']['object']['status']
			if suscripcion.status == 'active':
				suscripcion.activo = True
			else:
				suscripcion.activo = False
		# Guardamos la actualización de la suscripción
		suscripcion.save()
		# Creamos el historial de la suscripción
		historial = Historial()
		historial.suscripcion = suscripcion
		if event.event_type == 'subscription.paid':
			historial.movimiento = u'Pago de suscripción'
		elif event.event_type == 'subscription.created':
			historial.movimiento = u'Creación de suscripción'
		elif event.event_type == 'subscription.paused':
			historial.movimiento = u'Se pausó la suscripción'
		elif event.event_type == 'subscription.resumed':
			historial.movimiento = u'Reanudación de suscripción'
		elif event.event_type == 'subscription.canceled':
			historial.movimiento = u'Cancelación de suscripción'
		elif event.event_type == 'subscription.updated':
			historial.movimiento = u'Actualización de suscripción'
		elif event.event_type == 'subscription.payment_failed':
			historial.movimiento = u'No se pudo procesar el pago de la suscripción'
		else:
			historial.movimiento = event.event_type
		historial.save()

	return HttpResponse(json.dumps({'status':'200'}), content_type="application/json")