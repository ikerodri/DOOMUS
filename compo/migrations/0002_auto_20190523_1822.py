# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-23 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infocompos',
            name='imatge_compo',
            field=models.ImageField(blank=True, default='/static/Compo/DefaultCompo.png', upload_to='ImatgesCompos'),
        ),
    ]