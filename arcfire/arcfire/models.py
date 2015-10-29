from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# # # # # # # # #
# Bootstrapping #
# # # # # # # # #

class Common(models.Model):
    '''
    Abstract base class for elements, for bootstrapping.
    '''
    class Meta:
        abstract = True

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    scale = models.PositiveIntegerField(default=0)
    ki = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(1)],
        default=0, max_digits=4, decimal_places=3)

    keywords = models.ManyToManyField("self")
    properties = models.ManyToManyField("self")
    purposes = models.ManyToManyField("self")
    relations = models.ManyToManyField("self", through='RelationJoin', symmetrical=False)


class Collectable(models.Model):
    '''
    Abstract base class for groups of elements.
    '''
    class Meta:
        abstract = True
    # I'm not entirely sure what I want to do with this yet, since fields need
    # to be defined in each subclass instead of overridden.  This makes things
    # more complex than I like, but probably OK.  In the meantime, I'll
    # leave this here and give it methods soon, hopefully generic to work
    # for all subclasses.


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
    source = models.ForeignKey("self", related_name="sources")
    target = models.ForeignKey("self", related_name="targets")
    type = models.CharField(
        max_length=10, blank=False, choices=PREDICATES, default='related')


class Aspect(models.Model):
    '''
    A type of representation, like an angle or perspective, usually for Picture or Plan.
    '''
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
        max_length=10, unique=True, blank=False, choices=CHOICES, default='primary')


class Picture(Common):
    '''
    An "a posteriori" representation of an element, usually raster, usually graphical.  Contrast with 'Plan'.
    '''
    width = models.PositiveIntegerField(help_text="In pixels.")
    height = models.PositiveIntegerField(help_text="In pixels.")
    aspect = models.ForeignKey(Aspect, related_name="pictures")
    image = models.ImageField(width_field=width, height_field=height)


class Plan(Common):
    '''
    An "a priori" representation of an element, usually vector, usually graphical.  Contrast with 'Picture'.
    '''
    aspect = models.ForeignKey(Aspect, related_name="plans")
    file = models.FileField()



# # # # # # # # # # #
# Level 1: Elements #
# # # # # # # # # # #


class Item(Common):
    '''
    Basic Noun.
    '''
    mass = models.DecimalField(max_digits=12, decimal_places=3,
        help_text="In kilograms.")

    pictures = models.ManyToManyField(Picture)
    plans = models.ManyToManyField(Plan)

    height = models.DecimalField(max_digits=12, decimal_places=3,
        help_text="In meters.")
    width = models.DecimalField(max_digits=12, decimal_places=3,
        help_text="In meters.")
    length = models.DecimalField(max_digits=12, decimal_places=3,
        help_text="In meters.")
    heading = models.DecimalField(max_digits=4, decimal_places=3,
        help_text="In radians.  The angle between the direction the item is pointing and true North.")
    # approximation


class Collection(Collectable, Item):
    '''
    A selected group of items.
    '''
    items = models.ManyToManyField(Item, related_name="collections")


class Location(Common):
    '''
    A set of geographic and temporal coordinates for an item.
    '''
    item = models.ForeignKey(Item)
    KINDS = (
        ('begin', 'Begin'),
        ('change', 'Change'),
        ('end', 'End'),
    )
    time = models.DateTimeField()
    longitude = models.DecimalField(max_digits=9, decimal_places=6, help_text="In decimal.")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, help_text="In meters.")
    altitude = models.DecimalField(max_digits=9, decimal_places=3, help_text="In meters.")
    kind = models.CharField(max_length=10, choices=KINDS)


class Event(Common):
    '''
    Basic Verb.
    '''
    # Not sure what I'm going to do with this yet, but it seems necessary to include.


# # # # # #
# Level 2 #
# # # # # #


class Life(Item):
    '''
    A Living thing.
    '''

    GENDERS = (
        ('female', 'Female'),
        ('male', 'Male'),
        ('none', 'None'),
        ('other', 'Other'),
    )
    gender_default = None
    species_default = None

    gender = models.CharField(max_length=10, blank=True, null=True,
        choices=GENDERS, default=gender_default)
    species = models.CharField(max_length=255, blank=True, null=True,
        default=species_default)


class Memory(Common):
    '''
    Something a living thing takes with them.
    '''
    life = models.ForeignKey(Life, related_name="memories")


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


class Person(Life):
    '''
    A human being.
    '''
    class Meta:
        proxy = True

    species_default = 'homo sapiens'


class Group(Collectable, Person):
    '''
    An organization, class, tribe or family of human beings.
    '''
    # cls = Person
    members = models.ManyToManyField(Person, related_name="groups")
