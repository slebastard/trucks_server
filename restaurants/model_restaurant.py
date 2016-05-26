# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .currencies import *

WEEK_DAYS = (
        (0, 'monday'),
        (1, 'tuesday'),
        (2, 'wednesday'),
        (3, 'thursday'),
        (4, 'friday'),
        (5, 'saturday'),
        (6, 'sunday')
    )

class OpeningHour(models.Model):
    opening = models.CharField(max_length=14,
                            blank=True)
    closing = models.CharField(max_length=14,
                            blank=True)
    day = models.IntegerField(choices=WEEK_DAYS, default=-1)
    def to_dict(self):
        exp_dict = {}
        exp_dict[self.opening] = self.closing
        return exp_dict

class Dish(models.Model):
    name = models.CharField(max_length=50,
                            blank=True)
    imageUrl = models.CharField(max_length=1000,
                            blank=True)
    description = models.CharField(max_length=1000,
                            blank=True)
    # Pour la gestion des prix avec le module py-moneyed
    prix = models.FloatField(verbose_name="prix",
                            null=True, blank=True)
    devise = models.CharField(max_length=10,
                            choices=CURRENCIES,
                            default="EUR")
    def to_dict(self):
        fields = [
            'id',
            'name',
            'imageUrl',
            'description'
        ]

        exp_dict = {field: self.serializable_value(field) for field in fields}
        return exp_dict

class Restaurant(models.Model):
    name = models.CharField(max_length=50,
                            blank=True)
    address = models.CharField(max_length=100,
                            blank=True)
    tel = models.CharField(max_length=12,
                            blank=True)
    description = models.CharField(max_length=100,
                            blank=True)
    imageUrl = models.CharField(max_length=1000,
                            blank=True)
    longitude = models.FloatField(verbose_name="longitude",
                            null = True, blank = True)
    latitude = models.FloatField(verbose_name="latitude",
                            null = True, blank = True)
    #TODO change name
    monday = models.ManyToManyField(OpeningHour)
    dishes = models.ManyToManyField(Dish)

    def to_dict(self):
        fields = [
            'id',
            'name',
            'address',
            'tel',
            'description',
            'imageUrl',
            'latitude',
            'longitude'
        ]

        exp_dict = {field: self.serializable_value(field) for field in fields}
        exp_dict['disponibility'] = {
                'monday': [],
                'tuesday': [],
                'wednesday': [],
                'thursday': [],
                'friday': [],
                'saturday': [],
                'sunday': []
            }
        for hour in self.monday.all():
            exp_dict['disponibility'][WEEK_DAYS[hour.day][1]].append(hour.to_dict())

        exp_dict["dishes"] = [dish.to_dict() for dish in self.dishes.all()]
        return exp_dict
