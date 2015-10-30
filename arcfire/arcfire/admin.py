from django.contrib import admin
# from .models import Picture, Plan, Location, Keyword, Property, Event, Thing, Person, Place, Collection, Group
from .models import Person, Property, Picture

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fields = ('name', 'name_secondary', 'description',  'gender', 'properties', 'height', 'mass', 'pictures', 'slug')
    list_display = ('name', 'name_secondary', 'gender')
    prepopulated_fields = {'slug': ('name', 'name_secondary')}

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'slug')
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    fields = ('name', 'image', 'aspect', 'description', 'width', 'height', 'slug')
    list_display = ('name', 'aspect')
    prepopulated_fields = {'slug': ('aspect', 'name')}
