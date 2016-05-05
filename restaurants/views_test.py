import json

from django.http import HttpResponse

def show_test(request):
    test_dict = {"test":"test"}
    http_response = HttpResponse(json.dumps(test_dict), content_type='application/json')
    return http_response
