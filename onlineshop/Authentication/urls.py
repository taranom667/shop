from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from Authentication.views import RegisterUserAPI
from .views import LogoutView

urlpatterns = [
    path('login/',jwt_views.TokenObtainPairView.as_view()),
    path('refresh/',jwt_views.TokenRefreshView.as_view()),
    path('register/', RegisterUserAPI.as_view()),
    path('logout',LogoutView.as_view(), name='auth_logout'),
    #path('forgotpassword/',ForgotPasswordApi()),


]


