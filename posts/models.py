from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    REGION_CHOICES = (
        ('미국', '미국'),
        ('중국', '중국'),
        ('일본', '일본'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    region = models.CharField(max_length=30, choices=REGION_CHOICES)
    heart = models.IntegerField(default=10)
    poop = models.IntegerField(default=10)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    time_created = models.DateTimeField(auto_created=True, auto_now_add=True)
    region = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    heart = models.IntegerField(default=0)
    poop = models.IntegerField(default=0)
    comment_num = models.IntegerField(default=0)

    def __str__(self):
        return self.title

# class Comment(models.Model):
#     post = models.ForeignKey(Post, related_name=)
#     author =
#     content = models.TextField()
#     comment_id =
