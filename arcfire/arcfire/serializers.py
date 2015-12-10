from rest_framework.serializers import ModelSerializer
from arcfire.models import (
    Card, Event, Keyword, Person, Picture, Place, Plan, Property, Thing)


class CardSerializer(ModelSerializer):
    '''
    JSON serializer for Cards.
    '''

    class Meta:
        model = Card
        fields = (
            'pk', 'name', 'text', 'slug')


class EventSerializer(ModelSerializer):
    '''
    JSON serializer for Events.
    '''

    class Meta:
        model = Event
        fields = (
            'pk', 'name', 'slug')


class KeywordSerializer(ModelSerializer):
    '''
    JSON serializer for Keywords.
    '''

    class Meta:
        model = Keyword
        fields = (
            'pk', 'name', 'slug')


class PersonSerializer(ModelSerializer):
    '''
    JSON serializer for Person.
    '''

    class Meta:
        model = Person
        fields = (
            'pk', 'name', 'slug')


class PictureSerializer(ModelSerializer):
    '''
    JSON serializer for Pictures.
    '''

    class Meta:
        model = Picture
        fields = (
            'pk', 'name', 'slug')


class PlaceSerializer(ModelSerializer):
    '''
    JSON serializer for Places.
    '''

    class Meta:
        model = Place
        fields = (
            'pk', 'name', 'slug')


class PlanSerializer(ModelSerializer):
    '''
    JSON serializer for Plans.
    '''

    class Meta:
        model = Plan
        fields = (
            'pk', 'name', 'slug')


class PropertySerializer(ModelSerializer):
    '''
    JSON serializer for Properties.
    '''

    class Meta:
        model = Property
        fields = (
            'pk', 'name', 'slug')


class ThingSerializer(ModelSerializer):
    '''
    JSON serializer for Things.
    '''

    class Meta:
        model = Thing
        fields = (
            'pk', 'name', 'slug')
