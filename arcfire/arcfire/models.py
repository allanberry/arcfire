from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# # # # # # # # #
# Bootstrapping #
# # # # # # # # #

class Common(models.Model):
    '''
    Abstract base class for elements.
    '''
    class Meta:
        abstract = True
        ordering = ['name']

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    scale = models.PositiveIntegerField(default=0)
    sentience = models.DecimalField(
        validators = [MinValueValidator(0), MaxValueValidator(1)])


class Keyword(Common):
    '''
    A means of sorting elements.
    '''
    class Meta:
        abstract = True
    name = models.CharField(max_length=255, unique=True, required=True)


class Location(Common):
    '''
    A set of geographic and temporal coordinates of elements.
    '''
    class Meta:
        abstract = True
    KINDS = (
        ('begin', 'Begin'),
        ('change', 'Change'),
        ('end', 'End'),
    )
    longitude = DecimalField(max_digits=9, decimal_places=6)
    latitude = DecimalField(max_digits=9, decimal_places=6)
    altitude = DecimalField(decimal_places=3)
    time = models.DateTimeField()
    kind = models.CharField(
        max_length=10,
        choices=KINDS)


class Property(Common):
    '''
    Characteristics, adjectives of elements.
    '''
    class Meta:
        abstract = True
    name = models.CharField(max_length=255, unique=True, required=True)


class Purpose(Common):
    '''
    Generic class to track what elements are for.
    '''
    class Meta:
        abstract = True
    name = models.CharField(max_length=255, unique=True, required=True)


# # # # # #
# Level 1 #
# # # # # #

class Element(Common):
    '''
    Abstract base class for Level 1.
    '''
    class Meta(Common.Meta):
        abstract = True

    properties = models.ManyToManyField(Property)
    purposes = models.ManyToManyField(Purpose)
    keywords = models.ManyToManyField(Keyword)


class Relation(Common):
    '''
    Relationships between elements.
    '''
    PREDICATES = (
        ('child', 'is child of'),
        ('cause', 'is caused by'),
        ('type', 'is type of'),
        ('part', 'is part of'),
        ('attract', 'is attracted to'),
        ('control', 'is controlled by'),
        ('subject', 'is subject of')
    )
    subject = models.ForeignKey(Element)
    recipient = models.ForeignKey(Element)
    name = models.CharField(
        max_length=10, required=True, choices=PREDICATES, default='child')


class Aspect(Common):
    '''
    A type of representation, like an angle or perspective, usually for Image or Plan.
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
    name = models.CharField(
        max_length=10, unique=True, required=True,
        choices=CHOICES, default='primary')


class Image(Common):
    '''
    A representation of an element, usually graphical.  Contrast with 'Plan'.
    '''
    element = models.ForeignKey(Element)
    aspect = models.ForeignKey(Aspect)

    image = models.ImageField(width_field=width, height_field=height)
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()


class Plan(Common):
    '''
    A model or defining document for an element, usually graphical.  Contrast with 'Image'.
    '''
    element = models.ForeignKey(Element)
    aspect = models.ForeignKey(Aspect)

    file = models.FileField()


class Span(Element):
    '''
    Defined by boundaries.
    '''
    boundary = models.ManyToManyField(Location)


class Item(Element):
    '''
    Defined by characteristics.
    '''
    location = models.ForeignKey(Location)


# # # # # #
# Level 2 #
# # # # # #
