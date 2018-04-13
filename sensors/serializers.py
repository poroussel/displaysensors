# -*- coding: utf-8 -*-

from sensors.models import Sensor, Reading
from rest_framework import serializers


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ('url', 'code', 'name', 'value_type', 'active')


class ReadingSerializer(serializers.HyperlinkedModelSerializer):
    sensor = serializers.StringRelatedField()

    class Meta:
        model = Reading
        fields = ('url', 'timestamp', 'value', 'sensor')
