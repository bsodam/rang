from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView

from mysite.forms import UserCreationMultiForm


class HomeView(TemplateView):
    template_name = "index.html"


class UserCreateView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationMultiForm
    success_url = '/registered'

    def form_valid(self, form):
        user = form['user'].save()
        profile = form['profile'].save(commit=False)
        profile.user = user
        profile.save()
        return redirect(self.success_url)


class RegisterdView(TemplateView):
    template_name = 'registration/registered.html'
