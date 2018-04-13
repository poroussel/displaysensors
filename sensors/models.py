# -*- coding: utf-8 -*-

from django.db import models


class Sensor(models.Model):
    TYPES = (('i', u'Integer'),
             ('f', u'Float'),
             ('b', u'Boolean'))

    code = models.CharField(max_length=20)
    name = models.CharField(max_length=80)
    value_type = models.CharField(max_length=1, default='v', choices=TYPES)
    active = models.BooleanField(default=False, editable=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Reading(models.Model):
    sensor = models.ForeignKey(Sensor)
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.DecimalField(max_digits=8, decimal_places=3)
