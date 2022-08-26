from rest_framework.generics import ListAPIView

from . models import Country, Hotels
from . serializer import CountrySerializer, HotelsSerializer


class CountryList(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class HotelList(ListAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelsSerializer
