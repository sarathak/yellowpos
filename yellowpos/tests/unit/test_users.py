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

    # def test_login(self):
    #     user = User.objects.get(username='owner')
    #     client = Client()
    #     url_login = reverse('staffapi:login', )
    #     url_info = reverse('staffapi:user_info', )
    #     print('login with wrong password')
    #     response = client.post(url_login, json.dumps({'username': 'owner', 'password': '123123s'}),
    #                            content_type='application/json', )
    #     self.assertEqual(response.status_code, 406)
    #     user.is_active = False
    #     user.save()
    #     response = client.post(url_login, json.dumps({'username': 'owner', 'password': '123123'}),
    #                            content_type='application/json', )
    #     self.assertEqual(response.status_code, 406)
    #     # testing correct login
    #     user.is_active = True
    #     user.save()
    #     response = client.post(url_login, json.dumps({'username': 'owner', 'password': '123123'}),
    #                            content_type='application/json', )
    #     self.assertEqual(response.status_code, 200)
    #     # testing not staff
    #     user.is_staff = False
    #     user.save()
    #     response = client.post(url_login, json.dumps({'username': 'owner', 'password': '123123'}),
    #                            content_type='application/json', )
    #     self.assertEqual(response.status_code, 406)
    #
    #     user.is_staff = True
    #     user.save()
    #     # login with email
    #     response = client.post(url_login, json.dumps({'username': 'owner@siteano.com', 'password': '123123'}),
    #                            content_type='application/json', )
    #     self.assertEqual(response.status_code, 200)
    #     # login not owner
    #
    #     response = client.post(url_login, json.dumps({'username': 'manager', 'password': '123123'}),
    #                            content_type='application/json', )
    #     self.assertEqual(response.status_code, 406)
    #
    #     response = client.post(url_login,
    #                            json.dumps({'username': 'manager', 'password': '123123', 'shop_number': 1001}),
    #                            content_type='application/json', )
    #     print(response.data, 'login not owner')
    #     self.assertEqual(response.status_code, 200)
    #     # testing user info
    #     self.login(client, username='owner')
    #     response = client.get(url_info, content_type='application/json', )
    #     doc = response.data
    #     self.assertEqual(user.username, doc['user']['username'])

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
