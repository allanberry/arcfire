from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from arcfire.models import Picture, Plan, Keyword, Property, Item, Event, Person, Place, Collection, Group, Location, Relation
import inflection


class HomeView(TemplateView):
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


# # # # # # # # # # # # # #
# Individual Model Views  #
# # # # # # # # # # # # # #

class ModelListView(ListView):
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
    template_name = "arcfire/place_list.html"
    model = Place


class PictureListView(ModelListView):
    model = Picture


class PlanListView(ModelListView):
    model = Plan


class KeywordListView(ModelListView):
    model = Keyword


class PropertyListView(ModelListView):
    model = Property


class ItemListView(ModelListView):
    model = Item


class EventListView(ModelListView):
    model = Event


class PersonListView(ModelListView):
    model = Person


class LocationListView(ModelListView):
    model = Location


class RelationListView(ModelListView):
    model = Relation


# class CollectionListView(ModelListView):
# class GroupListView(ModelListView):


# # # # # # # # # # # # # #
# Individual Model Views  #
# # # # # # # # # # # # # #

class ModelView(DetailView):
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
    model = Event
    parent_view = EventListView


class KeywordView(ModelView):
    model = Keyword
    parent_view = KeywordListView


class PersonView(ModelView):
    model = Person
    parent_view = PersonListView


class PictureView(ModelView):
    model = Picture
    parent_view = PictureListView


class PlanView(ModelView):
    model = Plan
    parent_view = PlanListView


class PlaceView(ModelView):
    model = Place
    parent_view = PlaceListView


class PropertyView(ModelView):
    model = Property
    parent_view = PropertyListView


class LocationView(ModelView):
    model = Location
    parent_view = LocationListView


class RelationView(ModelView):
    model = Relation
    parent_view = RelationListView


# class CollectionView(ModelView):
# class GroupView(ModelView):
