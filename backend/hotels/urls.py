from django.urls import path
from . import views

urlpatterns = [
    path('countryList/', views.CountryList),
    path('countryList/<int:pk>/', views.CountryList),
    path('hotelList/', views.HotelList),
    path('hotelList/<int:pk>', views.HotelList),
]
