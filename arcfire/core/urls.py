from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from arcfire.views import *
from arcfire.models import *


# # # # # # #
# DRF setup # TODO: break this stuff into another file
# # # # # # #

# Serializers define the API representation
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide a way to automatically determine the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


# # # # #
# URLs  #
# # # # #

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),

    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    
    # model views
    url(r'^events$', ModelListView.as_view(),
        kwargs={'model':Event}, name='event_list'),
    url(r'^keywords$', ModelListView.as_view(),
        kwargs={'model':Keyword}, name='keyword_list'),
    url(r'^locations$', ModelListView.as_view(),
        kwargs={'model':Location}, name='location_list'),
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
    url(r'^relations$', ModelListView.as_view(),
        kwargs={'model':Relation}, name='relation_list'),
    url(r'^thing$', ModelListView.as_view(),
        kwargs={'model':Thing}, name='thing_list'),
    # url(r'^groups$', ModelListView.as_view(),
        # kwargs={'model':Group}, name='group_list'),
    # url(r'^collections$', ModelListView.as_view(),
        # kwargs={'model':Collection}, name='collection_list'),

    # model views
    url(r'^events/(?P<slug>[-\w]+)$', EventView.as_view(), name='event'),
    url(r'^keywords/(?P<slug>[-\w]+)$', KeywordView.as_view(), name='keyword'),
    url(r'^people/(?P<slug>[-\w]+)$', PersonView.as_view(), name='person'),
    url(r'^pictures/(?P<slug>[-\w]+)$', PictureView.as_view(), name='picture'),
    url(r'^places/(?P<slug>[-\w]+)$', PlaceView.as_view(), name='place'),
    url(r'^plans/(?P<slug>[-\w]+)$', PlanView.as_view(), name='plan'),
    url(r'^properties/(?P<slug>[-\w]+)$', PropertyView.as_view(), name='property'),
    url(r'^things/(?P<slug>[-\w]+)$', ThingView.as_view(), name='thing'),
    url(r'^relations/(?P<source>[-\w]+)/(?P<predicate>[-\w]+)/(?P<target>[-\w]+)$',
        RelationView.as_view(), name='relation'),
    url(r'^locations/(?P<longitude>[-\w]+)/(?P<latitude>[-\w]+)/(?P<altitude>[-\w]+)/(?P<time>[-\w]+)$',
        LocationView.as_view(), name='location'),
    # url(r'^collections/(?P<slug>[-\w]+)$', CollectionView.as_view(), name='collection'),
    # url(r'^groups/(?P<slug>[-\w]+)$', GroupView.as_view(), name='group'),

    # DRF
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
