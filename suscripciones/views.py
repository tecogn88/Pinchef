from django.shortcuts import render, get_object_or_404
import conekta
from django.conf import settings
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Suscripcion
conekta.api_key = settings.CONEKTA_PRIVATE_KEY



@login_required(login_url='/singin/')
def crear_suscripcion(request):
	if request.method == 'POST':
		customer = conekta.Customer.create({
			 'name':request.user.get_full_name(),
			 'email':request.user.email,
			 'cards':[request.POST['conektaTokenId'],]
		}, settings.CONEKTA_PRIVATE_KEY)
		# Crear suscripcion
		plan = conekta.Plan.find(settings.CONEKTA_PLAN_ID,settings.CONEKTA_PRIVATE_KEY)
		suscripcion = customer.createSubscription({'plan_id':plan.id})
		# Validacion para ver el status en el que guardaremos al suscriptor
		suscripcion_bk = Suscripcion(
							usuario=request.user,
							id_cliente=customer.id,
							id_suscripcion=suscripcion.id,
							status=suscripcion.status,
							activo=True
						)
		suscripcion_bk.save()
		print suscripcion.status
	return render(request,'crear.html')

@login_required(login_url='/singin/')
def datos_suscripcion(request):
	suscripcion = get_object_or_404(Suscripcion, usuario=request.user)
	customer = conekta.Customer.find(suscripcion.id_cliente)
	subscription = customer.subscription
	return render(request,'datos-suscripcion.html',{'suscripcion_conekta':subscription,'suscripcion':suscripcion})


@login_required(login_url='/singin/')
def cancelar_suscripcion(request):
	pass

@login_required(login_url='/singin/')
def pausar_suscripcion(request):
	pass

@login_required(login_url='/singin/')
def reanudar_suscripcion(request):
	pass


@csrf_exempt
def notifications(request):
	event_json = json.loads(request.body)
	print event_json
	return HttpResponse(json.dumps({'status':'200'}), content_type="application/json")