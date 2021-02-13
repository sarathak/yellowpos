# -*- coding: utf-8 -*-

import json

from django.test import Client
from django.test import TestCase
from django.urls import reverse

from products.models import Category


class SimpleTest(TestCase):
    # fixtures = ['system.json', 'staff.json']

    @classmethod
    def setUp(cls):
        pass

    def test_category_list(self):
        client = Client()
        url = reverse('products:category-list', )
        Category.objects.create(name='cat1')
        Category.objects.create(name='cat12')
        response = client.get(url, content_type='application/json', )

        self.assertEqual(response.status_code, 200)
        categories = response.json()
        self.assertEqual(len(categories), 2)

    def test_category_create(self):
        client = Client()
        url = reverse('products:category-list', )
        response = client.post(url,
                               json.dumps({'name': 'cat1',
                                           'tax': '10.5',
                                           'tax_included': True,
                                           }),
                               content_type='application/json', )

        self.assertEqual(response.status_code, 201)
        category = Category.objects.get(name='cat1')
        self.assertEqual(category.tax, 10.5)
        self.assertEqual(category.tax_included, True)

    def test_category_details(self):
        client = Client()
        category = Category.objects.create(name='cat1')
        url = reverse('products:category-detail', args=[category.id])
        response = client.get(url, content_type='application/json', )
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), {'name': 'cat1', 'tax': 0.0, 'tax_included': True})

    def test_category_edit(self):
        client = Client()
        category = Category.objects.create(name='cat1')
        url = reverse('products:category-detail', args=[category.id])
        response = client.put(url, json.dumps({'name': 'cat2',
                                               'tax': '10.5',
                                               'tax_included': True,
                                               }), content_type='application/json', )
        self.assertEqual(response.status_code, 200)
        category.refresh_from_db()
        self.assertEqual(category.name, 'cat2')
        self.assertEqual(category.tax, 10.5)

    def test_category_delete(self):
        client = Client()
        category = Category.objects.create(name='cat1')
        url = reverse('products:category-detail', args=[category.id])
        response = client.delete(url,  content_type='application/json', )
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Category.objects.filter(id=category.id).exists())