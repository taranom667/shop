from django.urls import path
from .views import *

urlpatterns = [
    path('POST/',AddProductAPI.as_view()),
    path('GET/',GetProductAPI.as_view()),
    path('DELETE/',DeleteProductAPI.as_view()),
    path('PUT/',UpdateProductAPI.as_view()),



]