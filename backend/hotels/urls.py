from django.urls import path
from . import views

urlpatterns = [
    path('countryList/', views.CountryList.as_view()),
    path('hotelList/', views.HotelList.as_view()),
]
