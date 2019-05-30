# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from django.shortcuts import render
from compo.models import *

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def quisom(request):
    return render(request, 'quisom.html', {})

def registrat(request):
    return render(request, 'registrat.html', {})

def freestyle(request):
    return render(request, 'freestyle.html', {})


def descobreix(request):
    composicions = infocompos.objects.all()

    return render(request, 'descobreix.html', {'composicions': composicions})