from django.urls import path, include
from .views import logout, login, register

urlpatterns = [
    path('logout/', logout, name='account_logout'),
    path('login/', login, name='account_login'),
    path('register/', register, name='register'),
    path('password/', include('django.contrib.auth.urls')),
]