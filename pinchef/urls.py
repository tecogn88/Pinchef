from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from .views import home
from django.conf.urls.static import static


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pinchef.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', home.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^receta/(?P<slug>\w+)/', 'recetas.views.receta_view', name='receta_view'),
    url(r'^singup/', 'usuarios.views.singup', name='singup'),
    url(r'^singin/', 'usuarios.views.singin', name='singin'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)