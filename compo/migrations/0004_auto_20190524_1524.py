# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-24 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compo', '0003_auto_20190524_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infocompos',
            name='genere',
            field=models.CharField(choices=[('Pop', 'Pop'), ('Rock', 'Rock'), ('Trap', 'Trap'), ('Reggaeton', 'Reggaeton'), ('EDM', 'EDM'), ('Clasica', 'Clasica'), ('Indie', 'Indie')], max_length=50),
        ),
    ]