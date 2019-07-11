from django.urls import path
from .views import tracker, create_new_bug

urlpatterns = [
    path('', tracker, name='tracker'),
    path('new-bug/', create_new_bug, name='new_bug'),
]