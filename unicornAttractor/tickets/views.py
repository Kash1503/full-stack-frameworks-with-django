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

def create_new_bug(request):
    """load the create a bug page"""

    if request.method == 'POST':
        create_ticket_form = CreateTicketForm(request.POST)

        if create_ticket_form.is_valid():
            create_ticket_form.save()
            messages.success(request, 'Your bug has been logged successfully!')
            return redirect(reverse('tracker'))
    else:
        create_ticket_form = CreateTicketForm()

    return render(request, 'create-bug.html', {'create_ticket_form': create_ticket_form})