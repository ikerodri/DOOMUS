# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-24 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compo', '0002_auto_20190523_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='infocompos',
            name='arxiu',
            field=models.FileField(blank=True, default='/static/Compo/DefaultFile.mp3', upload_to='Compos'),
        ),
        migrations.AlterField(
            model_name='infocompos',
            name='genere',
            field=models.CharField(max_length=50),
        ),
    ]