# -*- coding: utf-8 -*-

import json

from django.test import Client
from django.test import TestCase
from django.urls import reverse

from users.models import User


class SimpleTest(TestCase):
    # fixtures = ['system.json', 'staff.json']

    @classmethod
    def setUp(cls):
        pass

    def test_login(self):
        user = User(username='test1', last_name='last', first_name='first', email='test@test.com')
        user.set_password('password', )
        user.save()
        client = Client()
        url_login = reverse('users:login', )
        response = client.post(url_login,
                               json.dumps({
                                   'username': 'test1',
                                   'password': 'password',
                               }),
                               content_type='application/json', )  # correct login
        self.assertEqual(response.status_code, 200)
        response = client.post(url_login,
                               json.dumps({
                                   'username': 'test@test.com',
                                   'password': 'password',
                               }),
                               content_type='application/json', )  # correct login with email
        self.assertEqual(response.status_code, 200)
        response = client.post(url_login,
                               json.dumps({
                                   'username': 'test2',
                                   'password': 'password',
                               }),
                               content_type='application/json', )  # wrong username
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(response.json(), {
            'message': 'Please enter a correct username and password. Note that both fields are case-sensitive.'})
        response = client.post(url_login,
                               json.dumps({
                                   'username': 'test1',
                                   'password': 'password2',
                               }),
                               content_type='application/json', )  # test wrong password
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(response.json(), {
            'message': 'Please enter a correct username and password. Note that both fields are case-sensitive.'})

        user.is_active = False
        user.save()
        response = client.post(url_login,
                               json.dumps({
                                   'username': 'test1',
                                   'password': 'password',
                               }),
                               content_type='application/json', )  # test inactive
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(response.json(), {'message': 'This account is inactive.'})

    def test_register(self):
        client = Client()
        url_register = reverse('users:register', )
        response = client.post(url_register,
                               json.dumps({'first_name': 'tester',
                                           'last_name': 'testlast',
                                           'username': 'test1',
                                           'password': 'password',
                                           'email': 'test@test.com',
                                           }),
                               content_type='application/json', )

        self.assertEqual(response.status_code, 200)
        user = User.objects.get(username='test1')
        self.assertEqual(user.first_name, 'tester')
        self.assertEqual(user.last_name, 'testlast')
        self.assertEqual(user.email, 'test@test.com')
        self.assertTrue(user.check_password('password'))
