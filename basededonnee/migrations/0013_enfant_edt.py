# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 20:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basededonnee', '0012_edt'),
    ]

    operations = [
        migrations.AddField(
            model_name='enfant',
            name='EDT',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basededonnee.Edt'),
        ),
    ]
