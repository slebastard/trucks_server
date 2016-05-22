# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse
from django.http import JsonResponse
from .model_restaurant import Restaurant


def show_resto(request):
    restaurants_model = Restaurant.objects.all()
    restaurants_list = []
    for restaurant in restaurants_model:
        restaurants_list.append(restaurant.to_dict())
    response_data = {"data": restaurants_list}
    return JsonResponse(response_data)
