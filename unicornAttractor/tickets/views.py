from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import CreateTicketForm
from .models import Ticket

# Create your views here.

def tracker(request):
    """
    Load the tracker page with a list of tickets which are not of 'closed' status
    and sort them by the oldest first
    """

    if request.user.is_authenticated:
        tickets = Ticket.objects.exclude(status__exact='closed').order_by('dateTimeCreated')
        return render(request, 'tracker.html', {'tickets': tickets})
    else:
        return redirect(reverse('account_login'))

def create_ticket(request, ticket_type):
    """Render the create-ticket.html page and allow users to create a new ticket"""

    if ticket_type == 'bug':
        header = 'Log a new bug'
    elif ticket_type == 'feature':
        header = 'Request a new feature'

    if request.method == 'POST':
        create_ticket_form = CreateTicketForm(request.POST)

        if create_ticket_form.is_valid():
            new_ticket = create_ticket_form.save(commit=False)
            new_ticket.ticket_type = ticket_type
            new_ticket.userID = request.user
            new_ticket.lastUpdatedBy = request.user.username
            new_ticket.save()
            messages.success(request, 'Your ' + ticket_type + ' has been logged successfully!')
            return redirect(reverse('tracker'))
    else:
        create_ticket_form = CreateTicketForm()

    return render(request, 'create-ticket.html', {'create_ticket_form': create_ticket_form, 'header': header})