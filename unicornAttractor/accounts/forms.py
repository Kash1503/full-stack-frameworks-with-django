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
    first_name = forms.CharField(label='First Name *', label_suffix='')
    last_name = forms.CharField(label='Last Name *', label_suffix='')
    username = forms.CharField(label='Username *', label_suffix='')
    email = forms.CharField(label='Email Address *', label_suffix='')
    # address1 = forms.CharField(label='Address 1', required=False, label_suffix='')
    # address2 = forms.CharField(label='Address 2', required=False, label_suffix='')
    # city = forms.CharField(required=False, label_suffix='')
    # postcode = forms.CharField(required=False, label_suffix='')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        """function used to ensure that unique email address is used"""

        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')

        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'There is already an account linked to that email address!')
        
        return email
    
    def clean_password2(self):
        """function used to validate the passwords"""

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise forms.ValidationError('Please confirm your password')
        
        if password1 != password2:
            raise forms.ValidationError('Passwords must match')

        return password2