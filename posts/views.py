from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView

from mysite.forms import PostForm
from posts.models import Post, Profile, Comment, CommentOnComment


class ListView(ListView):
    template_name = 'posts/list_all.html'
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
    template_name = 'posts/list_all.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        search_keyword = self.request.GET.get('search_keyword', '')
        return Post.objects.filter(title__contains=search_keyword)


@login_required
def list_local(request):
    user = request.user
    user_profile = Profile.objects.get(user=user)
    user_region = user_profile.region

    regional_post_list = Post.objects.filter(region=user_region)

    return render(request, 'posts/list_local.html', {'region': user_region, 'post_list': regional_post_list})


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
    return redirect('posts:list_local')


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


@login_required
def comment_on_comment(request, pk, pk_comment):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, pk=pk_comment)
        content = request.POST.get('content')

        user = request.user

        CommentOnComment.objects.create(comment=comment, author=user, content=content)
        return redirect('posts:detail', pk=pk)


@login_required
def comment_on_comment_remove(request, pk, pk_comment_on_comment):
    comment_on_comment = get_object_or_404(CommentOnComment, pk=pk_comment_on_comment)

    comment_on_comment.delete()
    return redirect('posts:detail', pk=pk)


@login_required
def add_heart(request, pk):
    user = request.user
    user_profile = Profile.objects.get(user=user)
    user_heart = user_profile.heart
    post = get_object_or_404(Post, pk=pk)

    if user_heart == 0:
        pass

    post.add_heart()

    return redirect('posts:detail', pk=pk)


@login_required
def add_poop(request, pk):
    user = request.user
    user_profile = Profile.objects.get(user=user)
    user_poop = user_profile.poop
    post = get_object_or_404(Post, pk=pk)

    if user_poop == 0:
        pass

    post.add_poop()

    return redirect('posts:detail', pk=pk)
