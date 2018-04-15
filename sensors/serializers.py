# -*- coding: utf-8 -*-

from sensors.models import Sensor, Reading
from rest_framework import serializers


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'url', 'code', 'name', 'value_type', 'active')


class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = ('id', 'url', 'timestamp', 'value', 'sensor')
