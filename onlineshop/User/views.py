from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import *

class GetUserApi(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.get(id=self.request.user.id)

    serializer_class = UserSerializer

class UpdateUser(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.get(id=self.request.user.id)

    serializer_class = UserSerializer

class DeleteUser(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.get(id=self.request.user.id)

    serializer_class = UserSerializer

class UpdateProfileImage(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
