import django.test
import parameterized
import catalog.models
import django.core.exceptions

# Create your tests here.
class StaticURLTests(django.test.TestCase):
    def test_catalog_endpoint(self):
        response = django.test.Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    @parameterized.parameterized.expand(
        [
            # ('1', 200),
            # ('200', 200),
            # ('0', 200),
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
        response = django.test.Client().get(f'/catalog/{url}/')
        self.assertEqual(response.status_code, expected_status,
                         f'in catalog/{url}/ expected status_code: {expected_status} but given is {response.status_code}')


class ModelsTests(django.test.TestCase):
    def setUp(self):
        self.category = catalog.models.Category.objects.create(
            name='test category',
            slug='test-category',
        )
        self.tag = catalog.models.Tag.objects.create(
            name='test tag',
            slug='test_tag',
        )
        super(ModelsTests, self).setUp()

    def tearDown(self):
        catalog.models.Item.objects.all().delete()
        catalog.models.Tag.objects.all().delete()
        catalog.models.Category.objects.all().delete()

        super(ModelsTests, self).tearDown()

    @parameterized.parameterized.expand(
        [
            ('Превосходно',),
            ('роскошно',),
            ('роскошно!',),
            ('роскошно`',),
            ('!роскошно и превосходно',),
            ('не роскошно',),
        ]
    )
    def test_item_text_validator(self, text):
        item_counts = catalog.models.Item.objects.count()

        item = catalog.models.Item(
            name='Тестовый товар',
            text=text,
            category=self.category,
        )
        item.full_clean()
        item.save()
        item.tags.add(self.tag)

        self.assertEqual(
            catalog.models.Item.objects.count(),
            item_counts + 1,
        )

    @parameterized.parameterized.expand(
        [
            ('Преврсходно', ),
            ('Привосходно', ),
            ('ПреВосх0дно', ),
            ('Роск!шно', ),
        ]
    )
    def test_negative_text_validator(self, text):
        item_counts = catalog.models.Item.objects.count()

        with self.assertRaises(django.core.exceptions.ValidationError):
            item = catalog.models.Item(
                name='тестовый товарчик',
                text=text,
                category=self.category,
            )
            item.full_clean()
            item.save()
            item.tags.add(self.tag)
            self.assertEqual(
                catalog.models.Item.objects.count(),
                item_counts,
            )