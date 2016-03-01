# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-14 10:43
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basededonnee', '0021_auto_20160214_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='Nombre_place',
            field=models.CharField(blank=True, max_length=3, null=True, validators=[django.core.validators.RegexValidator(message='Format de nombre de place incorrect.', regex='^\\d{0,3}$')]),
        ),
        migrations.AlterField(
            model_name='parent',
            name='Numero_Telephone',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message='Format de numéro de téléphone incorrect.', regex='^\\d{9,15}$')]),
        ),
    ]