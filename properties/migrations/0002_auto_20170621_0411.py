# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 04:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='own_bathroom',
            field=models.BooleanField(default=False, verbose_name='has own bathroom'),
        ),
        migrations.AlterField(
            model_name='room',
            name='own_kitchen',
            field=models.BooleanField(default=False, verbose_name='has own kitchen'),
        ),
    ]