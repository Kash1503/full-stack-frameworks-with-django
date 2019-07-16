from django import forms
from .models import Order

class MakePaymentForm(forms.Form):
    """
    Allow users to input payment information to complete the order
    """

    MONTH_CHOICES = [(i, i) for i in range (1, 12)]
    YEAR_CHOICES = [(i, i) for i in range (2019, 2038)]

    card_number = forms.CharField(label='Card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    """
    Order form made using a model form from the Order model
    """
    class Meta:
        model = Order
        fields = {'full_name', 'phone_number', 'country', 'county', 'town_or_city', 'postcode', 'street1', 'street2'}