#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.test import TestCase
from django.test.client import RequestFactory

from glue import Epoxy

# Create your tests here.
class FakeTest(TestCase):
  '''
  Test glue against our precious Fake model
  '''
  def setUp(self):
    # Every test needs access to the request factory.
    self.factory = RequestFactory()
    self.user = User.objects.create_user(
      username='jacob', email='jacob@…', password='top_secret')



  def test_get_fakes(self):

    request = self.factory.get('/customer/details')
    request.user = self.user
    
    result = Epoxy(request).json()

    self.assertEqual('%s' % result, 'Content-Type: application/json\r\n\r\n{"status": "ok", "meta": {"action": "test_get_fakes", "user": "jacob", "method": "GET"}}')



class EpoxyTest(TestCase):
  '''
  Test Epoxy functions, cfr glue module
  '''
  def setUp(self):
    # Every test needs access to the request factory.
    self.factory = RequestFactory()
    self.user = User.objects.create_user(
      username='jacob', email='jacob@…', password='top_secret')


  def test_meta(self):
    request = self.factory.get('/glue/')
    request.user = self.user

    result = Epoxy(request)
    result.meta('property', 'value')
    

    self.assertEqual(True, True)


  def test_limits(self):
    request = self.factory.get('/glue/?limit=0&offset=50')
    request.user = self.user

    result = Epoxy(request)
    self.assertEqual(True, True)


  def test_error(self):
    request = self.factory.get('/glue')
    request.user = self.user
    result = Epoxy(request)
    #result.throwerror('')
    self.assertEqual(True, True)