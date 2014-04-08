#encoding:utf-8

# Defaults Imports.
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.template import Context
from datetime import datetime
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.db.models import Q

# My Imports.
from .models import *
from .forms import *



# Create your views here.
########################## Views website.
def index(request):
    template = 'sites/index.html'
    return render_to_response(template, context_instance=RequestContext(request))

# Create your views here.
########################## Views website.
def bienvenidos(request):
    template = 'sites/bienvenidos.html'
    return render_to_response(template, context_instance=RequestContext(request))

# Create your views here.
########################## Views website.
def servicios(request):
    template = 'sites/servicios.html'
    return render_to_response(template, context_instance=RequestContext(request))

# Create your views here.
########################## Views website.
def galeria(request):
    template = 'sites/galeria.html'
    return render_to_response(template, context_instance=RequestContext(request))

# Create your views here.
########################## Views website.
def contacto(request):
    now = datetime.now()
    if request.method=='POST':
        contactoform = ContactoForm(request.POST)
        if contactoform.is_valid():
            titulo = 'Mensaje'
            contenido = contactoform.cleaned_data['mensaje'] + '\n'
            contenido += 'Comunicarse a: ' + contactoform.cleaned_data['correo']
            correo = EmailMessage(titulo, contenido, to=['skatowalker@gmail.com'])
            correo.send()
            return HttpResponseRedirect('/')
    else:
        contactoform = ContactoForm()
    ctx = {'contactoform':contactoform, 'hora':now}
    template = 'sites/contacto.html'
    return render_to_response(template, ctx, context_instance=RequestContext(request))