import uuid
from urllib.parse import urljoin

from django.conf import settings
from django.db import models
from django.urls import reverse


class Foo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    