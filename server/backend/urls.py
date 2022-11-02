"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from park.views import ParkAPI
from emhospital.views import EmHospitalAPI
urlpatterns = [
    path('admin/', admin.site.urls),
    path('infra/', include('infra.urls')),
    path('park/', ParkAPI.as_view()),
    path('emhospital/', EmHospitalAPI.as_view()),
]

# 기본적으로 admin이 존재하고, 만든 앱의 이름으로 된 URL로 접속할 때 실행할 API(as_view 형식)를 적어주는 것.
# 또한 infra는 나머지 2개와 다르게 더 세세하게 URL이 뻗어나가기에, include를 통해 infra.urls을 읽어들이는 것.
# 또한 API를 실행하도록 지시를 하기에, 그 API를 위에서 먼저 임포트해주는 것.
# 또한 코드의 중복적 사용, infra 앱에서 묶어 설명하겠음. (infra-url로~)
