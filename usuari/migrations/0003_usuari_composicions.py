# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-28 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compo', '0006_auto_20190527_1601'),
        ('usuari', '0002_auto_20190523_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuari',
            name='composicions',
            field=models.ManyToManyField(to='compo.infocompos'),
        ),
    ]
