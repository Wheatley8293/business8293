from django.db import models


class Infra(models.Model):
    InfraGoo = models.CharField(max_length=20)
    InfraDong = models.CharField(max_length=20)
    InfraWork = models.CharField(max_length=20)
    InfraName = models.CharField(max_length=50)
    Latitude = models.FloatField()
    Longitude = models.FloatField()

# 필요한 형식에 맞춰 클래스 형태로 만들고 자료형 CharField나 IntegerField 등을 지정함.
# 문자열은 max_length를 지정해줘야 하고, 정수나 실수형은 상관없음.
# 이 양식을 만들어두고 makemigrations와 migrate를 하면 데이터에 맞춘 모델을 생성하게 됨.
# 맨 처음엔 빈값들이고, test.py에 있는 방법대로 csv를 데이터베이스에 집어넣었음.

# serializers.py로
