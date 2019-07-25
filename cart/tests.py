from django.test import TestCase, Client
from django.urls import resolve, reverse
from .views import view_cart, add_to_cart, adjust_pledge, delete_ticket
from tickets.models import Ticket
from django.contrib.auth.models import User
from django.utils import timezone

# Create your tests here.
class TestCartUrls(TestCase):

    def test_view_cart_url_resolves_view_cart_view(self):
        path = resolve(reverse('view_cart'))
        self.assertEqual(path.func, view_cart)

    def test_add_to_cart_resolves_add_to_cart_view(self):
        path = resolve(reverse('add_to_cart', args=[1]))
        self.assertAlmostEqual(path.func, add_to_cart)

    def test_adjust_cart_resolves_adjust_cart_view(self):
        path = resolve(reverse('adjust_pledge', args=[1]))
        self.assertAlmostEqual(path.func, adjust_pledge)

    def test_delete_cart_resolves_delete_cart_view(self):
        path = resolve(reverse('delete_ticket', args=[1]))
        self.assertAlmostEqual(path.func, delete_ticket)


class TestCartViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.test_user = User.objects.create(
            username='testUser',
            first_name='Test',
            last_name='User',
            email='test@test.com',
            password='Test12345!'
        )
        self.test_user.save()

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

        self.view_cart_url = reverse('view_cart')
        self.add_to_cart_url = reverse('add_to_cart', args=[1])
        self.adjust_pledge_url = reverse('adjust_pledge', args=[1])
        self.delete_ticket_url = reverse('delete_ticket', args=[1])

    def test_view_cart_GET(self):
        response = self.client.get(self.view_cart_url)
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, 'cart.html')

    def test_add_to_cart_POST_adds_new_ticket_to_cart(self):
        response = self.client.post(self.add_to_cart_url, {'pledge':20})
        id = self.test_ticket.pk
        pledge = 20
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['cart'], {str(id): pledge})

    def test_add_existing_ticket_to_cart_adds_to_current_pledge_on_same_ticket(self):
        response = self.client.post(self.add_to_cart_url, {'pledge':20})
        response = self.client.post(self.add_to_cart_url, {'pledge':20})
        id = self.test_ticket.pk
        pledge = 40
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['cart'], {str(id): pledge})

    def test_adjust_pledge_POST_changes_the_pledge(self):
        response = self.client.post(self.add_to_cart_url, {'pledge':20})
        response = self.client.post(self.adjust_pledge_url, {'pledge': 30})
        id = self.test_ticket.pk
        pledge = 30
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['cart'], {str(id): pledge})

    def test_delete_ticket_removes_ticket_from_cart(self):
        response = self.client.post(self.add_to_cart_url, {'pledge':20})
        response = self.client.get(self.delete_ticket_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['cart'], {})