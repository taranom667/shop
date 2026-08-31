from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend


class GetAllProductsAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'in_stock']
    permission_classes = [AllowAny]


class CreateProductAPI(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]


# is admin
class AddProductAPI(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# is admin
class UpdateProductAPI(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


# is admin
class DeleteProductAPI(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


class GetProductAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()  # ???????????
    lookup_field = 'id'
    serializer_class = ProductSerializer
    # filter_backends = [DjangoFilterBackend]


from rest_framework import filters
from rest_framework.pagination import PageNumberPagination


class ProductListView(GenericAPIView):
    serializer_class = ProductSerializer
    queryset = (
        Product.objects.select_related('category').all())
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'name',
        'category__name',
        'price',
    ]

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            # If pagination is applied, get the paginated response
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # If no pagination, return the full response
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

