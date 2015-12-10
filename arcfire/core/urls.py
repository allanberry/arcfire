from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from arcfire.views.core import (
    HomeView, LoginView, LogoutView, SearchView, ModelView, ModelListView)

from arcfire.views import api

from arcfire.models import (
    Card, Event, Keyword, Person, Picture, Place, Plan, Property, Thing)


# # # # #
# URLs  #
# # # # #

urlpatterns = [

    # # # # # #
    # GENERAL #
    # # # # # #

    # home
    url(r'^$',
        HomeView.as_view(),
        name='home'),

    # external
    url(r'^admin/',
        admin.site.urls),

    #auth
    url(r'^login/',
        LoginView.as_view(),
        name='login'),
    url(r'^logout/',
        LogoutView.as_view(),
        name='logout'),
    
    # searh
    url(r'^search$',
        SearchView.as_view(),
        name='search'),

    # # # # # # # # #
    # SINGLE MODEL  #
    # # # # # # # # #

    # card
    url(r'^cards/(?P<slug>[-\w]+)$',
        ModelView.as_view(),
        kwargs={'model':Card},
        name='card'),
    url(r'^api/cards/(?P<slug>[-\w]+)$',
        api.CardView.as_view(),
        name='card_json'),

    # event
    url(r'^events/(?P<slug>[-\w]+)$',
        ModelView.as_view(),
        kwargs={'model':Event},
        name='event'),
    url(r'^api/events/(?P<slug>[-\w]+)$',
        api.EventView.as_view(),
        name='event_json'),
    
    # keyword
    url(r'^keywords/(?P<slug>[-\w]+)$',
        ModelView.as_view(),
        kwargs={'model':Keyword},
        name='keyword'),
    url(r'^api/keywords/(?P<slug>[-\w]+)$',
        api.KeywordView.as_view(),
        name='keyword_json'),
    
    # person
    url(r'^people/(?P<slug>[-\w]+)$',
        ModelView.as_view(),
        kwargs={'model':Person},
        name='person'),
    url(r'^api/people/(?P<slug>[-\w]+)$',
        api.PersonView.as_view(),
        name='person_json'),

    # picture
    url(r'^pictures/(?P<slug>[-\w]+)$',
        ModelView.as_view(),
        kwargs={'model':Picture},
        name='picture'),
    url(r'^api/pictures/(?P<slug>[-\w]+)$',
        api.PictureView.as_view(),
        name='picture_json'),

    # place
    url(r'^places/(?P<slug>[-\w]+)$',
        ModelView.as_view(),
        kwargs={'model':Place},
        name='place'),
    url(r'^api/places/(?P<slug>[-\w]+)$',
        api.PlaceView.as_view(),
        name='place_json'),

    # plan
    url(r'^plans/(?P<slug>[-\w]+)$',
        ModelView.as_view(),
        kwargs={'model':Plan},
        name='plan'),
    url(r'^api/plans/(?P<slug>[-\w]+)$',
        api.PlanView.as_view(),
        name='plan_json'),

    # property
    url(r'^properties/(?P<slug>[-\w]+)$',
        ModelView.as_view(),
        kwargs={'model':Property},
        name='property'),
    url(r'^api/properties/(?P<slug>[-\w]+)$',
        api.PropertyView.as_view(),
        name='property_json'),

    # thing
    url(r'^things/(?P<slug>[-\w]+)$',
        ModelView.as_view(),
        kwargs={'model':Thing},
        name='thing'),
    url(r'^api/things/(?P<slug>[-\w]+)$',
        api.ThingView.as_view(),
        name='thing_json'),


    # # # # # # # #
    # MODEL LIST  #
    # # # # # # # #

    # cards
    url(r'^cards$',
        ModelListView.as_view(),
        kwargs={'model':Card},
        name='card_list'),
    url(r'^api/cards$',
        api.CardListView.as_view(),
        name='card_list_json'),

    # events
    url(r'^events$',
        ModelListView.as_view(),
        kwargs={'model':Event},
        name='event_list'),
    url(r'^api/events$',
        api.EventListView.as_view(),
        name='event_list_json'),

    # keywords
    url(r'^keywords$',
        ModelListView.as_view(),
        kwargs={'model':Keyword},
        name='keyword_list'),
    url(r'^api/keywords$',
        api.KeywordListView.as_view(),
        name='keyword_list_json'),

    # people
    url(r'^people$',
        ModelListView.as_view(),
        kwargs={'model':Person},
        name='person_list'),
    url(r'^api/people$',
        api.PersonListView.as_view(),
        name='person_list_json'),

    # pictures
    url(r'^pictures$',
        ModelListView.as_view(),
        kwargs={'model':Picture},
        name='picture_list'),
    url(r'^api/pictures$',
        api.PictureListView.as_view(),
        name='picture_list_json'),

    # places
    url(r'^places$',
        ModelListView.as_view(),
        kwargs={'model':Place},
        name='place_list'),
    url(r'^api/places$',
        api.PlaceListView.as_view(),
        name='place_list_json'),

    # plans
    url(r'^plans$',
        ModelListView.as_view(),
        kwargs={'model':Plan},
        name='plan_list'),
    url(r'^api/plans$',
        api.PlanListView.as_view(),
        name='plan_list_json'),

    # properties
    url(r'^properties$',
        ModelListView.as_view(),
        kwargs={'model':Property},
        name='property_list'),
    url(r'^api/properties$',
        api.PropertyListView.as_view(),
        name='property_list_json'),

    # things
    url(r'^things$',
        ModelListView.as_view(),
        kwargs={'model':Thing},
        name='thing_list'),
    url(r'^api/things$',
        api.ThingListView.as_view(),
        name='thing_list_json'),
]
