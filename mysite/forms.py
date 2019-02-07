from betterforms.multiform import MultiModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm

from posts.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['region',]


class UserCreationMultiForm(MultiModelForm):
    form_classes = {
        'user' : UserCreationForm,
        'profile' : ProfileForm,
    }
