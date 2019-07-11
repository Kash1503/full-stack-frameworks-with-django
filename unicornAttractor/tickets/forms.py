from django import forms
from .models import Ticket

class CreateTicketForm(forms.ModelForm):
    """Form to create a Ticket Object using the Ticket model"""
    class Meta:
        model = Ticket
        fields = ('title', 'description')