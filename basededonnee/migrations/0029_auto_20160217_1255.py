# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-17 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basededonnee', '0028_auto_20160216_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='covoiturage',
            name='h_arrivee',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='covoiturage',
            name='h_depart',
            field=models.TimeField(null=True),
        ),
    ]
