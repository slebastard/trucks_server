# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-21 23:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_restaurant_imageurl'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpeningHour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opening', models.CharField(blank=True, max_length=14)),
                ('closing', models.CharField(blank=True, max_length=14)),
            ],
        ),
    ]
