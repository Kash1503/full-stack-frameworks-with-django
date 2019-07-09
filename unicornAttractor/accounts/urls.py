from django.urls import path
from .views import logout, login

urlpatterns = [
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
]