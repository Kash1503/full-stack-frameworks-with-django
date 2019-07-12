from django.urls import path
from .views import tracker, create_ticket

urlpatterns = [
    path('', tracker, name='tracker'),
    path('new-ticket/<ticket_type>/', create_ticket, name='new_ticket'),
]