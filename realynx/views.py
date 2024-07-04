from django.forms import BaseModelForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Notice


def home(request):
    return render(request, "realynx/home.html", {"title": "Home"})


def notice(request):
    context = {"notices": Notice.objects.all()}
    return render(request, "realynx/notice.html", context)


class NoticeListView(ListView):
    model = Notice
    # <app>/<model>_<viewtype>.html: Default naming convention else specify as:
    template_name = "realynx/notice.html"
    context_object_name = "notices"
    ordering = ["-date_posted"]
    paginate_by = 4


class UserNoticeListView(ListView):
    model = Notice
    # <app>/<model>_<viewtype>.html: Default naming convention else specify as:
    template_name = "realynx/notice_user.html"
    context_object_name = "notices"
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Notice.objects.filter(author=user).order_by("-date_posted")



class NoticeDetailView(DetailView):
    model = Notice


class NoticeCreateView(LoginRequiredMixin, CreateView):
    model = Notice
    fields = ["title", "content"]

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)


class NoticeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Notice
    fields = ["title", "content"]

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self) -> bool | None:
        notice = self.get_object()
        if self.request.user == notice.author:
            return True
        return False


class NoticeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Notice
    success_url = "/notice/"

    def test_func(self) -> bool | None:
        notice = self.get_object()
        if self.request.user == notice.author:
            return True
        return False
