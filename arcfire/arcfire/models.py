from django.db import models

# # # # # # # # #
# Bootstrapping #
# # # # # # # # #

class Domain(models.Model):
    '''
    The fundamental model in this system.
    '''
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    scale = 0
    sentience = 0
    entropy = 0
    distance = 0

    attributes = models.ForeignKey(Attribute)
    images = models.ForeignKey(Image)
    kinds = models.ForeignKey(Kind)
    locations = models.ForeignKey(Location)
    purposes = models.ForeignKey(Purpose)
    plans = models.ForeignKey(Plan)
    relations = models.ForeignKey(Relation)
    subjects = models.ForeignKey(Subject)
    times = models.ForeignKey(Time)


class Attribute(models.Model):
    '''
    '''
    pass


class Image(models.Model):
    '''
    '''
    pass


class Kind(models.Model):
    '''
    '''
    pass


class Location(models.Model):
    '''
    '''
    pass


class Plan(models.Model):
    '''
    '''
    pass

class Purpose(models.Model):
    '''
    '''
    pass


class Relation(models.Model):
    '''
    '''
    pass


class Subject(models.Model):
    '''
    '''
    pass


class Time(models.Model):
    '''
    '''
    pass


class Span(Domain):
    '''
    Defined by boundaries.
    '''
    pass


class Item(Domain):
    '''
    Defined by characteristics.
    '''
    pass


# # # # # # # #
# Derivatives #
# # # # # # # #
