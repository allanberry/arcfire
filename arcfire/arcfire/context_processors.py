from arcfire.models import (Collection, Event, Group, Item,
    Keyword, Person, Picture, Place, Plan, Property,
    # Location,
    )


def arcfire_global_context(request):
    '''
    Arcfire main global context.
    '''
    # NAVIGATION
    # Populate navigation with a list of models.
    # Add further links afterward if necessary.
    models = [Collection, Event, Group, Item, Keyword,
        Person, Picture, Place, Plan, Property,
        #Location
        ]
    nav_models = [{
        'name_plural': m._meta.verbose_name_plural,
        'url_name': get_model_url(m)
    } for m in models ]

    return {
        'nav_models': nav_models
    }


def get_model_url(model):
    '''
    Link url names back from model names.
    '''
    models = {
        Collection: 'collection_list',
        Event: 'event_list',
        Group: 'group_list',
        Item: 'item_list',
        Keyword: 'keyword_list',
        # Location: 'location_list',
        Person: 'person_list',
        Picture: 'picture_list',
        Place: 'place_list',
        Plan: 'plan_list',
        Property: 'property_list',
    }
    return models[model]

