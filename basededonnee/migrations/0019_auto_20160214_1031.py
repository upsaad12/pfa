# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-14 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basededonnee', '0018_telephone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Telephone',
        ),
        migrations.AddField(
            model_name='parent',
            name='Couleur_voiture',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='parent',
            name='Immatriculation',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='parent',
            name='Nombre_place',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='parent',
            name='Numero_Telephone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
