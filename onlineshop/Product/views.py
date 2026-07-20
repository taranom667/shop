from hmac import new

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Product
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend


class GetAllProductsAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'in_stock']
    permission_classes = [AllowAny]

#is admin
class AddProductAPI(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#is admin
class UpdateProductAPI(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

#is admin
class DeleteProductAPI(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


class GetProductAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all() #???????????
    lookup_field = 'id'
    serializer_class = ProductSerializer
    #filter_backends = [DjangoFilterBackend]

'''  
class searchProductAPI(generics.ListAPIView):
    queryset = Product.objects.all() #???????
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]#???????
    filterset_fields = ['category', 'in_stock'] #??????????/
    permission_classes = [AllowAny]'''


#FILTER?????????????????????????????????//
'''
class FilterProductAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'in_stock']
    permission_classes = [AllowAny]
        '''

'''
sort 
new
popular
related'''





