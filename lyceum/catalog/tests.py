from django.test import TestCase, Client


# Create your tests here.
class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_catalog__negative_item_description_negative_nums(self):
        response = Client().get('/catalog/-123/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_item_description_positive_nums(self):
        response = Client().get('/catalog/1231231231241/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_negative_string_id(self):
        response = Client().get('/catalog/12mamasd12312/')
        self.assertEqual(response.status_code, 404)
