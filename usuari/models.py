# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class usuari(models.Model):
    usuaris = models.OneToOneField(User, on_delete=models.CASCADE)
    correu = models.CharField(max_length=50, blank=False, unique=True)
    imatge_perfil = models.ImageField(upload_to='ImatgesPerfil/avatar', default='/static/Usuari'
                                                                          '/DefaultPerfil.png', blank=True)
    composicions = models.ManyToManyField('compo.infocompos')

    def __str__(self):
        return self.usuaris.username