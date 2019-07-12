from django import forms
from .models import Ticket, Comments

class CreateTicketForm(forms.ModelForm):
    """Form to create a Ticket Object using the Ticket model"""
    class Meta:
        model = Ticket
        fields = ('title', 'description')


class CommentForm(forms.ModelForm):
    """Form to create and leave a comment on a ticket"""
    class Meta:
        model = Comments
        fields = ('body', )