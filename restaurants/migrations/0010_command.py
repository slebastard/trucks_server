# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-25 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0009_restaurant_dishes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.CharField(blank=True, max_length=25)),
                ('delivery_date', models.CharField(blank=True, max_length=25)),
                ('name', models.CharField(blank=True, max_length=40)),
            ],
        ),
    ]
