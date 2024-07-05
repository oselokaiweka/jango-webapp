import pytest
from django.urls import reverse

@pytest.fixture
def user_setup():
    user_data = {
        'username' : 'testuser',
        'email' : 'test@email.com',
        'password1' : 'testpassword',
        'password2' : 'testpassword'
    }
    yield user_data




@pytest.mark.django_db
def test_signup_user(user_setup, client):
    url = reverse("users-signup")
    response = client.post(url, data=user_setup, format='text/html')
    assert response.status_code == 302