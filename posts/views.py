from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView

from posts.models import Post


class ListView(ListView):
    template_name = 'posts/list.html'
    context_object_name = 'post_list'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.order_by('-time_created')


class DetailView(DetailView):
    model = Post


class CreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = '/post/list/all'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SearchResultListView(ListView):
    template_name = 'posts/list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        search_keyword = self.request.GET.get('search_keyword', '')
        return Post.objects.filter(title__contains=search_keyword)

