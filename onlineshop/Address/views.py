from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Address
from .serializers import AddressSerializer

# LIST ADDRESS FOR USER
class ListAddressAPI(generics.ListAPIView):
    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]


# POST
class CreateAddressAPI(generics.CreateAPIView):
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# DELETE
class DeleteAddressAPI(generics.DestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'


# patch
class UpdateAddressAPI(generics.UpdateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'


class GetOneAddressAPI(generics.RetrieveAPIView):
    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'


class SetAsDefaultAddressAPI(generics.RetrieveUpdateAPIView):
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        Address.objects.filter(user=self.request.user).update(default=False)
        serializer.save(default=True)
