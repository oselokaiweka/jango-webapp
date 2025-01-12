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
    path("", views.home, name="home"),
    path("notice/", NoticeListView.as_view(), name="notice"),
    path("notice/new/", NoticeCreateView.as_view(), name="notice_create"),
    path("notice/<int:pk>/", NoticeDetailView.as_view(), name="notice_detail"),
    path("notice/<str:username>/", UserNoticeListView.as_view(), name="notice_user"),
    path("notice/<int:pk>/update/", NoticeUpdateView.as_view(), name="notice_update"),
    path("notice/<int:pk>/delete/", NoticeDeleteView.as_view(), name="notice_delete"),
]
