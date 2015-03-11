from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import UserCreationEmailForm, EmailAuthenticationForm
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
		form.save()

	return render(request, 'access.html', {'form': form})

def register(request):
	form = UserCreationEmailForm(request.POST or None)

	if form.is_valid():
		form.save()

	return render(request, 'register.html', {'form': form})

def direccion(request):
	return render(request, 'direccion.html')

def pago(request):
	return render(request, 'pago.html')