# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-17 15:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basededonnee', '0031_covutil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covutil',
            name='LieuArrivee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='LieuArrivee', to='basededonnee.Lieu'),
        ),
    ]