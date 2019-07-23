from django.test import TestCase, Client
from django.urls import resolve, reverse
from .views import get_json_data, dashboard

# Create your tests here.
class TestAnalyticsUrls(TestCase):
    """
    Test the URLs for the analytics app
    """

    def test_dashboard_url_resolves_to_dashboard_view(self):
        path = resolve(reverse('dashboard'))
        self.assertEqual(path.func, dashboard)

    def test_get_data_url_resolves_to_get_json_data_view(self):
        path = resolve(reverse('get_json_data'))
        self.assertEqual(path.func, get_json_data)


class TestAnalyticsViews(TestCase):
    """
    Test the views for the analytics app
    """
    def setUp(self):
        self.client = Client()
        self.dashboard_url = reverse('dashboard')
        self.get_json_data_url = reverse('get_json_data')


    def test_dashboard_GET(self):
        response = self.client.get(self.dashboard_url)
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, 'dashboard.html')

    def test_get_json_data_GET(self):
        response = self.client.get(self.get_json_data_url)
        self.assertEqual(response.status_code, 200)