from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .async_tasks import *
import json
from rest_framework.parsers import JSONParser
from django.http import QueryDict

@api_view(['GET'])
def api_zip_codes(request):
    _status,status_code,data = read_csv_zipcodes() # NOT AN ASYNC TASK
    return JsonResponse(
        {
            "status": _status,
            "zip"   : data
        },status = status_code
    )

@api_view(['GET'])
def api_get_data_from_zip(request, zipCode):
    print(zipCode)

    _status,status_code,data = read_csv_get_document(zipCode) # NOT AN ASYNC TASK
    return JsonResponse(
        {
            "status"    : _status,
            "document"  : data
        },status = status_code
    )

@api_view(['PUT'])
def api_modify_data(request):
    if request.method == "PUT":
        data_input = json.loads(request.body.decode("utf-8"))
        try:
            _zip = data_input["zip"]
        except:
            return JsonResponse({"status":False,"error":"zip is a must parameter"},status = 400)
        try:
            population = data_input["population"]
        except:
            return JsonResponse({"status":False,"error":"population is a must parameter"},status = 400)
        
        update_population.delay(_zip,population)           
        
        return JsonResponse(
            {
                "status" : True,
                "job"    : "Initialized"
            },status = 200
        )
    else:
        return True