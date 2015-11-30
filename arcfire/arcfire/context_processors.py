from arcfire.models import *

models_list = [
    Event,
    Keyword,
    Person,
    Picture,
    Place,
    Plan,
    Property,
    Thing,
]

def arcfire_global_context(request):
    '''
    Arcfire main global context.
    '''
    # NAVIGATION
    # Populate navigation with a list of models.
    # Add further links afterward if necessary.
    nav_models = [{
        'name_plural': m._meta.verbose_name_plural,
        'url_name': get_model_url(m)
    } for m in models_list ]

    return {
        'nav_models': nav_models
    }


def get_model_url(model):
    '''
    Link url names back from model names.
    '''

    models_dict = {
        Event: 'event_list',
        Keyword: 'keyword_list',
        Person: 'person_list',
        Picture: 'picture_list',
        Place: 'place_list',
        Plan: 'plan_list',
        Property: 'property_list',
        Thing: 'thing_list',
    }

    # TODO this functionality is already in models; refactor this out.  
    return models_dict[model]

