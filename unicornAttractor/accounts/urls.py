from django.urls import path
from .views import logout, login, register

urlpatterns = [
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]