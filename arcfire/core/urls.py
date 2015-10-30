from django.conf.urls import url, include
from django.contrib import admin
from arcfire.views import HomePageView

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

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

    # DRF
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
