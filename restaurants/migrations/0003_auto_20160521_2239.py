# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-21 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20160521_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
