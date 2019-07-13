from django import forms
from .models import Ticket, Comments

class CreateTicketForm(forms.ModelForm):
    """Form to create a Ticket Object using the Ticket model"""
    class Meta:
        model = Ticket
        fields = ('title', 'description')


class EditTicketForm(forms.ModelForm):
    """Form to edit a Ticket Object"""
    class Meta:
        STATUS_CHOICES = [
            ('reviewing', 'Reviewing'),
            ('in progress', 'In Progress'),
            ('closed', 'Closed')
        ]
        
        TICKET_TYPE_CHOICES = [
            ('bug', 'Bug'),
            ('feature', 'Feature'),
        ]

        model = Ticket
        fields = ('title', 'description', 'status', 'ticket_type')
        widgets = {
            'status': forms.Select(choices=STATUS_CHOICES),
            'ticket_type': forms.Select(choices=TICKET_TYPE_CHOICES)
        }

class CommentForm(forms.ModelForm):
    """Form to create and leave a comment on a ticket"""
    class Meta:
        model = Comments
        fields = ('body', )


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

    ticket_type = forms.CharField(label='Ticket type', required=False, widget=forms.Select(choices=TICKET_TYPE_CHOICES))
    sort_by = forms.CharField(label='Sort By', required=False, widget=forms.Select(choices=SORT_BY_CHOICES))