from django.contrib import admin
from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    ContactView
)
from django.views.generic import RedirectView
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="index", permanent=False)),
    path("index/", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("cars/", views.cars, name="cars"),
    path("single_car/", views.single_car, name="single_car"),
    path("quick-booking/", views.quick_booking, name="quick-booking"),
    path("profile/", views.profile, name="profile"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("orders/", views.orders, name="orders"),
    path("favorite/", views.favorite, name="favorite"),

    path("register", RegisterView.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("logout", views.logout, name="logout")
]
