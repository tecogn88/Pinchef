from django.shortcuts import render
import conekta
from django.conf import settings

def crear_suscripcion(request):
	conekta.api_key = settings.CONEKTA_PRIVATE_KEY
	if request.method == 'POST':
		customer = conekta.Customer.create({
			 'name':'Fabian Ortiz',
			 'email':'fabian@newemage.com',
			 'phone':'6565629606',
			 'cards':[request.POST['conektaTokenId'],]
		}, settings.CONEKTA_PRIVATE_KEY)
		# Crear suscripcion
		plan = conekta.Plan.find(settings.CONEKTA_PLAN_ID,settings.CONEKTA_PRIVATE_KEY)
		suscripcion = customer.createSubscription({'plan_id':plan.id})
		print suscripcion.status
	return render(request,'crear.html')