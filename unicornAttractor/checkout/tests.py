from django.test import TestCase, Client
from django.urls import resolve, reverse
from .views import checkout
from django.contrib.auth.models import User
from accounts.models import UserProfile
from tickets.models import Ticket
from .models import Order, OrderLineItem
from django.utils import timezone

# Create your tests here.
class TestCheckoutUrls(TestCase):

    def test_checkout_url_resolves_to_checkout_view(self):
        path = resolve(reverse('checkout'))
        self.assertEqual(path.func, checkout)

class TestCheckoutViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.checkout_url = reverse('checkout')
        self.add_to_cart_url = reverse('add_to_cart', args=[1])

        self.test_user = User.objects.create_user('testUser', 'test@test.com', 'testPassword', first_name='Test', last_name='User')
        self.test_user.save()
        self.test_user_profile = UserProfile.objects.create(userID=self.test_user)

        self.test_ticket = Ticket.objects.create(
            pk=1,
            title='test_ticket',
            description='this is a test',
            upvotes=0,
            views=0,
            dateTimeCreated=timezone.now(),
            userID=self.test_user,
            status='in progress',
            lastUpdatedBy='testUser',
            lastUpdatedDateTime=timezone.now(),
            value=0,
            ticket_type='bug'
        )
        self.test_ticket.save()

    def test_checkout_GET_logged_in_returns_200_status_and_checkout_template(self):
        self.client.login(username='testUser', password='testPassword')
        response = self.client.get(self.checkout_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout.html')

    def test_checkout_GET_not_logged_in_returns_302_status(self):
        response = self.client.get(self.checkout_url)
        self.assertEqual(response.status_code, 302)

    def test_checkout_POST_order_is_created_and_cart_is_emptied_and_ticket_value_increased(self):
        self.client.login(username='testUser', password='testPassword')
        response = self.client.post(self.add_to_cart_url, {'pledge':20})
        response = self.client.post(self.checkout_url, {
            'full_name': 'Test Name', 
            'phone_number': '01234567890', 
            'country': 'testCountry', 
            'county': 'testCounty', 
            'town_or_city': 'testTown', 
            'postcode': 'testPostcode', 
            'street1': 'testStreet1', 
            'street2': 'testStreet2',
            'stripe_id': 'tok_visa',
            'credit_card_number': 4242424242424242,
            'cvv': 111,
            'expiry_month': 1,
            'expiry_year': 2022,
        })
        self.assertEqual(Order.objects.get(pk=1).full_name, 'Test Name')
        self.assertEqual(self.client.session['cart'], {})
        self.assertEqual(Ticket.objects.get(pk=1).value, 20)


class TestCheckoutModels(TestCase):

    def setUp(self):
        self.test_user = User.objects.create(
            username='testUser',
            first_name='Test',
            last_name='User',
            email='test@test.com',
            password='Test12345!'
        )
        self.test_user.save()
        self.new_order = Order.objects.create(
            full_name='Test Name', 
            phone_number='01234567890', 
            country='testCountry', 
            county='testCounty', 
            town_or_city='testTown', 
            postcode='testPostcode', 
            street1='testStreet1', 
            street2='testStreet2',
            date_ordered='2019-07-01'
        )
        self.new_order.save()
        self.test_ticket = Ticket.objects.create(
            pk=1,
            title='test_ticket',
            description='this is a test',
            upvotes=0,
            views=0,
            dateTimeCreated=timezone.now(),
            userID=self.test_user,
            status='in progress',
            lastUpdatedBy='testUser',
            lastUpdatedDateTime=timezone.now(),
            value=0,
            ticket_type='bug'
        )
        self.test_ticket.save()
        self.new_order_line_item = OrderLineItem.objects.create(
            order=self.new_order,
            ticket=self.test_ticket,
            pledge=20
        )
        self.new_order_line_item.save()

    def test_order_model_returns_correct_str(self):
        self.assertEqual(str(self.new_order), '1-2019-07-01-Test Name')

    def test_oder_line_item_returns_correct_str(self):
        self.assertEqual(str(self.new_order_line_item), '20 for test_ticket')


