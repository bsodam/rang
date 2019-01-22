from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from posts.models import Post


class ListView(ListView):
    template_name = 'posts/list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.order_by('id')
