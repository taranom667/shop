from django.urls import path

from .views import *

urlpatterns = [
    path('GET/', ListAddressAPI.as_view()),
    path('POST/', CreateAddressAPI().as_view()),
    path('GET/<int:id>/', GetOneAddressAPI.as_view()),
    path('UPDATE/<int:id>/',UpdateAddressAPI.as_view()),
    path('DELETE/<int:id>/', DeleteAddressAPI.as_view()),
    path('Default/<int:id>/',SetAsDefaultAddressAPI.as_view()),

]