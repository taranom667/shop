from django.shortcuts import render
from django.template.context_processors import request
from django.views import View
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterUserSerializer


class RegisterUserAPI(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = (AllowAny,)


