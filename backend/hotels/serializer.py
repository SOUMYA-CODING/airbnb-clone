from rest_framework import serializers
from . models import Country, Category, Hotels


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = '__all__'


class HotelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = '__all__'
