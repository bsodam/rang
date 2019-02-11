from django.contrib import admin

# Register your models here.
from posts.models import Post, Profile, Comment, CommentOnComment

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(CommentOnComment)
