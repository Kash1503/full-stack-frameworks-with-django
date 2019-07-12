from django.urls import path
from django.conf.urls import url
from .views import tracker, create_ticket, ticket_details

urlpatterns = [
    path('', tracker, name='tracker'),
    path('new-ticket/<ticket_type>/', create_ticket, name='new_ticket'),
    url(r'^(?P<pk>\d+)/$', ticket_details, name='ticket_details')
]