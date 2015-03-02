from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, Http404

# Create your views here.

class home(TemplateView):
	template_name = 'home.html'

	def get_context_data(self, **kwargs):
		context = super(home, self).get_context_data(**kwargs)
		is_auth = False
		name = None

		if self.request.user.is_authenticated():
			is_auth = True
			name = self.request.user.username

		data = {
			'is_auth': is_auth,
			'nombre': name,
		}

		context.update(data)

		return context

	#return render(request, 'home.html')