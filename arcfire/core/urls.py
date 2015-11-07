from django.conf.urls import url, include
from django.contrib import admin
from arcfire.views import HomePageView

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from arcfire.views import (PictureListView, PlanListView,
    KeywordListView, PropertyListView, ItemListView, EventListView,
    ItemListView, PersonListView, PlaceListView, CollectionListView,
    GroupListView,
    # LocationListView,
    )

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
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomePageView.as_view(), name='home'),

    # model views
    url(r'^collections$', CollectionListView.as_view(), name='collection_list'),
    url(r'^events$', EventListView.as_view(), name='event_list'),
    url(r'^groups$', GroupListView.as_view(), name='group_list'),
    url(r'^items$', ItemListView.as_view(), name='item_list'),
    url(r'^keywords$', KeywordListView.as_view(), name='keyword_list'),
    # url(r'^locations$', LocationListView.as_view(), name='location_list'),
    url(r'^people$', PersonListView.as_view(), name='person_list'),
    url(r'^pictures$', PictureListView.as_view(), name='picture_list'),
    url(r'^places$', PlaceListView.as_view(), name='place_list'),
    url(r'^plans$', PlanListView.as_view(), name='plan_list'),
    url(r'^properties$', PropertyListView.as_view(), name='property_list'),

    # DRF
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
