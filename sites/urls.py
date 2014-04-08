# Imports:
from django.conf.urls import patterns, include, url

urlpatterns = patterns('sites.views',
    # Examples:
    # url(r'^$', 'draoo.views.home', name='home'),
    url(r'^$', 'index', name='index'),
    url(r'^bienvenidos/$', 'bienvenidos', name='bienvenidos'),
    url(r'^servicios/$', 'servicios', name='servicios'),
    url(r'^galeria/$', 'galeria', name='galeria'),
    url(r'^contacto/$', 'contacto', name='contacto'),
)