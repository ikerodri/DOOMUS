# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-24 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compo', '0004_auto_20190524_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infocompos',
            name='instrument',
            field=models.CharField(choices=[('Piano', 'Piano'), ('Guitarra', 'Guitarra'), ('Baix', 'Baix'), ('Bateria', 'Bateria'), ('Sintetitzador', 'Sintetitzador'), ('Strings', 'Strings')], max_length=50),
        ),
        migrations.AlterField(
            model_name='infocompos',
            name='tonalitat',
            field=models.CharField(choices=[('C Maj', 'C Maj'), ('C min', 'C min'), ('C# Maj', 'C# Maj'), ('C# min', 'C# min'), ('D Maj', 'D Maj'), ('D min', 'D min'), ('D# Maj', 'D# Maj'), ('D# min', 'D# min'), ('E Maj', 'E Maj'), ('E min', 'E min'), ('F Maj', 'F Maj'), ('F min', 'F min'), ('F# Maj', 'F# Maj'), ('F# min', 'F# min'), ('G Maj', 'G Maj'), ('G min', 'G min'), ('G# Maj', 'G# Maj'), ('G# min', 'G# min'), ('A Maj', 'A Maj'), ('A min', 'A min'), ('A# Maj', 'A# Maj'), ('A# min', 'A# min'), ('B Maj', 'B Maj'), ('B min', 'B min')], max_length=50),
        ),
    ]
