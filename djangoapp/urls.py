from django.urls import path
from . import views

app_name = 'djangoapp'

urlpatterns = [
    path('api/zip-codes/', views.api_zip_codes),
    path('api/data/<zipCode>/', views.api_get_data_from_zip),
    path('api/data/', views.api_modify_data),
    path('',views.index)
]