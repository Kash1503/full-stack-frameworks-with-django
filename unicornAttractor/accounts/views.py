from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from .forms import LoginForm, RegistrationForm
from django.contrib.auth.decorators import login_required

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
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You have successfully logged in!')
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, 'Your username or password is incorrect')

    else:
        login_form = LoginForm()

    return render(request, 'login.html', {'login_form': login_form})


def register(request):
    """Render the registration form and handle registration logic"""

    if request.user.is_authenticated:
        return redirect(reverse('account_login'))

    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You have successfully registered!')
                return redirect(reverse('index'))
            
            else:
                messages.error(request, 'We were unable to create a new account at this time')

    else:
        registration_form = RegistrationForm()
    
    return render(request, 'register.html', {'registration_form': registration_form})