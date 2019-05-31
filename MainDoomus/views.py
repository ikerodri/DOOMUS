# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from usuari.models import *
from usuari.forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render
from compo.models import *

# Create your views here.
def redirecthome(request):
    return HttpResponseRedirect(reverse('home'))

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



@login_required()
def composdusuari(request):
    usuario = usuari.objects.get(usuaris=request.user)
    composicions = usuario.composicions.all()
    print composicions
    return render(request, "freestyle.html", {"usaurio": usuario, "composicions": composicions})