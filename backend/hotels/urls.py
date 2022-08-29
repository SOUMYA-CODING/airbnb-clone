from django.urls import path
from . import views

urlpatterns = [
    path('countryList/', views.CountryList),
    path('countryList/<int:pk>/', views.CountryList),
    path('categoryList/', views.CategoryList),
    path('hotelList/', views.HotelList),
    path('hotelList/<int:pk>/', views.HotelList),
    path('hotelList/<int:categoryID>/', views.HotelFilter),
]
