# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 19:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basededonnee', '0006_auto_20160117_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='lieu',
            name='proprietaire',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basededonnee.Parent'),
        ),
    ]
