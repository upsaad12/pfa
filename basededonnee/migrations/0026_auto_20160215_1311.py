# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-15 13:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basededonnee', '0025_auto_20160215_0709'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ecole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=40, null=True)),
                ('Adresse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basededonnee.Lieu', unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='enfant',
            name='Ecole',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basededonnee.Ecole'),
        ),
    ]