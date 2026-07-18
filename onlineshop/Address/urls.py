from django.urls import path

from .views import *

urlpatterns = [
    path('POST/', add_address_api),
    path('DELETE/', DeleteAddressAPI.as_view()),
    path('GET',ListAddressAPI.as_view()),
    path('UPDATE',UpdateAddressAPI.as_view()),

]