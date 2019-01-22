from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    time_created = models.DateTimeField(auto_created=True, auto_now_add=True)
    region = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    heart = models.IntegerField(default=0)
    poop = models.IntegerField(default=0)

    def __str__(self):
        return self.title
