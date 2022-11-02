from rest_framework import serializers
from .models import EmHospital

class EmHospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmHospital
        fields = ['HosGoo', 'HosDong', 'HosName', 'AlwaysTime', 'HosAddress', 'HosSNA', 'Latitude', 'Longitude']
