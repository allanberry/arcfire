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
from arcfire.models import *

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
            'page_title': 'Welcome to Arcfire.',
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

        # parent pages, in ('url_name', 'page_title') format
        # Allows multiple, ordered parents for breadcrumbs
        parent_pages = (
            ('home', 'Home'),
        )

        context.update({
            'window_title': 'Login',
            'page_title': 'Login to Arcfire.',
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

        # report to user
        messages.add_message(self.request,
            messages.SUCCESS, 'You have been logged out.')

        return super(LogoutView, self).get(request, *args, **kwargs)


class ModelView(DetailView):
    '''
    Single model pages.
    '''
    template_name = "arcfire/model.html"
    # parent_view = HomeView

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

    def get_context_data(self, *args, **kwargs):
        context = super(ModelView, self).get_context_data(*args, **kwargs)

        # parent pages, in ('url_name', 'page_title') format
        # Allows multiple, ordered parents for breadcrumbs
        parent_pages = (
            ('home', 'Home'),
            # ('{}_list'.format(self.parent_view.model._meta.verbose_name),
            #     self.parent_view.model._meta.verbose_name_plural.title()),
        )

        context.update({
            'window_title': self.object.name.title(),
            'page_title': self.object.name.title(),
            'parent_pages': parent_pages
        })

        return context


class ModelListView(ListView):
    '''
    Abstract class for providing functionality to further model views.
    '''

    # default template; should be able to (minimally) display any model
    template_name = 'arcfire/model_list.html'

    def dispatch(self, *args, **kwargs):
        # Override dispatch to set model instance variable.
        self.model = self.kwargs.pop('model')
        return super(ModelListView, self).dispatch(*args, **kwargs)        

    def get_template_names(self, *args, **kwargs):
        # Provide a template to use; otherwise, use default.
        templates = super(
            ModelListView, self).get_template_names(*args, **kwargs)
        model_templates = {
            Event:      'arcfire/timeline.html',
            Keyword:    'arcfire/inline_list.html',
            Person:     'arcfire/network.html',
            Picture:    'arcfire/gallery.html',
            Place:      'arcfire/map.html',
            Plan:       'arcfire/gallery.html',
            Property:   'arcfire/tree.html',
            Thing:      'arcfire/glossary.html',
        }
        if model_templates.get(self.model):
            templates.insert(0, model_templates[self.model])

        return templates

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