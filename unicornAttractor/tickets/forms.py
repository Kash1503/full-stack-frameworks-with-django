from django import forms
from .models import Ticket, Comments

class CreateTicketForm(forms.ModelForm):
    """Form to create a Ticket Object using the Ticket model"""
    class Meta:
        model = Ticket
        fields = ('title', 'description')
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-textbox', 'placeholder': 'Enter a description here...'})
        }


class EditTicketForm(forms.ModelForm):
    """Form to edit a Ticket Object"""
    class Meta:

        model = Ticket
        fields = ('title', 'description', 'ticket_type')
        widgets = { 
            'ticket_type': forms.Select(attrs={'class': 'form-dropdown'}),
            'description': forms.Textarea(attrs={'class': 'form-textbox'})
        }

class CommentForm(forms.ModelForm):
    """Form to create and leave a comment on a ticket"""
    class Meta:
        model = Comments
        fields = ('body', )
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-textbox', 'placeholder': 'Leave a comment...'})
        }


class FilterForm(forms.Form):
    """Form used to filter tickets using database queries"""

    SORT_BY_CHOICES = [
        ('dateTimeCreated', 'Newest'),
        ('-dateTimeCreated', 'Oldest'),
        ('-upvotes', 'Most liked'),
        ('-views', 'Most viewed'),
    ]

    TICKET_TYPE_CHOICES = [
        ('bug', 'Bug'),
        ('feature', 'Feature'),
        ('all', 'All'),
    ]

    ticket_type = forms.CharField(label='Ticket type', required=False, widget=forms.Select(choices=TICKET_TYPE_CHOICES, attrs={'class': 'form-dropdown'}))
    sort_by = forms.CharField(label='Sort By', required=False, widget=forms.Select(choices=SORT_BY_CHOICES, attrs={'class': 'form-dropdown'}))