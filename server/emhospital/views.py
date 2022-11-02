from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from .serializers import EmHospitalSerializer
from .models import EmHospital

class EmHospitalAPI(APIView):
    def get(self, request):
        emhospitals = EmHospital.objects.all()
        serializer = EmHospitalSerializer(emhospitals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)