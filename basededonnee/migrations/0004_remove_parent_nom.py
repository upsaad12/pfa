# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 16:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basededonnee', '0003_auto_20160117_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='Nom',
        ),
    ]
