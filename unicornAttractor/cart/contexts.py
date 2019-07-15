from django.shortcuts import get_object_or_404
from tickets.models import Ticket

def cart_contents(request):
    """
    Keeps track of the contents of the cart accross all pages
    """

    cart = request.session.get('cart', {})

    cart_tickets = []
    total_pledge = 0
    ticket_count = 0
    for id, pledge in cart.items():
        ticket = get_object_or_404(Ticket, pk=id)
        total_pledge += pledge
        ticket_count += 1
        cart_tickets.append({'id': id, 'pledge': pledge, 'ticket': ticket})

    return {'cart_tickets': cart_tickets, 'total_pledge': total_pledge, 'ticket_count': ticket_count}
