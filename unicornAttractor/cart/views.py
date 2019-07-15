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

    pledge = int(request.POST.get('pledge'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + pledge
    else:
        cart[id] = cart.get(id, pledge)

    request.session['cart'] = cart
    return redirect(reverse('ticket_details', args=[id]))


def adjust_pledge(request, id):
    """
    Adjust the amount pledged to the feature ticket
    """

    pledge = int(request.POST.get('pledge'))
    cart = request.session.get('cart', {})

    if pledge > 0:
        cart[id] = pledge
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))