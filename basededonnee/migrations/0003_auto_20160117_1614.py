# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 16:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basededonnee', '0002_auto_20160117_1610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parent',
            old_name='utilisateur',
            new_name='user',
        ),
    ]
