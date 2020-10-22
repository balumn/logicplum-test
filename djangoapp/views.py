from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .async_tasks import read_csv_zipcodes
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