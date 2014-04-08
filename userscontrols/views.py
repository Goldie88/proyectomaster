# -*- coding: utf-8 -*-

#  Defaults Imports
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from datetime import datetime
# // GESTOR DE USUARIOS
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as loginuser, authenticate, logout
from django.contrib.auth.decorators import login_required
# My import
from .models import *
from .forms import *

# Create your views here.
########################## Views website.
@login_required(login_url='login/')
def home(request):
    usuario = request.user
    now = datetime.now()
    ctx = {"usuario":usuario,"fecha":now}
    template = 'userscontrols/home.html'
    return render_to_response(template, ctx, context_instance=RequestContext(request))

@login_required(login_url='login/')
def newuser(request):
    newuserform = UserCreationForm
    if request.method == 'POST':
        newuserform = UserCreationForm(request.POST)
        if newuserform.is_valid():
            newuserform.save()
            return HttpResponseRedirect('/')

    else:
        newuserform = UserCreationForm()

    ctx = {'newuserform':newuserform}
    template = 'userscontrols/newuser.html'
    return render_to_response(template, ctx, context_instance=RequestContext(request))

########################## LOGIN.
def login(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/userscontrols')
    if request.method == 'POST':
        loginform = AuthenticationForm(request.POST)
        if loginform.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            access = authenticate(username=usuario, password=clave)
            if access is not None:
                if access.is_active:
                    loginuser(request, access)
                    return HttpResponseRedirect('/userscontrols')
                else:
                    return render_to_response('userscontrols/noactive.html', context_instance=RequestContext(request))
            else:
                return render_to_response('userscontrols/nouser.html', context_instance=RequestContext(request))
    else:
        loginform = AuthenticationForm()
        ctx = {'loginform':loginform}
    return render_to_response('userscontrols/login.html', ctx, context_instance=RequestContext(request))

########################## LOGOUT.
@login_required(login_url='login/')
def logout(request):
    logout(request)
    return render_to_response('/') 