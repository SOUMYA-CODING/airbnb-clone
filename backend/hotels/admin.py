from django.contrib import admin
from . models import Country, Category, Hotels
# Register your models here.


# Country Admin
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('-id',)


# Country Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('-id',)


# Country Admin
class HotelsAdmin(admin.ModelAdmin):
    list_display = ('id', 'placename', 'country', 'category',
                    'hotelname', 'description', 'cost', 'photo')
    ordering = ('category',)


admin.site.register(Country, CountryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Hotels, HotelsAdmin)
