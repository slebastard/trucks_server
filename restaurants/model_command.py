# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Command(models.Model):
    creation_date = models.CharField(max_length=25,
                            blank=True)
    delivery_date = models.CharField(max_length=25,
                            blank=True)
    name = models.CharField(max_length=40,
                            blank=True)
    user_tel = models.CharField(max_length=12,
                            blank=True)

    def generate_id(self):
        return self.id
