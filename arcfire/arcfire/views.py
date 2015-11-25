from django.contrib.auth import (
    REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout)
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from arcfire.models import Picture, Plan, Keyword, Property, Thing, Event, Person, Place, Collection, Group, Location, Relation

import inflection
# import floppyforms as forms # TODO: wait until FF 1.6, which is compatible
# with D1.9


class HomeView(TemplateView):
    '''
    The main home page.
    '''
    template_name = "arcfire/home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)

        parent_pages = ()

        context.update({
            'window_title': 'Home',
            'page_title': 'Home',
            'parent_pages': parent_pages
        })
        return context


class LoginView(FormView):
    '''
    Provides login with a username and password.
    https://coderwall.com/p/sll1kw/django-auth-class-based-views-login-and-logout
    '''
    success_url = reverse_lazy('login')
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = "arcfire/login.html"

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        print(self.request.POST.get(self.redirect_field_name))

        redirect_to = self.request.POST.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, host=self.request.get_host()):
            redirect_to = self.success_url
        return redirect_to

    def get_context_data(self, *args, **kwargs):
        context = super(LoginView, self).get_context_data(*args, **kwargs)

        # parent pages, in ('url_name', 'page_title') format
        # Allows multiple, ordered parents for breadcrumbs
        parent_pages = (
            ('home', 'Home'),
        )

        context.update({
            'window_title': 'Authenticate',
            'page_title': 'Authenticate',
            'parent_pages': parent_pages
        })
        return context


class LogoutView(RedirectView):
    '''
    Provides logout functionality.
    '''
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


# # # # # # # # # # # # # #
# Individual Model Views  #
# # # # # # # # # # # # # #

class ModelListView(ListView):
    '''
    Abstract class for providing functionality to further model views.
    '''
    template_name = "arcfire/model_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ModelListView, self).get_context_data(*args, **kwargs)

        parent_pages = (
            ('home', 'Home'),
        )

        context.update({
            'window_title': self.model._meta.verbose_name_plural.title(),
            'page_title': self.model._meta.verbose_name_plural.title(),

            'model_name': self.model._meta.verbose_name,
            'model_name_plural': self.model._meta.verbose_name_plural,
            'parent_pages': parent_pages
        })
        return context


class PlaceListView(ModelListView):
    '''
    Places presented on a map.
    '''
    template_name = "arcfire/place_list.html"
    model = Place


class PictureListView(ModelListView):
    '''
    Pictures presented in a gallery.
    '''
    model = Picture


class PlanListView(ModelListView):
    '''
    Plans presented in a gallery/list.
    '''
    model = Plan


class KeywordListView(ModelListView):
    '''
    Keywords presented possibly in a tag cloud.
    '''
    model = Keyword


class PropertyListView(ModelListView):
    '''
    Properties presented by organization into a hierarchy. 
    '''
    model = Property


class ThingListView(ModelListView):
    '''
    Things presented in dictionary form.
    '''
    model = Thing


class EventListView(ModelListView):
    '''
    Events presented in a timeline.
    '''
    model = Event


class PersonListView(ModelListView):
    '''
    People/Characters presented in a network graph.
    '''
    model = Person


class LocationListView(ModelListView):
    '''
    Locations presented on a map; see PlaceListView
    '''
    model = Location


class RelationListView(ModelListView):
    '''
    Relations presented... in a list?  In a series of chord graphs?
    '''
    model = Relation


# class CollectionListView(ModelListView):
# class GroupListView(ModelListView):


# # # # # # # # # # # # # #
# Individual Model Views  #
# # # # # # # # # # # # # #

class ModelView(DetailView):
    '''
    Abstract base class for individual model pages, below.
    '''
    template_name = "arcfire/model.html"
    parent_view = HomeView

    def get_context_data(self, *args, **kwargs):
        context = super(ModelView, self).get_context_data(*args, **kwargs)

        # parent pages, in ('url_name', 'page_title') format
        # Allows multiple, ordered parents for breadcrumbs
        parent_pages = (
            ('home', 'Home'),
            ('{}_list'.format(self.parent_view.model._meta.verbose_name),
                self.parent_view.model._meta.verbose_name_plural.title()),
        )

        context.update({
            'window_title': self.object.name.title(),
            'page_title': self.object.name.title(),
            'parent_pages': parent_pages
        })
        return context


class EventView(ModelView):
    '''
    A single Event.
    '''
    model = Event
    parent_view = EventListView


class ThingView(ModelView):
    '''
    A single Thing.
    '''
    model = Thing
    parent_view = ThingListView


class KeywordView(ModelView):
    '''
    A single Keyword.
    '''
    model = Keyword
    parent_view = KeywordListView


class PersonView(ModelView):
    '''
    A single Person.
    '''
    model = Person
    parent_view = PersonListView


class PictureView(ModelView):
    '''
    A single Picture.
    '''
    model = Picture
    parent_view = PictureListView


class PlanView(ModelView):
    '''
    A single Plan.
    '''
    model = Plan
    parent_view = PlanListView


class PlaceView(ModelView):
    '''
    A single Place.
    '''
    model = Place
    parent_view = PlaceListView


class PropertyView(ModelView):
    '''
    A single Property.
    '''
    model = Property
    parent_view = PropertyListView


class LocationView(ModelView):
    '''
    A single Location.
    '''
    model = Location
    parent_view = LocationListView


class RelationView(ModelView):
    '''
    A single Relation.
    '''
    model = Relation
    parent_view = RelationListView


# class CollectionView(ModelView):
# class GroupView(ModelView):
