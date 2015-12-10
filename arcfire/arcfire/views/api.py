from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from arcfire.models import (
    Card, Event, Keyword, Person, Picture, Place, Plan, Property, Thing)
from arcfire.serializers import (
    CardSerializer, EventSerializer, KeywordSerializer, PersonSerializer, 
    PictureSerializer, PlaceSerializer, PlanSerializer, PropertySerializer,
    ThingSerializer)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# cards
class CardView(RetrieveUpdateDestroyAPIView):
    '''
    Card in JSON format.
    '''
    lookup_field = 'slug'
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardListView(ListCreateAPIView):
    '''
    List of Cards in JSON format.
    '''
    queryset = Card.objects.all()
    serializer_class = CardSerializer


# events
class EventView(RetrieveUpdateDestroyAPIView):
    '''
    Event in JSON format.
    '''
    lookup_field = 'slug'
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventListView(ListCreateAPIView):
    '''
    List of Events in JSON format.
    '''
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# keywords
class KeywordView(RetrieveUpdateDestroyAPIView):
    '''
    Keyword in JSON format.
    '''
    lookup_field = 'slug'
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer


class KeywordListView(ListCreateAPIView):
    '''
    List of Keywords in JSON format.
    '''
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer


# people
class PersonView(RetrieveUpdateDestroyAPIView):
    '''
    Person in JSON format.
    '''
    lookup_field = 'slug'
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonListView(ListCreateAPIView):
    '''
    List of People in JSON format.
    '''
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


# pictures
class PictureView(RetrieveUpdateDestroyAPIView):
    '''
    Pictures in JSON format.
    '''
    lookup_field = 'slug'
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class PictureListView(ListCreateAPIView):
    '''
    List of Pictures in JSON format.
    '''
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


# place
class PlaceView(RetrieveUpdateDestroyAPIView):
    '''
    Place in JSON format.
    '''
    lookup_field = 'slug'
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceListView(ListCreateAPIView):
    '''
    List of Places in JSON format.
    '''
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


# plan
class PlanView(RetrieveUpdateDestroyAPIView):
    '''
    Plan in JSON format.
    '''
    lookup_field = 'slug'
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class PlanListView(ListCreateAPIView):
    '''
    List of Plans in JSON format.
    '''
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


# property
class PropertyView(RetrieveUpdateDestroyAPIView):
    '''
    Property in JSON format.
    '''
    lookup_field = 'slug'
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class PropertyListView(ListCreateAPIView):
    '''
    List of Properties in JSON format.
    '''
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


# thing
class ThingView(RetrieveUpdateDestroyAPIView):
    '''
    Thing in JSON format.
    '''
    lookup_field = 'slug'
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


class ThingListView(ListCreateAPIView):
    '''
    List of Things in JSON format.
    '''
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


