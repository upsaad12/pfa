# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basededonnee', '0011_journee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('J', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='J', to='basededonnee.Journee')),
                ('L', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='L', to='basededonnee.Journee')),
                ('M', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='M', to='basededonnee.Journee')),
                ('Mer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Mer', to='basededonnee.Journee')),
                ('S', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='S', to='basededonnee.Journee')),
                ('V', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='V', to='basededonnee.Journee')),
            ],
        ),
    ]
