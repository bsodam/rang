from betterforms.multiform import MultiModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm

from posts.models import Profile


# class RegionInput(forms.CharField):
#     input_type =

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['region',]
        # widgets = {
        #     'region': RegionInput(),
        # }


class UserCreationMultiForm(MultiModelForm):
    form_classes = {
        'user' : UserCreationForm,
        'profile' : ProfileForm,
    }
