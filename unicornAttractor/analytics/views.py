from django.shortcuts import render
from tickets.models import Ticket
from django.core.serializers import serialize
from django.http import HttpResponse

# Create your views here.
def get_json_data(request):
    """
    Query the database and return all closed tickets in JSON format to be used by D3.js
    """

    closed_tickets = serialize('json', Ticket.objects.filter(status__exact='closed'))
    return HttpResponse(closed_tickets, content_type="application/json")


def dashboard(request):
    """
    Render the data dashboard and pass through any relevant data
    """

    top_features = Ticket.objects.filter(ticket_type__exact='feature').exclude(status__exact='closed').order_by('-value')[:5]
    top_bugs = Ticket.objects.filter(ticket_type__exact='bug').exclude(status__exact='closed').order_by('-upvotes')[:5]

    return render(request, 'dashboard.html', {'top_features': top_features, 'top_bugs': top_bugs})


