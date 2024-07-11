import pytest
from django import urls
from django.contrib.auth import get_user_model

"""
@pytest.mark.parametrize('param', [
    ('home'),
    ('notice'),
    ('notice_user'),
])

def test_realynx_views(client, param):
    temp_url = urls.reverse(param) # returns absolute url for each param
    response = client.get(temp_url)
    assert response.status_code == 200
"""