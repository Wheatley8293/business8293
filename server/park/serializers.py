from rest_framework import serializers
from .models import Park

class ParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Park
        fields = ['ParkGoo', 'ParkDong', 'ParkName', 'ParkType', 'ParkAddress', 'Latitude', 'Longitude', 'ParkArea', 'AreaPart']
