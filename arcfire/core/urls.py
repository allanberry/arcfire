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
    url(r'^thing$', ModelListView.as_view(),
        kwargs={'model':Thing}, name='thing_list'),

    # model views
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

    # url(r'^relations/(?P<source>[-\w]+)/(?P<predicate>[-\w]+)/(?P<target>[-\w]+)$',
    #     ModelView.as_view(), kwargs={'model':Relation}, name='relation'),
    # url(r'^locations/(?P<longitude>[-\w]+)/(?P<latitude>[-\w]+)/(?P<altitude>[-\w]+)/(?P<time>[-\w]+)$',
    #     ModelView.as_view(), kwargs={'model':Location}, name='location'),
    # url(r'^collections/(?P<slug>[-\w]+)$', ModelView.as_view(),
    #     kwargs={'model':Thing}, name='collection'),
    # url(r'^groups/(?P<slug>[-\w]+)$', ModelView.as_view(),
    #     kwargs={'model':Thing}, name='group'),

    # DRF
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
