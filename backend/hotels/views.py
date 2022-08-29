from rest_framework.decorators import api_view
from rest_framework.response import Response

from . models import Country, Category, Hotels
from . serializer import CountrySerializer, CategorySerializer, HotelsSerializer


# Country List
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def CountryList(request, pk=None):
    # Get the ID
    id = pk

    # GET
    if request.method == "GET":
        if id is not None:
            list = Country.objects.get(id=id)
            serializer = CountrySerializer(list)
            return Response(serializer.data)

        list = Country.objects.all()
        serializer = CountrySerializer(
            list, many=True, context={'request': request})
        return Response(serializer.data)

    # POST
    if request.method == "POST":
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'MESSAGE': 'Created'})
        return Response(serializer.errors)

    # PUT
    if request.method == "PUT":
        updateData = Country.objects.get(id=id)
        serializer = CountrySerializer(
            updateData, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'MESSAGE': 'Data Updated'})
        return Response(serializer.errors)

    # DELETE
    if request.method == "DELETE":
        data = Country.objects.get(id=id)
        data.delete()
        return Response({'MESSAGE': 'Data Deleted'})


# Category
@api_view(['GET'])
def CategoryList(request):
    if request.method == "GET":
        list = Category.objects.all()
        serializer = CategorySerializer(list, many=True)
        return Response(serializer.data)


# Hotel List
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def HotelList(request, pk=None):
    # Get the ID
    id = pk

    # GET
    if request.method == "GET":
        if id is not None:
            list = Hotels.objects.get(id=id)
            serializer = HotelsSerializer(list, context={'request': request})
            return Response(serializer.data)

        list = Hotels.objects.all()
        serializer = HotelsSerializer(
            list, many=True, context={'request': request})
        return Response(serializer.data)

    # POST
    if request.method == "POST":
        serializer = HotelsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'MESSAGE': 'Created'})
        return Response(serializer.errors)

    # PUT
    if request.method == "PUT":
        updateData = Hotels.objects.get(id=id)
        serializer = HotelsSerializer(
            updateData, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'MESSAGE': 'Data Updated'})
        return Response(serializer.errors)

    # DELETE
    if request.method == "DELETE":
        data = Hotels.objects.get(id=id)
        data.delete()
        return Response({'MESSAGE': 'Data Deleted'})


# Hotel Filter
@api_view(['GET'])
def HotelCategoryFilter(request, categoryID):
    catID = categoryID
    if catID is not None:
        list = Hotels.objects.filter(category=catID)
        serializer = HotelsSerializer(
            list, many=True, context={'request': request})
        return Response(serializer.data)
    return Response({'msg': 'No data found'})


# Country Filter
@api_view(['GET'])
def HotelCountryFilter(request, countryID):
    contID = countryID
    if contID is not None:
        list = Hotels.objects.filter(country=contID)
        serializer = HotelsSerializer(
            list, many=True, context={'request': request})
        return Response(serializer.data)
    return Response({'msg': 'No data found'})
