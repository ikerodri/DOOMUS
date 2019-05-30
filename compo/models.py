# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class infocompos (models.Model):
    GENERE = (
        ('Pop', 'Pop'),
        ('Rock', 'Rock'),
        ('Trap', 'Trap'),
        ('Reggaeton', 'Reggaeton'),
        ('EDM', 'EDM'),
        ('Clasica', 'Clasica'),
        ('Indie', 'Indie'),
    )
    INSTRUMENT = (
        ('Piano', 'Piano'),
        ('Guitarra', 'Guitarra'),
        ('Baix', 'Baix'),
        ('Bateria', 'Bateria'),
        ('Sintetitzador', 'Sintetitzador'),
        ('Strings', 'Strings'),
    )
    TONALITAT = (
        ('C Maj', 'C Maj'),
        ('C min', 'C min'),
        ('C# Maj', 'C# Maj'),
        ('C# min', 'C# min'),
        ('D Maj', 'D Maj'),
        ('D min', 'D min'),
        ('D# Maj', 'D# Maj'),
        ('D# min', 'D# min'),
        ('E Maj', 'E Maj'),
        ('E min', 'E min'),
        ('F Maj', 'F Maj'),
        ('F min', 'F min'),
        ('F# Maj', 'F# Maj'),
        ('F# min', 'F# min'),
        ('G Maj', 'G Maj'),
        ('G min', 'G min'),
        ('G# Maj', 'G# Maj'),
        ('G# min', 'G# min'),
        ('A Maj', 'A Maj'),
        ('A min', 'A min'),
        ('A# Maj', 'A# Maj'),
        ('A# min', 'A# min'),
        ('B Maj', 'B Maj'),
        ('B min', 'B min'),
    )
    titol = models.CharField(max_length=100, null=False, default="Compo")
    instrument = models.CharField(max_length=50, choices=INSTRUMENT, blank=False)
    genere = models.CharField(max_length=50, choices=GENERE, blank=False)
    bpms = models.IntegerField(blank=False)
    tonalitat = models.CharField(max_length=50,choices=TONALITAT, blank=False)
    definicio = models.CharField(max_length=300, blank=True)
    arxiu = models.FileField(upload_to='Compos', default='/static/Compo/DefaultFile.mp3', blank=True)
    imatge_compo = models.ImageField(upload_to='ImatgesCompos', default='../static/Compo'
                                                                          '/DefaultCompo.png', blank=True)
    autor = models.ForeignKey('usuari.usuari', on_delete=models.CASCADE)
    def __str__(self):
        return self.instrument