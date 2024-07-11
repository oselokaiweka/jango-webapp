import pytest
from django.urls import reverse
from django.db import connections
from django.db.utils import OperationalError


@pytest.mark.django_db
def test_home(client):
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200
    assert response.templates[0].name == 'realynx/home.html'

@pytest.mark.django_db
def test_notice(client):
    url = reverse("notice")
    response = client.get(url)
    assert response.status_code == 200
    assert response.templates[0].name == 'realynx/notice.html'

