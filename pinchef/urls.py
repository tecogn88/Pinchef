from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from .views import home
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pinchef.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', home.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^como-funciona/', TemplateView.as_view(template_name="como-funciona.html")),
    url(r'^zonas-entrega/', TemplateView.as_view(template_name="zonas-entrega.html")),
    url(r'^metodos-pago/', TemplateView.as_view(template_name="metodos-pago.html")),
    url(r'^terminos/', TemplateView.as_view(template_name="terminos.html")),
    url(r'^aviso-privacidad/', TemplateView.as_view(template_name="aviso-privacidad.html")),
    url(r'^contacto/', 'usuarios.views.contacto', name='contacto'),
    url(r'^preguntas/', TemplateView.as_view(template_name="preguntas.html")),
    url(r'^receta/(?P<slug>\w+)/', 'recetas.views.receta_view', name='receta_view'),
    url(r'^recetas/', 'recetas.views.recetas', name='recetas'),
    url(r'^pedir/', 'recetas.views.pedir', name='pedir'),
    url(r'^remover/', 'recetas.views.remover', name='remover'),
    url(r'^singup/', 'usuarios.views.singup', name='singup'),
    url(r'^singin/', 'usuarios.views.singin', name='singin'),
    url(r'^singout/', 'usuarios.views.singout', name='singout'),
    url(r'^access/', 'usuarios.views.access', name='access'),
    url(r'^register/', 'usuarios.views.register', name='register'),
    url(r'^direccion/', 'usuarios.views.direccion', name='direccion'),
    url(r'^pago/', 'usuarios.views.pago', name='pago'),
    url(r'^suscripciones/', include('suscripciones.urls', namespace='suscripciones', app_name='suscripciones')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)