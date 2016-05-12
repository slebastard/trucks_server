import json

from django.http import HttpResponse
from django.http import JsonResponse
from datetime import time


def show_resto(request):
    response_data = {}
    response_data['resto1'] = {}
    response_data['resto1']['ID'] = 8
    response_data['resto1']['name'] = 'nom'
    response_data['resto1']['type'] = 'externalKey'
    response_data['resto1']['disponibility'] = {'monday': [], 'tuesday': [],
            'wednesday': [], 'thursday': [], 'friday': [], 'saturday': [], 'sunday': []}
    response_data['resto1']['disponibility']['monday'].append({time(10).isoformat(): time(12).isoformat()})
    response_data['resto1']['disponibility']['monday'].append({time(13).isoformat(): time(18).isoformat()})
    response_data['resto1']['disponibility']['tuesday'].append({time(10).isoformat(): time(22).isoformat()})
    response_data['resto1']['disponibility']['wednesday'].append({time(10).isoformat(): time(22).isoformat()})
    response_data['resto1']['disponibility']['thursday'].append({time(10).isoformat(): time(22).isoformat()})
    response_data['resto1']['disponibility']['friday'].append({time(10).isoformat(): time(22).isoformat()})
    response_data['resto1']['disponibility']['saturday'].append({time(10).isoformat(): time(22).isoformat()})
    response_data['resto1']['disponibility']['sunday'].append({time(10).isoformat(): time(22).isoformat()})
    response_data['resto1']['tel'] = '+33705432543'
    response_data['resto1']['adress'] = 'adresse'
    return JsonResponse(response_data)
