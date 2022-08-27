from django.urls import path
from . import views

urlpatterns = [
    path('countryList/', views.CountryList),
    path('countryList/<int:id>', views.CountryList),
    path('hotelList/', views.HotelList),
]
