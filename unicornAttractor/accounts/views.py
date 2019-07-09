from django.shortcuts import render, redirect, reverse
from django.contrib import auth

# Create your views here.

def logout(request):
    """Function to allow users to logout"""

    auth.logout(request)
    return redirect(reverse('index'))