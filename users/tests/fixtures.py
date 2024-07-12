import pytest
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.fixture
def invalid_user_data():
    return {
        "username": "",  # No username
        "email": "invalid_email",
        "password1": "short",
        "password2": "short",
    }


@pytest.fixture
def user_data():
    return {
        "username": "test_username",
        "email": "test_email@example.com",
        "first_name": "instagram",
        "last_name": "jkuffor_",
        "password1": "dummy_pass123",
        "password2": "dummy_pass123",
    }


@pytest.fixture
def create_test_user(user_data):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(
        username=user_data["username"],
        email=user_data["email"],
        password=user_data["password1"],
    )
    return test_user


@pytest.fixture
def logged_in_user(client, create_test_user):
    logged_in_test_user = create_test_user
    client.login(username=logged_in_test_user.username, password="dummy_pass123")
    return logged_in_test_user


@pytest.fixture
def temp_media_root(tmpdir, settings):
    settings.MEDIA_ROOT = tmpdir.strpath
    yield tmpdir


@pytest.fixture
def test_image():
    with open("media_test/IMG_8773.jpg", "rb") as f:
        return SimpleUploadedFile("test_image.jpg", f.read(), content_type="image/jpeg")
