from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_cart(request):
    """
    Render the cart.html page to view the cart contents
    """
    return render(request, 'cart.html')


def add_to_cart(request, id):
    """
    Pledge a certain value to a given ticket, specified by the tickets id
    """

    pledge = round(float(request.POST.get('pledge')), 2)
    cart = request.session.get('cart', {})

    if id in cart:
        cart[id] = round(float(cart[id]) + pledge, 2)
    else:
        cart[id] = cart.get(id, pledge)

    request.session['cart'] = cart
    return redirect(reverse('ticket_details', args=[id]))


def adjust_pledge(request, id):
    """
    Adjust the amount pledged to the feature ticket
    """

    pledge = round(float(request.POST.get('pledge')), 2)
    cart = request.session.get('cart', {})
    cart[id] = pledge
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def delete_ticket(request, id):
    """
    Delete the ticket from the cart
    """

    cart = request.session.get('cart', {})
    cart.pop(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))