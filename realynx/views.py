from django.shortcuts import render

from .models import Post


def home(request):
    return render(request, "realynx/home.html", {"title": "Home"})


def notice(request):
    context = {"posts": Post.objects.all()}
    return render(request, "realynx/notice.html", context)
