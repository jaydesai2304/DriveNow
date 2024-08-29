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
    path("", RegisterView.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),
]
