import datetime
import json
import uuid
from django.utils.timezone import make_aware
from django.test import Client, TestCase

from project2.bar.models import Bar

class BarTestCase(TestCase):

    def test_something(self):
        self.assertTrue(True)