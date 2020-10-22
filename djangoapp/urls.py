from django.urls import path
from . import views

app_name = 'djangoapp'

urlpatterns = [
    path('api/zip-codes/', views.api_zip_codes),
    # path('message/pull', views.message_pull_view),
]