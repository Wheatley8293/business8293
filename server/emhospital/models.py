from django.db import models

class EmHospital(models.Model):
    HosGoo = models.CharField(max_length=20)
    HosDong = models.CharField(max_length=20)
    HosName = models.CharField(max_length=50)
    AlwaysTime = models.IntegerField()
    HosAddress = models.CharField(max_length=50)
    HosSNA = models.CharField(max_length=50)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
