from django.urls import path
from .views import GetOrdersApi, GetOrderApi, CreateOrderApi

urlpatterns = [
    path('', GetOrdersApi.as_view(), name='orders-list'),
    path('<int:id>/', GetOrderApi.as_view(), name='order-detail'),
    path('create/', CreateOrderApi.as_view(), name='create-order'),
]