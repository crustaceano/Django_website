from django.test import TestCase, Client
import parameterized


# Create your tests here.
class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    @parameterized.parameterized.expand(
        [
            ('1', 200),
            ('200', 200),
            ('0', 200),
            ('-0', 404),
            ('-400', 404),
            ('0.5', 404),
            ('abd', 404),
            ('0abd', 404),
            ('abc0', 404),
            ('something', 404),
            ('1e5', 404),
        ]
    )
    def test_catalog_item_endpoint(self, url, expected_status):
        response = Client().get(f'/catalog/{url}/')
        self.assertEqual(response.status_code, expected_status, f'in catalog/{url}/ expected status_code: {expected_status} but given is {response.status_code}')

# class ModelsTests(django.test.TestCase):
#     def setUP(self):
#         self.category = catalog.models.Category.o
