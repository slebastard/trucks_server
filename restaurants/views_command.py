# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse
from django.http import JsonResponse
from .model_restaurant import Restaurant, Dish
from model_command import Command, NumberDish


def generate_command(request):
    name = request.GET.get("name")
    delivery_date = request.GET.get("deliveryDate")
    creation_date = request.GET.get("creationDate")
    user_tel = request.GET.get("userTel")
    id_dish = request.GET.get("id")
    if (len(Dish.objects.filter(id=id_dish)) == 0):
        plat_cmd = None
    else:
        plat_cmd = NumberDish()
        plat_cmd.plat_commande = Dish.objects.filter(id=id_dish)[0]
        plat_cmd.nombre = request.GET.get("nbPlats")
    if name is None or delivery_date is None or creation_date is None or user_tel is None  or plat_cmd is None:
        response_data = {"error": "invalid request, missing params"}
        return JsonResponse(response_data)

    #TODO use post
    if request.method == "POST":
        pass
    command = Command(name=name, delivery_date=delivery_date, creation_date=creation_date, user_tel=user_tel, plat_commande=plat_cmd)
    command.save()
    response_data = {"data": {"code": command.id}}
    return JsonResponse(response_data)
