from django.shortcuts import render, get_object_or_404, redirect, reverse
import stripe
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
from .forms import OrderForm, MakePaymentForm
from accounts.models import UserProfile
from tickets.models import Ticket
from .models import OrderLineItem


# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required()
def checkout(request):
    """
    Allow users to purchase tickets stored in the cart
    """
    full_name = request.user.first_name + ' ' + request.user.last_name
    user_profile = UserProfile.objects.get(userID=request.user.id)

    if request.method == 'POST':
        order_form = OrderForm(request.POST, label_suffix='', initial={
            'full_name': full_name,
            'phone_number': user_profile.phone_number,
            'country': user_profile.country, 
            'county': user_profile.county, 
            'town_or_city': user_profile.town_or_city, 
            'postcode': user_profile.postcode, 
            'street1': user_profile.street1, 
            'street2': user_profile.street2,
        })
        payment_form = MakePaymentForm(request.POST, label_suffix='')

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date_ordered = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total_pledge = 0
            for id, pledge in cart.items():
                ticket = get_object_or_404(Ticket, pk=id)
                total_pledge += pledge
                order_line_item = OrderLineItem(
                    order=order,
                    ticket=ticket,
                    pledge=pledge
                )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total_pledge * 100),
                    currency = 'GBP',
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, 'Your card was declined!')

            if customer.paid:
                messages.error(request, 'You have successfully paid!')

                for id, pledge in cart.items():
                    ticket = get_object_or_404(Ticket, pk=id)
                    ticket.value += pledge
                    ticket.lastUpdatedBy = request.user.username
                    ticket.lastUpdatedDateTime = timezone.now()
                    ticket.save()

                request.session['cart'] = {}
                return redirect(reverse('tracker', args=['all', 'dateTimeCreated', 1]))
            else:
                messages.error(request, 'Unable to take payment!')
        
        else:
            print(payment_form.errors)
            print(order_form.errors)
            messages.error(request, 'Unable to take payment with that card!')

    else:
        order_form = OrderForm(label_suffix='', initial={
            'full_name': full_name,
            'phone_number': user_profile.phone_number,
            'country': user_profile.country, 
            'county': user_profile.county, 
            'town_or_city': user_profile.town_or_city, 
            'postcode': user_profile.postcode, 
            'street1': user_profile.street1, 
            'street2': user_profile.street2,
        })
        payment_form = MakePaymentForm(label_suffix='')

    return render(request, 'checkout.html', {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE_KEY})
