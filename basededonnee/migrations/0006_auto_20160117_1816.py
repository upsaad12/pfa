# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 18:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basededonnee', '0005_auto_20160117_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enfant',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basededonnee.Parent'),
        ),
    ]
