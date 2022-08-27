from rest_framework.decorators import api_view
from rest_framework.response import Response

from . models import Country, Hotels
from . serializer import CountrySerializer, HotelsSerializer


# Country List
@api_view(['GET', 'POST'])
def CountryList(request, pk=None):
    if request.method == "GET":
        id = pk
        if id is not None:
            list = Country.objects.get(id=id)
            serializer = CountrySerializer(list)
            return Response(serializer.data)

        list = Country.objects.all()
        serializer = CountrySerializer(
            list, many=True, context={'request': request})
        return Response(serializer.data)

    if request.method == "POST":
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'MESSAGE': 'Created'})
        return Response(serializer.errors)


# Hotel List
@api_view(['GET', 'POST'])
def HotelList(request, pk=None):
    if request.method == "GET":
        id = pk
        if id is not None:
            list = Hotels.objects.get(id=id)
            serializer = HotelsSerializer(list, context={'request': request})
            return Response(serializer.data)

        list = Hotels.objects.all()
        serializer = HotelsSerializer(
            list, many=True, context={'request': request})
        return Response(serializer.data)

    if request.method == "POST":
        serializer = HotelsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'MESSAGE': 'Created'})
        return Response(serializer.errors)
