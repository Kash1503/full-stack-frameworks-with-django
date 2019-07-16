from django.shortcuts import render
import stripe
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import OrderForm, MakePaymentForm

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required()
def checkout(request):
    """
    Allow users to purchase tickets stored in the cart
    """

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
    else:
        order_form = OrderForm()
        payment_form = MakePaymentForm()

    return render(request, 'checkout.html', {'order_form': order_form, 'payment_form': payment_form})
