# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-25 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0010_command'),
    ]

    operations = [
        migrations.AddField(
            model_name='command',
            name='user_tel',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
