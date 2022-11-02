from rest_framework import serializers
from .models import Infra


class InfraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infra
        fields = ['InfraGoo', 'InfraDong', 'InfraWork',
                  'InfraName', 'Latitude', 'Longitude']


# rest_framework에서 serializers를 사용하기 위해 임포트하고, 모델의 데이터양식을 활용하기 위해 임포트함.

# 그리고 매우 간단한 방법으로 시리얼라이저를 만듬.
# 풀어서 쓰면 매우 복잡함.

# class Meta: 안에, model = (임포트한 모델인)Infra를 입력하고,
# 임포트한 Infra의 필드를 알맞게 fields = 의 목록에 적어주면 됨. 알아서 변환시켜줌. 끝.
