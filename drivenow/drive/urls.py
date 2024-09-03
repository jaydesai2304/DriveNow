from django.contrib import admin
from django.urls import path
from .views import (
    RegisterView,
    LoginView
)
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("index/", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

    path("", RegisterView.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),

]
