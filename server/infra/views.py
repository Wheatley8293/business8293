from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from .serializers import InfraSerializer
from .models import Infra


class InfraBeautyAPI(APIView):
    def get(self, request):
        InfraBeauty = Infra.objects.filter(InfraWork='애견미용')
        serializer = InfraSerializer(InfraBeauty, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class InfraHospitalAPI(APIView):
    def get(self, request):
        InfraHospital = Infra.objects.filter(InfraWork='동물병원')
        serializer = InfraSerializer(InfraHospital, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class InfraTaxiAPI(APIView):
    def get(self, request):
        InfraTaxi = Infra.objects.filter(InfraWork='펫택시')
        serializer = InfraSerializer(InfraTaxi, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class InfraHotelAPI(APIView):
    def get(self, request):
        InfraBeauty = Infra.objects.filter(InfraWork='펫호텔')
        serializer = InfraSerializer(InfraBeauty, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class InfraCafeAPI(APIView):
    def get(self, request):
        InfraCafe = Infra.objects.filter(InfraWork='펫카페')
        serializer = InfraSerializer(InfraCafe, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 임포트 부분의 rest_framework 부분은 필수 혹은 용도에 따라 이용하게 됨. 클론코딩.

# APi를 호출하게 되면, def 뒤엔 요청 이름에 따른 함수를 정의해줌.
# get 함수를 활용했기에 def get이 되었고, request는 서버가 요청을 받았다는 뜻.
# 그 응답Response로 serializer로 변환한 데이터와, 응답 코드를 보내준다는 것. 이게 기본적인 형태.

# 그러니까 데이터를 변환할 시리얼라이저, 데이터가 담긴 모델, 둘을 임포트해야함.
# from .serializers import InfraSerializer
# from .models import Infra


# class ParkAPI(APIView):
#     def get(Self, request):
#         parks = Park.objects.all()
#         serializer = ParkSerializer(parks, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# 조건을 따로 걸지 않는다면, 위의 형태로 데이터모델 이름인 Park(오브젝트)(모델) 데이터를 다 가져온다는 뜻.
# parks = Park.objects.all()

# 이 페이지인 infra에선, Infra.objects.filter를 걸어서, 데이터 모델과 일치하는 양식으로 원하는 데이터 조건을 입력함.
# 이걸 ORM 방식이라고 할 수 있음.

# 이제 그 데이터를 임시로 만든 변수에 우선 담아놓음.
# InfraCafe = Infra.objects.filter(InfraWork='펫카페')

# 그럼 그 데이터를 임포트한 시리얼라이저의 매개변수로 보내서 실행시키고 그 결과를 임시변수 serializer에 담음.
# serializer = InfraSerializer(InfraCafe, many=True)
# 그리고 시리얼라이저가 변환시킨 JSON 형태의 값이 .data에 담기게 되니, serializer.data를 응답으로 보내주는 것.

# 일단 infra-model로.
