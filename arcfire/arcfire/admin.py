from django.contrib import admin
# from .models import Picture, Plan, Location, Keyword, Property, Event, Thing, Person, Place, Collection, Group
from .models import Person, Property, Picture, Place, Event, Keyword

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'keywords', 'properties', 'locations', 'pictures', 'plans', 'description', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Keyword)
class EventAdmin(admin.ModelAdmin):
    fields = ('name','subkeywords', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fields = ('name', 'keywords', 'name_secondary', 'properties', 'height', 'mass', 'pictures', 'description', 'slug')
    list_display = ('__str__', 'gender')
    prepopulated_fields = {'slug': ('name', 'name_secondary')}

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    fields = ('name', 'keywords', 'image', 'aspect', 'width', 'height', 'description', 'slug')
    list_display = ('__str__', 'aspect')
    prepopulated_fields = {'slug': ('aspect', 'name')}

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    fields = ('name', 'keywords', 'longitude', 'latitude', 'altitude', 'time', 'kind', 'position', 'sublocations', 'ki', 'description', 'slug')
    list_display = ('name', 'longitude', 'latitude', 'altitude', 'time')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    fields = ('name', 'keywords', 'description', 'slug')
    list_display = ('__str__', 'slug')
    prepopulated_fields = {'slug': ('name',)}

