from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'

    REGION_CHOICES = (
        ('미국', '미국'),
        ('중국', '중국'),
        ('일본', '일본'),
        ('캐나다', '캐나다'),
        ('호주', '호주'),
        ('러시아', '러시아'),
        ('베트남', '베트남'),
        ('필리핀', '필리핀'),
        ('브라질', '브라질'),
        ('독일', '독일'),
        ('영국', '영국'),
        ('뉴질랜드', '뉴질랜드'),
        ('인도네시아', '인도네시아'),
        ('아르헨티나', '아르헨티나'),
        ('태국', '태국'),
        ('싱가포르', '싱가포르'),
        ('프랑스', '프랑스'),
        ('말레이시아', '말레이시아'),
        ('멕시코', '멕시코'),
        ('아랍에미리트', '아랍에미리트'),
        ('인도', '인도'),
        ('사우디아라비아', '사우디아라비아'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # nickname = models.CharField(max_length=30)
    region = models.CharField(max_length=30, choices=REGION_CHOICES)
    heart = models.IntegerField(default=10)
    poop = models.IntegerField(default=10)

    def sub_heart(self):
        self.heart -= 1
        self.save()

    def sub_poop(self):
        self.poop -= 1
        self.save()

    def refill_heart(self):
        self.heart = 10
        self.save()

    def refill_poop(self):
        self.poop = 10
        self.save()


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    time_created = models.DateTimeField(auto_created=True, auto_now_add=True)
    region = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    heart = models.IntegerField(default=0)
    poop = models.IntegerField(default=0)
    comment_num = models.IntegerField(default=0)

    class Meta:
        ordering = ['-time_created']

    def __str__(self):
        return self.title

    def add_heart(self):
        self.heart += 1
        self.save()

    def add_poop(self):
        self.poop += 1
        self.save()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent = models.IntegerField(default=None, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()


class CommentOnComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_on_comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
