from django.urls import path
from .views import get_json_data, dashboard

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('get_data', get_json_data, name='get_json_data'),
]