from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = 'user,receiver_name,receiver_email,postal_code,country ,province,city,street,alley ,plate address,is_default'
