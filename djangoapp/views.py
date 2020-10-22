from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_zip_codes(request):
    return JsonResponse({'status':True})