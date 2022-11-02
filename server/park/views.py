from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from .serializers import ParkSerializer
from .models import Park

class ParkAPI(APIView):
    def get(Self, request):
        parks = Park.objects.all()
        serializer = ParkSerializer(parks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)