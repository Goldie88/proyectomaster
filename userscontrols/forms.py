# Imports.
# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from .models import *


class ContactoForm(forms.Form):
	correo = forms.EmailField(label='Contactanos, estamos para servirte.')
	mensaje = forms.CharField(widget=forms.Textarea)

