import datetime
import json
import uuid
from django.utils.timezone import make_aware
from django.test import Client, TestCase

from project1.foo.models import Foo

class FooTestCase(TestCase):

    def test_something(self):
        self.assertTrue(True)