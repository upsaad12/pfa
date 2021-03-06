# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 17:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basededonnee', '0004_remove_parent_nom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parent',
            old_name='user',
            new_name='userP',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='Nom',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='Nom_de_compte',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='Prenom',
        ),
        migrations.RemoveField(
            model_name='enfant',
            name='mot_de_passe',
        ),
        migrations.AddField(
            model_name='enfant',
            name='userE',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='enfant',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basededonnee.Parent'),
        ),
    ]
