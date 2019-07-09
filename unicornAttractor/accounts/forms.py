from django import forms

class LoginForm(forms.Form):
    """Form to allow users to input log in details and log in"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)