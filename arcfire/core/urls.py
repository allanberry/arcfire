from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from arcfire.views.core import (
    HomeView, LoginView, LogoutView, SearchView, ModelView, ModelListView)

from arcfire.views.api import (
    CardViewJson, CardListViewJson)

from arcfire.models import (
    Card, Event, Keyword, Person, Picture, Place, Plan, Property, Thing)


# # # # #
# URLs  #
# # # # #

urlpatterns = [
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

    # single model
    url(r'^cards/(?P<slug>[-\w]+)$',
        ModelView.as_view(),
        kwargs={'model':Card},
        name='card'),

    url(r'^cards/(?P<slug>[-\w]+).json$',
        CardViewJson.as_view(),
        # kwargs={'model':Card},
        name='card_json'),

    url(r'^events/(?P<slug>[-\w]+)$', ModelView.as_view(),
        kwargs={'model':Event}, name='event'),
    url(r'^keywords/(?P<slug>[-\w]+)$', ModelView.as_view(),
        kwargs={'model':Keyword}, name='keyword'),
    url(r'^people/(?P<slug>[-\w]+)$', ModelView.as_view(),
        kwargs={'model':Person}, name='person'),
    url(r'^pictures/(?P<slug>[-\w]+)$', ModelView.as_view(),
        kwargs={'model':Picture}, name='picture'),
    url(r'^places/(?P<slug>[-\w]+)$', ModelView.as_view(),
        kwargs={'model':Place}, name='place'),
    url(r'^plans/(?P<slug>[-\w]+)$', ModelView.as_view(),
        kwargs={'model':Plan}, name='plan'),
    url(r'^properties/(?P<slug>[-\w]+)$', ModelView.as_view(),
        kwargs={'model':Property}, name='property'),
    url(r'^things/(?P<slug>[-\w]+)$', ModelView.as_view(),
        kwargs={'model':Thing}, name='thing'),

   # model list
    url(r'^cards$',
        ModelListView.as_view(),
        kwargs={'model':Card},
        name='card_list'),

    url(r'^cards.json$',
        CardListViewJson.as_view(),
        # kwargs={'model':Card},
        name='card_list_json'),

    url(r'^events$', ModelListView.as_view(),
        kwargs={'model':Event}, name='event_list'),
    url(r'^keywords$', ModelListView.as_view(),
        kwargs={'model':Keyword}, name='keyword_list'),
    url(r'^people$', ModelListView.as_view(),
        kwargs={'model':Person}, name='person_list'),
    url(r'^pictures$', ModelListView.as_view(),
        kwargs={'model':Picture}, name='picture_list'),
    url(r'^places$', ModelListView.as_view(),
        kwargs={'model':Place}, name='place_list'),
    url(r'^plans$', ModelListView.as_view(),
        kwargs={'model':Plan}, name='plan_list'),
    url(r'^properties$', ModelListView.as_view(),
        kwargs={'model':Property}, name='property_list'),
    url(r'^things$', ModelListView.as_view(),
        kwargs={'model':Thing}, name='thing_list'),
]
