from django.test import TestCase, Client
from django.urls import resolve, reverse
from .views import tracker, create_ticket, edit_ticket, ticket_details, upvote_comment, upvote_ticket, support_feature
from .models import Ticket, Comments
from django.contrib.auth.models import User
from django.utils import timezone

# Create your tests here.

class TestTicketUrls(TestCase):

    def test_tracker_url_resolves_to_tracker_view(self):
        path = resolve(reverse('tracker', args=['all', 'dateTimeCreated', 1]))
        self.assertEqual(path.func, tracker)

    def test_create_ticket_url_resolves_to_create_ticket_view(self):
        path = resolve(reverse('new_ticket', args=['bug']))
        self.assertEqual(path.func, create_ticket)

    def test_edit_ticket_url_resolves_to_edit_ticket_view(self):
        path = resolve(reverse('edit_ticket', args=[1]))
        self.assertEqual(path.func, edit_ticket)

    def test_ticket_details_url_resolves_to_ticket_details_view(self):
        path = resolve(reverse('ticket_details', args=[1]))
        self.assertEqual(path.func, ticket_details)

    def test_upvote_comment_url_resolves_to_upvote_comment_view(self):
        path = resolve(reverse('upvote_comment', args=[1, 1]))
        self.assertEqual(path.func, upvote_comment)

    def test_upvote_ticket_url_resolves_to_upvote_ticket_view(self):
        path = resolve(reverse('upvote_ticket', args=[1]))
        self.assertEqual(path.func, upvote_ticket)

    def test_support_feature_url_resolves_to_support_feature_view(self):
        path = resolve(reverse('support_feature', args=[1]))
        self.assertEqual(path.func, support_feature)


class TestTicketsModels(TestCase):

    def setUp(self):
        self.test_user = User.objects.create_user('testUser', 'test@test.com', 'testPassword', first_name='Test', last_name='User')
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
        self.test_comment = Comments.objects.create(
            pk=1,
            userID=self.test_user,
            body='this is a test comment',
            upvotes=0,
            ticketID=self.test_ticket,
            dateTimeCreated='2019-07-01'
        )
        self.test_comment.save()

    def test_ticket_model_returns_correct_str(self):
        self.assertEqual(str(self.test_ticket), 'test_ticket')

    def test_comments_model_returns_correct_str(self):
        self.assertEqual(str(self.test_comment), 'ID: 1 - User: testUser - Ticket: 1')


class TestTicketsViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_user('testUser', 'test@test.com', 'testPassword', first_name='Test', last_name='User')
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
        self.test_comment = Comments.objects.create(
            pk=1,
            userID=self.test_user,
            body='this is a test comment',
            upvotes=0,
            ticketID=self.test_ticket,
            dateTimeCreated='2019-07-01'
        )
        self.test_comment.save()

        self.tracker_url = reverse('tracker', args=['bug', 'dateTimeCreated', 1])
        self.create_ticket_url = reverse('new_ticket', args=['bug'])
        self.edit_ticket_url = reverse('edit_ticket', args=[1])
        self.ticket_details_url = reverse('ticket_details', args=[1])


    def test_tracker_GET_returns_200_status_and_tracker_html(self):
        self.client.login(username='testUser', password='testPassword')
        response = self.client.get(self.tracker_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tracker.html')

    def test_tracker_GET_redirects_to_login_if_no_user_logged_in(self):
        response = self.client.get(self.tracker_url)
        self.assertRedirects(response, reverse('account_login'), 302)

    def test_tracker_POST_valid_form_redirects_to_tracker_with_302_code(self):
        self.client.login(username='testUser', password='testPassword')
        response = self.client.post(self.tracker_url, {
            'ticket_type': 'bug',
            'sort_by': 'dateTimeCreated'
        })
        self.assertRedirects(response, reverse('tracker', args=['bug', 'dateTimeCreated', 1]), 302)

    def test_create_ticket_GET_returns_200_code_and_create_ticket_html(self):
        self.client.login(username='testUser', password='testPassword')
        response = self.client.get(self.create_ticket_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create-ticket.html')
    
    def test_create_ticket_POST_valid_form_redirects_tracker_and_new_ticket_created(self):
        self.client.login(username='testUser', password='testPassword')
        response = self.client.post(self.create_ticket_url, {
            'title': 'New Test Ticket',
            'description': 'This is a new Test Ticket',
        })
        self.assertRedirects(response, reverse('tracker', args=['all', 'dateTimeCreated', 1]), 302)
        self.assertEqual(Ticket.objects.get(title='New Test Ticket').description, 'This is a new Test Ticket')

    def test_edit_ticket_GET_returns_200_code_and_edit_ticket_html(self):
        self.client.login(username='testUser', password='testPassword')
        response = self.client.get(self.edit_ticket_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit-ticket.html')
    
    def test_edit_ticket_POST_valid_form_redirects_ticket_details_and_edits_ticket(self):
        self.client.login(username='testUser', password='testPassword')
        response = self.client.post(self.edit_ticket_url, {
            'title': 'test_ticket',
            'description': 'This is the amended description for the ticket',
            'ticket_type': 'feature'
        })
        self.assertRedirects(response, reverse('ticket_details', args=[1]), 302)
        self.assertEqual(Ticket.objects.get(pk=1).description, 'This is the amended description for the ticket')
        self.assertEqual(Ticket.objects.get(pk=1).ticket_type, 'feature')

    def test_ticket_details_GET_returns_200_code_and_ticket_details_html(self):
        self.client.login(username='testUser', password='testPassword')
        response = self.client.get(self.ticket_details_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ticket-details.html')

    def test_ticket_details_GET_adds_to_tickets_views(self):
        self.client.login(username='testUser', password='testPassword')
        response = self.client.get(self.ticket_details_url)
        self.assertEqual(Ticket.objects.get(pk=1).views, 1)
    
    def test_ticket_details_POST_valid_form_renders_ticket_details_html_and_adds_new_comment_to_ticket(self):
        self.client.login(username='testUser', password='testPassword')
        response = self.client.post(self.ticket_details_url, {
            'body': 'Test comment',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ticket-details.html')
        self.assertEqual(Comments.objects.filter(userID__exact=self.test_user).count(), 2)

    def test_upvote_comment_GET_adds_to_comment_upvotes_and_redirects_ticket_details(self):
        self.client.login(username='testUser', password='testPassword')
        response = self.client.get(reverse('upvote_comment', args=[1, 1]))
        self.assertEqual(Comments.objects.get(pk=1).upvotes, 1)
        self.assertRedirects(response, reverse('ticket_details', args=[1]), 302)
    
    def test_upvote_ticket_GET_adds_to_ticket_upvoted_and_redirects_ticket_details(self):
        self.client.login(username='testUser', password='testPassword')
        response = self.client.get(reverse('upvote_ticket', args=[1]))
        self.assertEqual(Ticket.objects.get(pk=1).upvotes, 1)
        self.assertRedirects(response, reverse('ticket_details', args=[1]))
    
    def test_support_feature_GET_returns_200_status_code_and_renders_support_feature_html(self):
        self.client.login(username='testUser', password='testPassword')
        response = self.client.get(reverse('support_feature', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'support-feature.html')