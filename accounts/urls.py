from django.urls import path, include
from .views import logout, login, register, user_profile

urlpatterns = [
    path('logout/', logout, name='account_logout'),
    path('login/', login, name='account_login'),
    path('register/', register, name='register'),
    path('password/', include('django.contrib.auth.urls')),
    path('profile/<current_page>', user_profile, name='user_profile')
]