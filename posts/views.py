from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView

from mysite.forms import PostForm
from posts.models import Post, Profile, Comment


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


@login_required
def post_new(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            user = request.user
            user_profile = Profile.objects.get(user=user)
            user_region = user_profile.region

            post = form.save(commit=False)
            post.author = user
            post.region = user_region
            post.save()
            return redirect('posts:detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('posts:detail', pk=post.pk)

    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form})


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('posts:list')


@login_required
def comment_add(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        content = request.POST.get('content')

        user = request.user
        user_profile = Profile.objects.get(user=user)

        Comment.objects.create(post=post, author=user, content=content)
        return redirect('posts:detail', pk=pk)


@login_required
def comment_remove(request, pk, pk_comment):
    comment = get_object_or_404(Comment, pk=pk_comment)

    comment.delete()
    return redirect('posts:detail', pk=pk)
