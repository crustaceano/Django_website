from django.test import TestCase, Client


# Create your tests here.
class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client.get('/')
        self.assertEqual(response.status_code, 200)
