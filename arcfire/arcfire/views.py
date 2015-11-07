from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from arcfire.models import (Picture, Plan, Keyword, Property, Item,
    Event, Person, Place, Collection, Group,
    #Location, 
    )


class HomePageView(TemplateView):
    template_name = "arcfire/home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        context.update({
            'window_title': 'Home',
        })
        return context


class ModelListView(ListView):
    template_name = "arcfire/model_list.html"

    def get_window_title(self):
        return self.model._meta.verbose_name_plural

    def get_context_data(self, *args, **kwargs):
        context = super(ModelListView, self).get_context_data(*args, **kwargs)
        context.update({
            'window_title': self.get_window_title(),
            'model_name': self.model._meta.verbose_name,
            'model_name_plural': self.model._meta.verbose_name_plural,
        })
        return context


class PlaceListView(ModelListView):
    template_name = "arcfire/place_list.html"
    model = Place


class PictureListView(ModelListView):
    model = Picture


# class LocationListView(ModelListView):
#     model = Location


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


class CollectionListView(ModelListView):
    model = Collection


class GroupListView(ModelListView):
    model = Group
