import pytest
from django import urls
from django.core import mail
from django.contrib.auth import get_user_model
from users.forms import UserUpdateForm, ProfileUpdateForm


@pytest.mark.django_db
def test_invalid_signup_form(client, invalid_user_data):
    user_model = get_user_model()
    signup_url = urls.reverse("signup")
    response = client.post(signup_url, invalid_user_data)
    assert user_model.objects.count() == 0
    assert response.status_code == 200
    assert "Required." in response.content.decode()
    assert "The password you provided is invalid." in response.content.decode()


@pytest.mark.django_db
def test_signup(client, user_data):
    user_model = get_user_model()
    signup_url = urls.reverse("signup")
    response = client.post(signup_url, data=user_data)
    assert user_model.objects.count() == 1
    assert response.status_code == 302


@pytest.mark.django_db
def test_user_login(client, create_test_user):
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    login_url = urls.reverse("login")
    credentials = {"username": create_test_user.username, "password": "dummy_pass123"}
    response = client.post(login_url, credentials)
    assert response.status_code == 302
    assert response.url == urls.reverse("home")


@pytest.mark.django_db
def test_user_logout(client, logged_in_user):
    logout_url = urls.reverse("logout")
    response = client.post(logout_url)
    assert response.status_code == 200
    assert "Sign out successful." in response.content.decode()
    assert "_auth_user_id" not in client.session


@pytest.mark.django_db
def test_profile_logged_out(client):
    profile_url = urls.reverse("profile")
    response = client.get(profile_url)
    assert response.status_code == 302
    assert response.url == f"{urls.reverse('login')}?next={urls.reverse('profile')}"


@pytest.mark.django_db
def test_profile_Logged_in(client, logged_in_user):
    profile_url = urls.reverse("profile")
    response = client.get(profile_url)
    assert response.status_code == 200
    assert response.templates[0].name == "users/profile.html"
    assert isinstance(response.context["profile_form"], ProfileUpdateForm)


@pytest.mark.django_db
def test_profile_update(client, logged_in_user, test_image, temp_media_root):
    profile = logged_in_user.profile

    update_data = {
        "username": "test_username",
        "email": "update_email@example.com",
        "first_name": "update_instagram",
        "last_name": "update_jkuffor_",
    }

    u_form = UserUpdateForm(instance=logged_in_user, data=update_data)
    p_form = ProfileUpdateForm(instance=profile, files={"image": test_image})
    assert u_form.is_valid and p_form.is_valid()
    u_form.save()
    p_form.save()

    # Reload the profile from the database to get updates
    profile.refresh_from_db()
    logged_in_user.refresh_from_db()

    profile_url = urls.reverse("profile")
    context = {"u_form": u_form, "p_form": p_form}
    response = client.post(profile_url, context)

    assert response.status_code == 200
    assert logged_in_user.profile.image.width <= 300
    assert logged_in_user.profile.image.height <= 300
    assert logged_in_user.username == "test_username"
    assert logged_in_user.first_name == "update_instagram"
    assert logged_in_user.email == "update_email@example.com"


@pytest.mark.django_db
def test_password_reset_view(client, create_test_user):
    password_reset_url = urls.reverse("password_reset")
    response = client.get(password_reset_url)
    assert response.status_code == 200
    assert response.templates[0].name == "users/password_reset.html"


@pytest.mark.django_db
def test_password_reset_done(client, create_test_user):
    password_reset_url = urls.reverse("password_reset")
    response = client.post(password_reset_url, {"email": "reset@example.com"})
    assert len(mail.outbox) == 1
