from django.contrib import admin

from .model_restaurant import Restaurant,OpeningHour,Dish

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'tel', 'address', 'imageUrl')

@admin.register(OpeningHour)
class OpeningHourAdmin(admin.ModelAdmin):
    list_display = ('opening', 'closing', 'day')

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'imageUrl', 'description')
