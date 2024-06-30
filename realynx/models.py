from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here


class Post(models.Model):  # Each class will be a different db table
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __self__(self):
        return self.title
