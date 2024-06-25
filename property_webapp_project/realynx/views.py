from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author": "Oseloka",
        "title": "Notification post 1",
        "content": "First notification content.",
        "date_posted": 'June 25, 2024'
    },
    {
        "author": "jkuffor_",
        "title": "Notification post 2",
        "content": "Second notification content.",
        "date_posted": 'June 25, 2024'
    },
]

def home(request):
    return render(request, "realynx/home.html", {"title":"Home"})

def notice(request):
    context = {
        "posts": posts
    }
    return render(request, "realynx/notice.html", context)