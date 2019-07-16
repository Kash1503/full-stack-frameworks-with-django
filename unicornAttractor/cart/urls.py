from django.urls import path
from django.conf.urls import url
from .views import view_cart, add_to_cart, adjust_pledge, delete_ticket

urlpatterns = [
    path('', view_cart, name='view_cart'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^adjust/(?P<id>\d+)', adjust_pledge, name='adjust_pledge'),
    url(r'^delete/(?P<id>\d+)', delete_ticket, name='delete_ticket'), 
]