from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from .forms import LoginForm, RegistrationForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from tickets.models import Ticket
import math

# Create your views here.

@login_required
def logout(request):
    """Function to allow users to logout"""

    auth.logout(request)
    messages.success(request, 'You have been successfully logged out')
    
    return redirect(reverse('index'))


def login(request):
    """Function to allow users to log in"""

    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        login_form = LoginForm(request.POST, label_suffix='')

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You have successfully logged in!')
                return redirect(reverse('index'))
            else:
                messages.error(request, 'Your username or password is incorrect')

    else:
        login_form = LoginForm(label_suffix='')

    return render(request, 'login.html', {'login_form': login_form})


def register(request):
    """Render the registration form and handle registration logic"""

    if request.user.is_authenticated:
        return redirect(reverse('account_login'))

    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST, label_suffix='')
        profile_form = UserProfileForm(request.POST, label_suffix='')

        if registration_form.is_valid() and profile_form.is_valid():
            registration_form.save()
            user_profile = profile_form.save(commit=False)

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You have successfully registered!')
                user_profile.userID = request.user
                user_profile.save()
                return redirect(reverse('index'))
            
            else:
                messages.error(request, 'We were unable to create a new account at this time')

    else:
        registration_form = RegistrationForm(label_suffix='')
        profile_form = UserProfileForm(label_suffix='')
    
    return render(request, 'register.html', {'registration_form': registration_form, 'profile_form': profile_form})


def user_profile(request, current_page):
    """
    Render the users profile page with the users information
    """
    user_profile = UserProfile.objects.get(userID=request.user)

    all_user_tickets = Ticket.objects.filter(userID__exact=request.user)

    page_amount = math.ceil(all_user_tickets.count() / 5)
    pages = []
    page = 1
    while page <= page_amount:
        pages.append(page)
        page += 1

    user_tickets = Ticket.objects.filter(userID__exact=request.user)[(int(current_page)*5)-5:int(current_page)*5]

    total_tickets = 0
    for ticket in user_tickets:
        total_tickets += 1

    return render(request, 'user-profile.html', {'user_profile': user_profile, 'user_tickets': user_tickets, 'total_tickets': total_tickets, 'pages': pages})