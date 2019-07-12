from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import CreateTicketForm, CommentForm
from .models import Ticket, Comments

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
    """
    Render the create-ticket.html page and allow users to create a new ticket.
    Check the ticket_type passed from the template to determine which type of
    ticket to create. Update the Ticket Object with the user who created it, and
    the username of the user to last update it
    """

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


def ticket_details(request, pk):
    """
    Get the details of the selected ticket and pass them to the rendered html page
    Create a list of comments linked to the ticket and pass them to the rendered html page
    Create the form to allow users to leave a new comment
    """

    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.views += 1
    ticket.save()

    comments_list = Comments.objects.filter(ticketID__exact=ticket).order_by('dateTimeCreated')

    if request.method =='POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.userID = request.user
            new_comment.ticketID = get_object_or_404(Ticket, pk=pk)
            new_comment.save()
            updated_comments_list = Comments.objects.filter(ticketID__exact=ticket).order_by('dateTimeCreated')
            return render(request, 'ticket-details.html', {'ticket': ticket, 'comment_form': CommentForm(), 'comments_list': updated_comments_list})

    else:
        comment_form = CommentForm()

    return render(request, 'ticket-details.html', {'ticket': ticket, 'comment_form': comment_form, 'comments_list': comments_list})