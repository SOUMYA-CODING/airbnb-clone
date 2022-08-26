from django.db import models


# Country
class Country(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


# Hotels
class Hotels(models.Model):
    placename = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    hotelname = models.CharField(max_length=50)
    cost = models.FloatField()
    photo = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name

