from django.db import models

class Park(models.Model):
    ParkGoo = models.CharField(max_length=20)
    ParkDong = models.CharField(max_length=20)
    ParkName = models.CharField(max_length=50)
    ParkType = models.CharField(max_length=20)
    ParkAddress = models.CharField(max_length=50)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    ParkArea = models.IntegerField()
    AreaPart = models.IntegerField()
