# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse
from django.http import JsonResponse
from datetime import time
import pytz


def show_resto(request):
    resto1 = {}
    resto1['ID'] = 8
    resto1['name'] = 'nom'
    resto1['type'] = 'externalKey'
    resto1['disponibility'] = {'monday': [], 'tuesday': [],
            'wednesday': [], 'thursday': [], 'friday': [], 'saturday': [], 'sunday': []}
    hour10 = time(hour=10, tzinfo=pytz.utc).isoformat()
    hour12 = time(hour=12, tzinfo=pytz.utc).isoformat()
    hour13 = time(hour=13, tzinfo=pytz.utc).isoformat()
    hour18 = time(hour=18, tzinfo=pytz.utc).isoformat()
    hour22 = time(hour=22, tzinfo=pytz.utc).isoformat()
    resto1['disponibility']['monday'].append({hour10: hour12, hour13: hour18})
    resto1['disponibility']['tuesday'].append({hour10: hour22})
    resto1['disponibility']['wednesday'].append({hour10: hour22})
    resto1['disponibility']['thursday'].append({hour10: hour22})
    resto1['disponibility']['friday'].append({hour10: hour22})
    resto1['disponibility']['saturday'].append({hour10: hour22})
    resto1['disponibility']['sunday'].append({hour10: hour22})
    resto1['tel'] = '+33705432543'
    resto1['address'] = 'addresse'
    resto1['description'] = 'Restaurant de sushis'
    resto1['imageUrl'] = None
    dishes = []
    dishes.append({
        'id': 0,
        'name': 'Plat 1',
        'description': 'description',
        'imageUrl': 'https://static.pexels.com/photos/5938/food-salad-healthy-lunch.jpg'
    })
    dishes.append({
        'id': 1,
        'name': 'Plat 2',
        'description': 'description',
        'imageUrl': 'https://static.pexels.com/photos/5938/food-salad-healthy-lunch.jpg'
    })
    dishes.append({
        'id': 1,
        'name': 'Plat 2',
        'description': 'description',
        'imageUrl': None
    })
    resto1['dishes'] = dishes
    response_data = {"data": [resto1]}
    return JsonResponse(response_data)
