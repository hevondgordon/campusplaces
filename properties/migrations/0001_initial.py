# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-28 04:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('address_line_1', models.CharField(blank=True, default='', max_length=255)),
                ('address_line_2', models.CharField(blank=True, default='', max_length=255)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('image', models.ImageField(blank=True, upload_to=b'')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('lat', models.PositiveIntegerField(blank=True, null=True)),
                ('lng', models.PositiveIntegerField(blank=True, null=True)),
                ('telephone_number', models.CharField(blank=True, default='', max_length=255)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address', to='properties.Address', verbose_name='Address')),
                ('images', models.ManyToManyField(blank=True, to='properties.Picture')),
                ('landlord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Property',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('price', models.PositiveIntegerField()),
                ('accomodation', models.CharField(choices=[(b'Single', b'Single'), (b'Shared', b'Shared')], default=b'Single', max_length=20)),
                ('own_kitchen', models.BooleanField(default=False, verbose_name='has own kitchen')),
                ('own_bathroom', models.BooleanField(default=False, verbose_name='has own bathroom')),
                ('images', models.ManyToManyField(blank=True, to='properties.Picture')),
                ('likes', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='likes')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.AddField(
            model_name='property',
            name='rooms',
            field=models.ManyToManyField(blank=True, related_name='property', to='properties.Room'),
        ),
    ]
