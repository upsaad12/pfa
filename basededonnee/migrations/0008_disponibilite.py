# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-18 09:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basededonnee', '0007_lieu_proprietaire'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disponibilite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debut', models.TimeField()),
                ('fin', models.TimeField()),
                ('userP', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basededonnee.Parent')),
            ],
        ),
    ]
