import pytest
from django.urls import reverse
from django.db import connections
from django.db.utils import OperationalError


@pytest.mark.django_db
def test_home(client):
    url = reverse('realynx-home')
    response = client.get(url)
    assert response.status_code == 200