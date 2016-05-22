# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-22 00:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_openinghour_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('imageUrl', models.CharField(blank=True, max_length=1000)),
                ('description', models.CharField(blank=True, max_length=1000)),
            ],
        ),
    ]
