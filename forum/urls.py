from django.urls import path

from .views import (
    HomePageView,
    SearchPageView,
    UserLoginView,
    UserLogoutView,
    UserRegisterView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("search/", SearchPageView.as_view(), name="search"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("register/", UserRegisterView.as_view(), name="register"),
]
