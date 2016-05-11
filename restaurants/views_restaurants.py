import json

from django.http import HttpResponse
from django.http import JsonResponse


def show_resto(request):
    response_data = {}
    response_data['resto1'] = {}
    response_data['resto1']['ID'] = 8
    response_data['resto1']['name'] = 'nom'
    response_data['resto1']['type'] = 'externalKey'
    response_data['resto1']['disponibility'] =  {}
    response_data['resto1']['disponibility']['monday'] =
    response_data['resto1']['disponibility']['monday'] =  ['10h-12h','13h-18h']
    response_data['resto1']['disponibility']['tuesday'] =  ['10h-22h']
    response_data['resto1']['disponibility']['wednesday'] =  ['10h-22h']
    response_data['resto1']['disponibility']['thursday'] =  ['10h-22h']
    response_data['resto1']['disponibility']['friday'] =  ['10h-22h']
    response_data['resto1']['disponibility']['saturday'] =  ['10h-22h']
    response_data['resto1']['disponibility']['sunday'] =  ['10h-22h']
    response_data['resto1']['tel'] = '+33705432543'
    response_data['resto1']['adress'] = 'adresse'
    # liste_restos = {ID: 8, name: ' ', type: externalKey, disponibility: {monday: [{IsoStringOpenHour: IsoStringCloseHour}]}, tel: '+33705432543', address: ''}
    return JsonResponse(response_data)
    # http_response = HttpResponse(json.dumps(response_data), content_type='application/json')
    # return http_response
