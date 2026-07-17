from django.urls import path

from .views import ListAddressAPI, UpdateAddressAPI, DeleteAddressAPI, AddAddressAPI

urlpatterns = [
    path('POST/', AddAddressAPI.as_view()),
    path('DELETE/', DeleteAddressAPI.as_view()),
    path('GET',ListAddressAPI.as_view()),
    path('UPDATE',UpdateAddressAPI.as_view()),

]