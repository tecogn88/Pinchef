# -*- encoding: utf-8 -*-
from django import forms

from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Direccion

class UserCreationEmailForm(UserCreationForm):
	email = forms.EmailField()
	TYPE_CHOICES = (
       ('vegetariano', 'Vegetariano(a)'),
       ('vegano', 'Vegano(a)'),
       ('ninguno', 'Ninguno de los Anteriores'),
    )
	res= forms.BooleanField(label='¿Come Carne de Res?', initial=False)
	cerdo= forms.BooleanField(label='¿Come Carne de Cerdo?', initial=False)
	pollo= forms.BooleanField(label='¿Come Pollo/Aves?', initial=False)
	pescado= forms.BooleanField(label='¿Come Pescado?', initial=False)
	mariscos= forms.BooleanField(label='¿Come Mariscos?', initial=False)
	cordero= forms.BooleanField(label='¿Come Cordero?', initial=False)
	alimentacion=forms.ChoiceField(choices=TYPE_CHOICES)
	restriccion=forms.CharField(widget = forms.Textarea)

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'username')

class EmailAuthenticationForm(forms.Form):
	email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
	password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))

	def __init__(self, *args, **kwargs):
		self.user_cache = None
		super(EmailAuthenticationForm, self).__init__(*args, **kwargs)

	def clean(self):
		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')

		self.user_cache = authenticate(email=email, password=password)

		if self.user_cache is None:
			raise forms.ValidationError('Usuario incorrecto')
		elif not self.user_cache.is_active:
			raise forms.ValidationError('Usuario inactivo')

		return self.cleaned_data

	def get_user(self):
		return self.user_cache

class UserCreationDireccionForm(forms.Form):
	calle= forms.CharField(label='Calle y Número', widget = forms.TextInput)
	colonia= forms.CharField(label='Colonia', widget = forms.TextInput)
	municipio= forms.CharField(label='Delegación/Municipio', widget = forms.TextInput)
	estado= forms.CharField(label='Estado', widget = forms.TextInput)
	cp= forms.CharField(label='Código Postal', widget = forms.TextInput)
	dia= forms.CharField(label='Día', widget = forms.TextInput)
	hora= forms.CharField(label='Hora', widget = forms.TextInput)
	referencias=forms.CharField(widget = forms.Textarea)

class UserContactoForm(forms.Form):
	nombre= forms.CharField(label='', widget = forms.TextInput(attrs={'placeholder': 'Nombre'}))
	email= forms.CharField(label='', widget = forms.TextInput(attrs={'placeholder': 'E-mail'}))
	estado= forms.CharField(label='', widget = forms.TextInput(attrs={'placeholder': 'Estado'}))
	municipio= forms.CharField(label='', widget = forms.TextInput(attrs={'placeholder': 'Municipio'}))
	mensaje=forms.CharField(widget = forms.Textarea(attrs={'placeholder': 'Mensaje'}))
