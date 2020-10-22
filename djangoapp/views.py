from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .async_tasks import read_csv_zipcodes, read_csv_get_document
import json

@api_view(['GET'])
def api_zip_codes(request):
    status,data = read_csv_zipcodes() # NOT AN ASYNC TASK
    return JsonResponse(
        {
            "status": status,
            "zip"   : data
        }
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