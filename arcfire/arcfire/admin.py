from django.contrib import admin
from .models import Event, Keyword, Location, Person, Picture, Plan, Place, Property, Card

class CommonAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    list_display = ('name', 'slug')
    list_editable = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Keyword)
class KeywordAdmin(CommonAdmin):
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    fields = ('time', 'latitude', 'longitude', 'altitude', 'position')
    list_display = ('__str__', 'time', 'latitude', 'longitude', 'altitude', 'position')
    list_editable = ('time', 'latitude', 'longitude', 'altitude', 'position')


@admin.register(Property)
class PropertyAdmin(CommonAdmin):
    pass


@admin.register(Picture)
class PictureAdmin(CommonAdmin):
    fields = ('name', 'image', 'width', 'height', 'aspect', 'slug')
    list_display = ('name', 'aspect', 'slug')
    prepopulated_fields = {'slug': ('aspect', 'name')}


@admin.register(Plan)
class PlanAdmin(CommonAdmin):
    fields = ('name', 'file', 'aspect', 'slug')
    list_display = ('name', 'aspect', 'slug')
    prepopulated_fields = {'slug': ('aspect', 'name')}


@admin.register(Event)
class EventAdmin(CommonAdmin):
    pass


@admin.register(Place)
class PlaceAdmin(CommonAdmin):
    fields = ('name', 'location', 'slug')


@admin.register(Person)
class PersonAdmin(CommonAdmin):
    fields = ('name', 'name_secondary', 'slug')
    list_display = ('name', 'gender', 'slug')
    prepopulated_fields = {'slug': ('name', 'name_secondary')}


@admin.register(Card)
class CardAdmin(CommonAdmin):
    fields = ('name', 'text_format', 'text', 'slug')
    list_display = ('name', 'text_format', 'slug')
    prepopulated_fields = {'slug': ('name',)}