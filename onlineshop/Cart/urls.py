from django.urls import path
from .views import CreateCartApi, GetCartApi

urlpatterns = [
    path('', GetCartApi.as_view(), name='get-cart'),
    path('create/', CreateCartApi.as_view(), name='create-cart'),
]