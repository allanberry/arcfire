from django.contrib import admin
# from .models import Picture, Plan, Location, Keyword, Property, Event, Thing, Person, Place, Collection, Group
from .models import Person, Property, Picture, Place

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fields = ('name', 'name_secondary', 'description',  'gender', 'properties', 'height', 'mass', 'pictures', 'slug')
    list_display = ('__str__', 'gender')
    prepopulated_fields = {'slug': ('name', 'name_secondary')}

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    list_display = ('__str__', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    fields = ('name', 'image', 'aspect', 'description', 'width', 'height', 'slug')
    list_display = ('__str__', 'aspect')
    prepopulated_fields = {'slug': ('aspect', 'name')}

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'longitude', 'latitude', 'altitude', 'time', 'kind', 'position', 'sublocations', 'ki', 'slug')
    list_display = ('name', 'longitude', 'latitude', 'altitude', 'time')
    prepopulated_fields = {'slug': ('name',)}