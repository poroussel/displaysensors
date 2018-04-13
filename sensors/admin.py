from django.contrib import admin
from sensors.models import Sensor, Reading



admin.site.register(Sensor)
admin.site.register(Reading)
