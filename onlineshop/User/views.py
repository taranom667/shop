from django.shortcuts import render
from django.views import View
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterUserSerializer


# Create your views here.
class RegisterUserAPI(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = (AllowAny,)