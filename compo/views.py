# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from compo.models import infocompos
from usuari.models import usuari
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *
from usuari.forms import *

# Create your views here.


@login_required()
def novacompo(request):
    usuario = usuari.objects.get(usuaris=request.user)
    form2 = creaciocompo(request.POST, request.FILES)
    context = {'form': form2}
    if request.method == "POST":
        if form2.is_valid():
            titol = form2.cleaned_data.get('titol')
            instrument = form2.cleaned_data.get('instrument')
            genere = form2.cleaned_data.get('genere')
            bpms = form2.cleaned_data.get('bpms')
            tonalitat = form2.cleaned_data.get('tonalitat')
            definicio = form2.cleaned_data.get('definicio')
            arxiu = form2.cleaned_data.get('arxiu')
            imatge_compo = form2.cleaned_data.get('imatge_compo')
            infocompos.objects.create(autor=usuario, titol=titol, instrument=instrument, genere=genere, bpms=bpms, tonalitat=tonalitat, definicio=definicio, arxiu=arxiu, imatge_compo=imatge_compo)
            return HttpResponseRedirect(reverse('home'))
    return render(request, "Penja.html", context)