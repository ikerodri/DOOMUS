# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse

from usuari.models import *
from .forms import *

def registrat(request):
    form = formulariregiste(request.POST, request.FILES)
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home'))
    context = {'formulari': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            nom = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            correu = form.cleaned_data.get('correu')
            imatge = form.cleaned_data.get('imatge')
            autentificacio = authenticate(username=nom, password=password)
            login(request, autentificacio)
            usuari.objects.create(usuaris=request.user,correu=correu, imatge_perfil=imatge)
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'registrat.html', context)


@login_required()
def afegircompo(request, compo_id):
    usuario = usuari.objects.get(usuaris=request.user)
    compo = infocompos.objects.get(pk=compo_id)
    usuario.composicions.add(compo)
    return HttpResponseRedirect(reverse('descobreix'))