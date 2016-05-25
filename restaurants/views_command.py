# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse
from django.http import JsonResponse
from .model_restaurant import Restaurant, Dish
from .model_command import Command,NumberDish
from datetime import datetime


def generate_command(request):
    name = request.GET.get("name")
    delivery_date = request.GET.get("deliveryDate")
    user_tel = request.GET.get("userTel")
    dishes_ids = request.GET.getlist("dishId")
    dishes_numbers = request.GET.getlist("dishNb")
    restaurant_id = request.GET.get("restaurantId")
    if name is None or delivery_date is None or user_tel is None  or restaurant_id is None or dishes_ids is None or dishes_numbers is None:
        response_data = {"error": "invalid request, missing params"}
        return JsonResponse(response_data)

    restaurant = Restaurant.objects.filter(id=restaurant_id)[0]

    for dish_id in dishes_ids:
        if (len(Dish.objects.filter(id=dish_id)) == 0):
            response_data = {"error": "the dishes you have requested does not exist"}
            return JsonResponse(response_data)

    creation_date = datetime.now().isoformat()

    command = Command(name=name, delivery_date=delivery_date, creation_date=creation_date, user_tel=user_tel, restaurant=restaurant)
    command.save()
    for dish_id, dish_nb in zip(dishes_ids, dishes_numbers):
        dish = Dish.objects.filter(id=dish_id)[0]
        numberDish = NumberDish(plat_commande=dish, nombre=dish_nb)
        numberDish.save()
        command.dishes.add(numberDish)
    response_data = {"data": {"code": command.id}}
    return JsonResponse(response_data)
