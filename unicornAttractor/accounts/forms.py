from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    """Form to allow users to input log in details and log in"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    """Form to allow users to input their details and create a new account"""

    password1 = forms.CharField(label='Password *', widget=forms.PasswordInput, label_suffix='')
    password2 = forms.CharField(label='Confirm your password *', widget=forms.PasswordInput, label_suffix='')
    firstName = forms.CharField(label='First Name *', label_suffix='')
    lastName = forms.CharField(label='Last Name *', label_suffix='')
    address1 = forms.CharField(label='Address 1', required=False, label_suffix='')
    address2 = forms.CharField(label='Address 2', required=False, label_suffix='')
    city = forms.CharField(required=False, label_suffix='')
    postcode = forms.CharField(required=False, label_suffix='')
    username = forms.CharField(label='Username *', label_suffix='')
    email = forms.CharField(label='Email Address *', label_suffix='')

    class Meta:
        model = User
        fields = ['username', 'firstName', 'lastName', 'email', 'password1', 'password2', 'address1', 'address2', 'city', 'postcode']