from django.shortcuts import render, redirect
from django.contrib import messages
from django.http.request import HttpRequest
from rest_framework import generics
from rest_framework.request import Request
from .serializers import (
    PersonSerializer,
    LoginSerializer,
    ContactSerializers
)
from rest_framework.renderers import TemplateHTMLRenderer
from typing import Union


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def cars(request):
    return render(request, 'cars.html')

def quick_booking(request):
    return render(request, 'quick-booking.html')

def profile(request):
    return render(request, 'account-profile.html')

def dashboard(request):
    return render(request, 'account-dashboard.html')

def orders(request):
    return render(request, 'account-booking.html')

def favorite(request):
    return render(request, 'account-favorite.html')

class RegisterView(generics.CreateAPIView):
    serializer_class = PersonSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "register.html"

    def get(self, request: Union[Request, HttpRequest]) -> Union[render, redirect]:
        if "username" in request.session:
            return redirect("index")
        serializer = PersonSerializer()
        return render(request, self.template_name, {"serializer": serializer})

    def post(self, request: Union[Request, HttpRequest]) -> Union[redirect, render]:
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("login")
        messages.error(request, serializer.errors["non_field_errors"][0])
        return render(request, self.template_name)
    
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        if "username" not in request.session:
            return redirect("index")
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.data.get("username")
            request.session["username"] = user
            return redirect("index")
        messages.error(request, serializer.errors["non_field_errors"][0])
        return render(request, self.template_name, {"serializer": serializer})


class ContactView(generics.CreateAPIView):
    serializer_class = ContactSerializers
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "contact.html"

    def get(self, request):
        if "username" not in request.session:
            return redirect("login")
        serializer = ContactSerializers()
        return render(request, self.template_name, {"serializer": serializer})

    def post(self, request, *args, **kwargs):
        serializer = ContactSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("index")
        return render(request, self.template_name)
    