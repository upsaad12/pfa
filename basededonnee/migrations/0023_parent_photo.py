# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-14 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basededonnee', '0022_auto_20160214_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='../media/'),
        ),
    ]