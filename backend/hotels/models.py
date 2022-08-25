from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=25)


class Hotels(models.Model):
    placename = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    hotelname = models.CharField(max_length=50)
    cost = models.FloatField()
    # hello = models.CharField(max_length=15)
    
