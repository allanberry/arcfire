from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# # # # # # # # #
# Bootstrapping #
# # # # # # # # #

class Common(models.Model):
    '''
    Abstract base class for elements, for bootstrapping.  Basically the most generic metadata, used throughout.
    '''
    class Meta:
        abstract = True

    name = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(unique=True, blank=False)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(
        editable=False, blank=False, null=True)
    updated_at = models.DateTimeField(
        blank=False, null=True)

    def save(self, *args, **kwargs):
        '''
        On save, update timestamps
        as per http://stackoverflow.com/a/1737078/652626
        '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Common, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.name)


class LifeMixin(models.Model):
    '''
    Breathes life, as a mixin.
    '''
    class Meta:
        abstract = True

    GENDERS = (
        ('female', 'Female'),
        ('male', 'Male'),
        ('none', 'None'),
        ('other', 'Other'),
    )
    gender = models.CharField(max_length=10, choices=GENDERS, blank=True)
    species = models.CharField(max_length=255, blank=True,
        help_text='TODO: Use controlled vocabulary.')
    ki = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(1)],
        blank=False, null=True,
        default=0.5, max_digits=4, decimal_places=3, help_text="Choose a number between 0.0 and 1.0.  The default is 0.5, which represents the life-force of Joe the Plumber.  0.0 is empty space, somewhere past Pluto.  1.0 is God himself. See wiki/ki for more information.") # TODO: wiki/ki


class CollectableMixin(models.Model):
    '''
    Abstract base class for groups of elements.
    '''
    class Meta:
        abstract = True

    collection = []
    # I'm not entirely sure what I want to do with this yet, since fields need
    # to be defined in each subclass instead of overridden.  This makes things
    # more complex than I like, but probably OK.  In the meantime, I'll
    # leave this here and give it methods soon, hopefully generic to work
    # for all subclasses.



class AspectMixin(models.Model):
    '''
    A type of representation, like an angle or perspective, usually for Picture or Plan.
    '''
    class Meta:
        abstract = True
    CHOICES = (
        ('primary', 'Primary'),
        ('secondary', 'Secondary'),
        ('front', 'Front'),
        ('back', 'Back'),
        ('left', 'Left Side'),
        ('right', 'Right Side'),
        ('top', 'Top'),
        ('bottom', 'Bottom'),
        ('internal', 'Internal'),
        ('external', 'External'),
    )
    aspect = models.CharField(
        blank=False,
        max_length=10, unique=True, choices=CHOICES, default='primary')


class RelationJoin(models.Model):
    '''
    Relationships between elements.
    '''
    # when ambiguity exists, relations should be of the form:
    # 1. source (subject, inferior, child, or branch)
    # 2. predicate
    # 3. target (direct object, superior, parent, or trunk)
    PREDICATES = (
        ('related', 'is related to'),
        ('attract', 'is attracted to'),
        ('cause', 'is caused by'),
        ('child', 'is child of'),
        ('control', 'is controlled by'),
        ('friend', 'is friend of'),
        ('inside', 'is inside of'),
        ('mate', 'is mate of'),
        ('own', 'is owned by'),
        ('part', 'is part of'),
        ('result', 'is result of'),
        ('subject', 'is subject of'),
        ('type', 'is type of'),
    )
    source = models.ForeignKey("self", related_name="sources",
        blank=False, null=True)
    target = models.ForeignKey("self", related_name="targets",
        blank=False, null=True)
    predicate = models.CharField(
        blank=False, max_length=10, choices=PREDICATES, default='related')

    def __str__(self):
        return '{} {} {}'.format(source, predicate, target)


class Picture(AspectMixin, Common):
    '''
    An "a posteriori" representation of something, usually raster, usually graphical.  Contrast with 'Plan'.
    '''

    width = models.PositiveIntegerField(help_text="In pixels.",
        blank=False, null=True)
    height = models.PositiveIntegerField(help_text="In pixels.",
        blank=False, null=True)
    image = models.ImageField(width_field=width, height_field=height,
        blank=False, null=True)

    # def image_tag(self): # TODO
    #     return '<img src="{}" width="{}" height="{}" />'.format(self.url, self.width, self.height)



class Plan(AspectMixin, Common):
    '''
    An "a priori" representation of something, usually vector, usually graphical.  Contrast with 'Picture'.
    '''
    file = models.FileField(blank=False, null=True)

class Location(Common):
    '''
    A set of geographic and temporal coordinates for an item.
    '''

    KINDS = (
        ('begin', 'Begin'),
        ('change', 'Change'),
        ('end', 'End'),
    )
    kind = models.CharField(max_length=10, choices=KINDS, blank=True)

    POSITIONS = (
        ('absolute', 'Absolute'),
        ('relative', 'Relative')
    )
    position = models.CharField(max_length=10, choices=POSITIONS, blank=False, default='relative', help_text='"Absolute" positions establish a new reference point for sublocations: they are always relative to the ABSOLUTE_LOCATION in settings.  "Relative" positions are relative to their nearest "Absolute" parent, otherwise they are also relative to ABSOLUTE_LOCATION.  See: wiki/position') # TODO: set REFERENCE_LOCATION
    time = models.DateTimeField(blank=True, null=True) # TODO: set default to D.time
    longitude = models.DecimalField(max_digits=9, decimal_places=6,
        blank=True, null=True,
        help_text="In decimal.")
    latitude = models.DecimalField(max_digits=9, decimal_places=6,
        blank=True, null=True,
        help_text="In meters.")
    altitude = models.DecimalField(max_digits=9, decimal_places=3,
        blank=True, null=True,
        help_text="In meters.")

    sublocations = models.ManyToManyField("self", blank=True, help_text="The main location indicates the reference point (e.g. the center); if sublocations are relative, they are  to this point.")

    def __str__(self):
        if self.name:
            return self.name
        else:
            return '{} @ time:{} long:{} lat:{} alt:{}'.format(position, time, longitude, latitude, altitude)

class Keyword(Common):
    '''
    A grass-roots means of classifying something.
    '''
    pass


class Property(Common):
    '''
    A characteristic or attribute of something.
    '''
    class Meta:
        verbose_name_plural = 'properties'
    pass


class Item(Common):
    '''
    The manifestation of the abstract attributes in "Common", but with access to subsequent models like picture and plan.
    '''

    keywords = models.ManyToManyField(Keyword, blank=True)
    properties = models.ManyToManyField(Property, blank=True)
    locations = models.ManyToManyField(Location, blank=True)

    # relations = models.ManyToManyField("self", through='RelationJoin', symmetrical=False)

    pictures = models.ManyToManyField(Picture, blank=True)
    plans = models.ManyToManyField(Plan, blank=True)

    scale = models.PositiveIntegerField(default=0, blank=True, null=True,
        help_text='The magnitude of a thing, in whole numbers.  0 is average/medium/normal/default/human-sized.  e.g.: -2=XS, -1=S, 0=M, 1=L, 2=XL, 3=2XL and so on.')


# # # # # # # # # # # # #
# Level 1: Basic Items  #
# # # # # # # # # # # # #

class Event(Item):
    '''
    Basic Verb.
    '''
    pass


class Thing(Item):
    '''
    Basic Noun.
    '''
    mass = models.DecimalField(max_digits=12, decimal_places=3,
        help_text="In kilograms.",
        blank=True, null=True)
    height = models.DecimalField(max_digits=12, decimal_places=3,
        help_text="In meters.",
        blank=True, null=True)
    width = models.DecimalField(max_digits=12, decimal_places=3,
        help_text="In meters.",
        blank=True, null=True)
    length = models.DecimalField(max_digits=12, decimal_places=3,
        help_text="In meters.",
        blank=True, null=True)
    heading = models.DecimalField(max_digits=4, decimal_places=3,
        blank=True, null=True,
        help_text="In radians.  The angle between the direction the item is pointing and true North.")
    # approximation


# # # # # # # # # # # # # #
# Level 2: Compound Items #
# # # # # # # # # # # # # #


class Person(LifeMixin, Thing):
    '''
    A human being.
    '''
    name_secondary = models.CharField(verbose_name='Given Name', max_length=255,
        blank=True)

    def __init__(self, *args, **kwargs):
        self._meta.get_field('name').blank = False
        self._meta.get_field('name').verbose_name = 'Family Name'
        self._meta.get_field('species').default = 'homo sapiens'
        # self._meta.get_field('mass').default = 75
        # self._meta.get_field('height').default = 1.75
        # self._meta.get_field('gender').default = 'female'
        super(Person, self).__init__(*args, **kwargs)

    def name_full(self):
        if self.name_secondary and self.name:
            return '{}, {}'.format(self.name, self.name_secondary)
        elif self.name:
            return '{}'.format(self.name)
        else:
            return 'No Name'

    def __str__(self):
        return self.name_full()


class Place(LifeMixin, Location):
    '''
    Some places have an energy all their own.
    '''
    pass


class Collection(CollectableMixin, Thing):
    '''
    A group of things.
    '''
    pass

class Group(CollectableMixin, Person):
    '''
    A group of people.
    '''
    pass


# class Memory(Thing):
#     '''
#     Something a living thing takes with them.
#     '''
#     life = models.ForeignKey(Life, related_name="memories")


# class Plant(Life):
#     '''
#     A plant (flora).
#     '''
#     pass


# class Animal(Life):
#     '''
#     An animal (fauna).
#     '''
#     pass


#
# class Group(Collectable, Person):
#     '''
#     An organization, class, tribe or family of human beings.
#     '''
#     # cls = Person
#     members = models.ManyToManyField(Person, related_name="groups")
