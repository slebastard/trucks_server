# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .model_restaurant import Dish

class Command(models.Model):
    creation_date = models.CharField(max_length=25,
                            blank=True)
    delivery_date = models.CharField(max_length=25,
                            blank=True)
    name = models.CharField(max_length=40,
                            blank=True)
    user_tel = models.CharField(max_length=12,
                            blank=True)
    plat_commande = models.ForeignKey("NumberDish",
                            null=True)

    def generate_id(self):
        return self.id

class NumberDish(models.Model):
    plat_commande = models.ForeignKey("Dish",
                            null=True)
    nombre = models.IntegerField(verbose_name="nombre",
                            null=True)
