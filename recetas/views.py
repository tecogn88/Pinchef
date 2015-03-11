from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Receta

# Create your views here.

def receta_view(request, slug):
	receta = get_object_or_404(Receta, slug=slug)
	return render(request, 'receta.html', {'receta': receta})

def recetas(request):
	recetas = Receta.objects.all()
	pedido = request.session.get('pedido', {})
	if pedido:
		pedido = pedido
	else: 
		pedido = False

	return render(request, 'recetas.html', {'recetas': recetas, 'pedido': pedido})

def pedir(request):
	if request.method == 'POST':
		pedido = request.session.get('pedido', {})
		item = int(request.POST.get('id'))
		p = list(pedido)
		# if item in p:
		# 	return HttpResponse('0')
		# else:
		p.append(item)
		request.session['pedido'] = p
		return HttpResponse('1')

def remover(request):
	if request.method == 'POST':
		item = int(request.POST.get('id'))
		p = request.session['pedido']
		if item in p:
			p.remove(item)
			request.session['pedido'] = p
			return HttpResponse('1')
		else:
			return HttpResponse('0')



