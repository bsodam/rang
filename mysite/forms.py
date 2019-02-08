from betterforms.multiform import MultiModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm

from posts.models import Profile, Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'content',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['region',]


class UserCreationMultiForm(MultiModelForm):
    form_classes = {
        'user' : UserCreationForm,
        'profile' : ProfileForm,
    }
