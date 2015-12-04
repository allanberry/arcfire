from collections import OrderedDict
from django.contrib import messages
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
from arcfire.models import (
    Event, Keyword, Person, Picture, Place, Plan, Property, Thing)
from arcfire.search import get_query

import inflection
# import floppyforms as forms # TODO: wait until FF 1.6, which is compatible
# with D1.9

class NavMixin(object):
    '''
    Mixin for shared functionality across views.
    TODO: Currently this is only used in ModelView, but I'd like to expand its use.
    '''

    def get_nav_relative(self, *args, **kwargs):
        '''
        A data structure to allow local wayfinding
        This defines the structure.  Meant to be heavily amended in subclass.
        '''
        nav_relative = [
            {'name': 'Home',
             'url': reverse_lazy('home')},
        ]
        return nav_relative


class HomeView(TemplateView):
    '''
    The main home page.
    '''
    template_name = "arcfire/home.html"

    def window_title(self):
        return 'Home'

    def page_title(self):
        return 'Welcome to Arcfire.'


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
        # Sets a test cookie to ensure cookies are enabled
        request.session.set_test_cookie()

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        # If the test cookie worked, delete it since it's no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        # report to user
        messages.add_message(self.request,
            messages.SUCCESS, 'Login successful.')

        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        redirect_to = self.request.POST.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, host=self.request.get_host()):
            redirect_to = self.success_url

        return redirect_to

    def get_context_data(self, *args, **kwargs):
        context = super(LoginView, self).get_context_data(*args, **kwargs)

        context.update({
            'window_title': 'Login',
            'page_title': 'Login to Arcfire.',
        })
        return context


class LogoutView(RedirectView):
    '''
    Provides logout functionality.
    '''
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        auth_logout(request)

        # report to user
        messages.add_message(self.request,
            messages.SUCCESS, 'You have been logged out.')

        return super(LogoutView, self).get(request, *args, **kwargs)


class SearchView(TemplateView):
    '''
    Results from search.
    '''
    template_name = "arcfire/search.html"

    def dispatch(self, *args, **kwargs):
        '''
        Setup
        '''
        self.searches = [
            {'model': Event,    'fields': ['name', 'slug']},
            {'model': Keyword,  'fields': ['name', 'slug']},
            {'model': Person,   'fields': ['name', 'slug']},
            {'model': Picture,  'fields': ['name', 'slug']},
            {'model': Place,    'fields': ['name', 'slug']},
            {'model': Plan,     'fields': ['name', 'slug']},
            {'model': Property, 'fields': ['name', 'slug']},
            {'model': Thing,    'fields': ['name', 'slug']},
        ]
        return super(SearchView, self).dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        '''
        Process site-wide search form.
        '''
        get_copy = self.request.GET.copy()
        query_string = ''

        # we're ok concatenating all query objects into a string,
        # because get_query will split them up anyways, and we don't want 
        # to do more than one query (per model).
        # Besides, this is only a boolean AND search, so we're not too picky.
        if get_copy:
            query_string = ' '.join(get_copy.pop('q', None))

        # do the search, once for each relevant model, and save in instance
        for dictionary in self.searches:
            model = dictionary['model']
            query = get_query(query_string, dictionary['fields'])
            if query_string:
                found = model.objects.filter(query)
            else:
                found = model.objects.all()

            # pass to get_context_data
            dictionary['result_set'] = found 

        return super(SearchView, self).get(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        '''
        Display Search Results.
        '''
        context = super(
            SearchView, self).get_context_data(*args, **kwargs)

        # populate search results
        for search_result in self.searches:
            model = search_result['model']
            instance = model() # need to instantiate to call class variables
            search_result.update({
                'model_name_plural': model._meta.verbose_name_plural.title(),
                'model_url': instance.get_list_url()
            })

        context.update({
            'window_title': 'Search Results',
            'page_title': 'Search Results.',
            'search_results': self.searches
        })
        return context


class ModelView(NavMixin, DetailView):
    '''
    Single model pages.
    Second level after Home.
    '''
    template_name = "arcfire/model.html"

    def dispatch(self, *args, **kwargs):
        # Override dispatch to set model instance variable.
        self.model = self.kwargs.pop('model')
        
        return super(ModelView, self).dispatch(*args, **kwargs)  

    def get_template_names(self, *args, **kwargs):   
        # Provide a template to use; otherwise, use default.
        templates = [
            'arcfire/{}.html'.format(self.model._meta.verbose_name),
            'arcfire/model.html'] # default/fallback

        # include (at the end) any which might be already fetched
        templates.extend(
            super(ModelView, self).get_template_names(*args, **kwargs))
        
        return templates

    def get_nav_relative(self, *args, **kwargs):
        '''A data structure to allow local wayfinding'''
        nav_relative = super(ModelView, self).get_nav_relative(*args, **kwargs)

        # each dict is a link
        # must have property 'name'; others are optional
        nav_relative.extend([
            {'name': 'Up: {}'.format(
                self.object._meta.verbose_name_plural.title()),
             'url': self.object.get_list_url()}, # TODO
            # {'name': 'Down'}, # TODO
            {'name': 'First: {}'.format(self.model.objects.all().first()), 
             'url': self.model.objects.all().first().get_absolute_url()},
            {'name': 'Last: {}'.format(self.model.objects.all().last()), 
             'url': self.model.objects.all().last().get_absolute_url()},
        ])

        if self.object.get_previous():
            nav_relative.append(
                {'name': 'Previous: {}'.format(self.object.get_previous()),
                 'url': self.object.get_previous().get_absolute_url()})
        if self.object.get_next():
            nav_relative.append(
                {'name': 'Next: {}'.format(self.object.get_next()),
                 'url': self.object.get_next().get_absolute_url()})

        return nav_relative


    def get_context_data(self, *args, **kwargs):
        context = super(ModelView, self).get_context_data(*args, **kwargs)

        nav_relative = self.get_nav_relative()

        context.update({
            'window_title': self.object.__str__().title(),
            'page_title': self.object.__str__().title(),
            'nav_relative': nav_relative,
        })
        return context


class ModelListView(ListView):
    '''
    An abstract class for compound model views: where models are seen in list 
    or group format.  
    Third level after ModelView and Home.
    '''

    # default template; should be able to (minimally) display any model
    template_name = 'arcfire/model_list.html'


    def dispatch(self, *args, **kwargs):
        # override dispatch to set model instance variable
        self.model = self.kwargs.pop('model')

        return super(ModelListView, self).dispatch(*args, **kwargs)

    def get_model_template(self, *args, **kwargs):
        '''
        All models derived from Common can be viewed as a list in a template.
        Which is best to view this model?
        '''

        # The best template for presenting any particular model list.
        templates = [
            {'model': Event,    'template': 'arcfire/timeline.html'},
            {'model': Keyword,  'template': 'arcfire/inline_list.html'},
            {'model': Person,   'template': 'arcfire/network.html'},
            {'model': Picture,  'template': 'arcfire/gallery.html'},
            {'model': Place,    'template': 'arcfire/map.html'},
            {'model': Plan,     'template': 'arcfire/gallery.html'},
            {'model': Property, 'template': 'arcfire/tree.html'},
            {'model': Thing,    'template': 'arcfire/glossary.html'},
        ]

        # add relevant template to start of template list
        model_template_dict = next(
            (d for d in templates if d['model'] == self.model), None) 

        if model_template_dict:
            return model_template_dict['template']
        else:
            # just a default; should work though for any model.
            return self.template     

    def get_template_names(self, *args, **kwargs):
        # start with the extant list of templates, if relevant
        templates = super(
            ModelListView, self).get_template_names(*args, **kwargs)

        # standard templates for model lists are defined in the model
        # add the relevant one to the 'templates' list
        templates.insert(0, self.get_model_template(self.model))

        return templates


    def get_context_data(self, *args, **kwargs):
        context = super(ModelListView, self).get_context_data(*args, **kwargs)

        context.update({
            'window_title': self.model._meta.verbose_name_plural.title(),
            'page_title': self.model._meta.verbose_name_plural.title(),
            'model_name': self.model._meta.verbose_name,
            'model_name_plural': self.model._meta.verbose_name_plural,
        })
        return context