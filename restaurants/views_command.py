# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse
from django.http import JsonResponse
from .model_restaurant import Restaurant
from model_command import Command


def generate_command(request):
    name = request.GET.get("name")
    delivery_date = request.GET.get("deliveryDate")
    creation_date = request.GET.get("creationDate")
    user_tel = request.GET.get("userTel")
    if name is None or delivery_date is None or creation_date is None or user_tel is None:
        response_data = {"error": "invalid request, missing params"}
        return JsonResponse(response_data)

    #TODO use post
    if request.method == "POST":
        pass
    command = Command(name=name, delivery_date=delivery_date, creation_date=creation_date, user_tel=user_tel)
    command.save()
    response_data = {"data": {"code": command.id}}
    return JsonResponse(response_data)
