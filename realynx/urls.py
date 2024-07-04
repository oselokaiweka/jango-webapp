from django.urls import path
from .views import (
    NoticeListView,
    NoticeDetailView,
    NoticeCreateView,
    NoticeUpdateView,
    NoticeDeleteView,
    UserNoticeListView,
)
from . import views

urlpatterns = [
    path("", views.home, name="realynx-home"),
    path("notice/", NoticeListView.as_view(), name="realynx-notice"),
    path("notice/<str:username>", UserNoticeListView.as_view(), name="notice-user"),
    path("notice/new/", NoticeCreateView.as_view(), name="notice-create"),
    path("notice/<int:pk>/", NoticeDetailView.as_view(), name="notice-detail"),
    path("notice/<int:pk>/update/", NoticeUpdateView.as_view(), name="notice-update"),
    path("notice/<int:pk>/delete/", NoticeDeleteView.as_view(), name="notice-delete"),
]
