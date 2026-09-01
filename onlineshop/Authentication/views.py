from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status, generics, request
from .serializers import RegisterUserSerializer
from Cart.models import Cart
from Wishlist.models import Wishlist

class RegisterUserAPI(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    user=serializer_class
    permission_classes = (AllowAny,)

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)



