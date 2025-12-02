from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView


class HomePageView(TemplateView):
    template_name = "index.html"


class SearchPageView(TemplateView):
    template_name = "search.html"


class UserLogoutView(LogoutView):
    next_page = "home"


class UserLoginView(LoginView):
    template_name = "login.html"

    def get_success_url(self):
        return reverse_lazy("home")


class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy("login")
