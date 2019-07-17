from django.shortcuts import render
from tickets.models import Ticket
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
def get_json_data(request):
    """
    Query the database and return the data in JSON format to be used by DC/D3.js
    """

    tickets = Ticket.objects.all()
    tickets = serializers.serialize('json', tickets)
    return HttpResponse(tickets, content_type='application/json')


def dashboard(request):
    """
    Render the data dashboard and pass through any relevant data
    """

    return render(request, 'dashboard.html')


