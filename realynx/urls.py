from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="realynx-home"),
    path("notice/", views.notice, name="realynx-notice"),
]
