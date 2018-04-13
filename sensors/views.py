# -*- coding: utf-8 -*-

from rest_framework import viewsets
from .models import Sensor, Reading
from .serializers import SensorSerializer, ReadingSerializer


class SensorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sensors to be viewed or edited.
    """
    queryset = Sensor.objects.all().order_by('-created')
    serializer_class = SensorSerializer


class ReadingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows readings to be viewed or edited.
    """
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer
