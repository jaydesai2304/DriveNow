from django.shortcuts import render, redirect
from django.contrib import messages
from django.http.request import HttpRequest
from rest_framework import generics
from rest_framework.request import Request
from .serializers import (
    PersonSerializer,
    Loginserializer
)
from rest_framework.renderers import TemplateHTMLRenderer
from typing import Union


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

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
    
class LoginView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Loginserializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "login.html"

    def get(self, request: Union[Request, HttpRequest]) -> Union[render, redirect]:
        if "username" in request.session:
            return redirect("index")
        return render(request, self.template_name)

    def post(self, request: Union[Request, HttpRequest]) -> Union[render, redirect]:
        serializer = Loginserializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get("username")
            request.session["username"] = username
            return redirect("index")
        messages.error(request, serializer.errors["non_field_errors"][0])
        return render(request, self.template_name)
