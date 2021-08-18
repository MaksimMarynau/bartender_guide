from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ingredients.models import Category, Ingredient


class IngredientsTests(APITestCase):

    def setUp(self):
        Category.objects.create(title_c='Jin',)
        Category.objects.create(title_c='Whisky',)

    def test_category_list(self):
        response = self.client.get(reverse('category-list'))
        print(response.data.results)
        self.assertEqual(response.data,{'id': 1, 'title_c': 'Python'})
