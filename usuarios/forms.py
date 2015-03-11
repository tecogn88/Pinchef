# -*- encoding: utf-8 -*-
from django import forms

from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from models import Usuario
from models import Preferencia

class UserCreationEmailForm(UserCreationForm):
	email = forms.EmailField()
	TYPE_CHOICES = (
       ('vegetariano', 'Vegetariano(a)'),
       ('vegano', 'Vegano(a)'),
       ('ninguno', 'Ninguno de los Anteriores'),
    )
	res= forms.BooleanField(label='¿Come Carne de Res?')
	cerdo= forms.BooleanField(label='¿Come Carne de Cerdo?')
	pollo= forms.BooleanField(label='¿Come Pollo/Aves?')
	pescado= forms.BooleanField(label='¿Come Pescado?')
	mariscos= forms.BooleanField(label='¿Come Mariscos?')
	cordero= forms.BooleanField(label='¿Come Cordero?')
	alimentacion=forms.ChoiceField(choices=TYPE_CHOICES)
	restriccion=forms.CharField(widget = forms.Textarea)

	class Meta:
		model = Usuario
		fields = ('nombre', 'apellidos', 'email')

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

