from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import UserCreationEmailForm, EmailAuthenticationForm, UserCreationDireccionForm, UserContactoForm
from .models import Preferencia
from .models import Direccion
from recetas.models import Pedido
from recetas.models import Receta
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
# Create your views here.

def singup(request):
	form = UserCreationEmailForm(request.POST or None)

	if form.is_valid():
		form.save()

	return render(request, 'singup.html', {'form': form})

def singin(request):
	form = EmailAuthenticationForm(request.POST or None)

	if form.is_valid():
		login(request, form.get_user())

	return render(request, 'singin.html', {'form': form})
	return redirect('/')

def singout(request):
    logout(request)
    return redirect('/')

def access(request):
	form = UserCreationEmailForm(request.POST or None)

	if form.is_valid():
		usuario = form.save()
		res = request.POST.get('res')
		cerdo = request.POST.get('cerdo')
		pollo = request.POST.get('pollo')
		pescado = request.POST.get('pescado')
		mariscos = request.POST.get('mariscos')
		cordero = request.POST.get('cordero')
		alimentacion = request.POST.get('alimentacion')
		restriccion = request.POST.get('restriccion')
		preferencia = Preferencia(res=res, cerdo=cerdo, pollo=pollo, pescado=pescado, mariscos=mariscos, cordero=cordero, alimentacion=alimentacion, restriccion=restriccion, usuario=User.objects.latest('id'))
		preferencia.save()
		# recipes = request.session['pedido']
		# for recipe in recipes:
		# 	receta = Receta.objects.get(id=recipe)
		# 	status = 'Pendiente'
		# 	pedido = Pedido.objects.create(usuario=usuario, status=status, recetas=receta)
		# login(request, form.get_user())
		return HttpResponseRedirect("/direccion/")

	return render(request, 'access.html', {'form': form})

def register(request):
	form = UserCreationEmailForm(request.POST or None)

	if form.is_valid():
		form.save()

	return render(request, 'register.html', {'form': form})

def direccion(request):
	form = UserCreationDireccionForm(request.POST or None)

	if form.is_valid():
		calle = request.POST.get('calle')
		colonia = request.POST.get('colonia')
		municipio = request.POST.get('municipio')
		estado = request.POST.get('estado')
		cp = request.POST.get('cp')
		dia = request.POST.get('dia')
		hora = request.POST.get('hora')
		referencias = request.POST.get('referencias')
		direccion = Direccion(calle=calle, colonia=colonia, municipio=municipio, estado=estado, cp=cp, dia=dia, hora=hora, referencias=referencias, usuario=User.objects.latest('id'))
		direccion.save()
		return HttpResponseRedirect("/pago/")

	return render(request, 'direccion.html', {'form': form})

def pago(request):
	return render(request, 'pago.html')

def contacto(request):
	form = UserContactoForm(request.POST or None)

	if form.is_valid():
		subject, from_email, to = 'Contacto de Pincheff', request.POST.get('email'), 'noe@newemage.com'
		text_content = 'Se ha recinido un email de contacto de Pincheff.'
		html_content = '<p>Estos son los datos del contacto:</p><p><b>Nombre: ' + request.POST.get('nombre') + '</p><p><b>E-mail: ' + request.POST.get('email') + '</p></p><p><b>Estado: ' + request.POST.get('estado') + '</p></p><p><b>Municipio: ' + request.POST.get('municipio') + '</p></p><p><b>Mensaje: ' + request.POST.get('mensaje') + '</p>'
		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		msg.attach_alternative(html_content, "text/html")
		msg.send()
		return render(request, 'contacto.html')

	return render(request, 'contacto.html', {'form': form})