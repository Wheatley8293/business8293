from django.urls import path, include
from .views import InfraHospitalAPI
from .views import InfraBeautyAPI
from .views import InfraTaxiAPI
from .views import InfraCafeAPI
from .views import InfraHotelAPI

urlpatterns = [
    path('hospital/', InfraHospitalAPI.as_view()),
    path('beauty/', InfraBeautyAPI.as_view()),
    path('taxi/', InfraTaxiAPI.as_view()),
    path('cafe/', InfraCafeAPI.as_view()),
    path('hotel/', InfraHotelAPI.as_view()),
]

# :8000/park와 emhospital은 바로 api를 실행하지만, infra는 편의시설별 페이지를 따로 나눠 한번 더 거쳐야 함.
# 그렇기에 localhost:8000/infra/
# 지금 위 경로에 있는 것.

# 이 상태에서 localhost:8000/infra/hospital 로 접속하면 InfraHospitalAPI.as_view()를 실행하도록 하는 것.
# API가 함수형태가 아닌 클래스 형태이기에 as_view() 형태인 것. 교재 참고.
# 또한 API를 실행하도록 하기에 .views에 작성한 API를 임포트하는 것.
# -> views로.
