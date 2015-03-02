from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Receta

# Create your views here.

def receta_view(request, slug):
	receta = get_object_or_404(Receta, slug=slug)
	return render(request, 'receta.html', {'receta': receta})
