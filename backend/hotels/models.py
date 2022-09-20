from django.db import models


# Country
class Country(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


# Category
class Category(models.Model):
    name = models.CharField(max_length=25, null=True, blank=True)
    photo = models.ImageField(
        upload_to="categoryImages/", null=True, blank=True)

    def __str__(self):
        return self.name


# Hotels
class Hotels(models.Model):
    placename = models.CharField(max_length=70)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, blank=True, null=True)
    hotelname = models.CharField(max_length=70)
    description = models.TextField()
    cost = models.FloatField()
    photo = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.hotelname
