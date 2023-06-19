from django.shortcuts import render
import matplotlib.pyplot as plt
# Create your views here.
from rest_framework import viewsets
from .models import Frequency
from .serializers import FrequencySerializer

from rest_framework.decorators import action
from rest_framework.response import Response

from django.http import FileResponse
from io import BytesIO

from rest_framework.decorators import action
from rest_framework.response import Response
import numpy as np
import matplotlib.pyplot as plt

class FrequencyViewSet(viewsets.ModelViewSet):
    queryset = Frequency.objects.all()
    serializer_class = FrequencySerializer

    @action(detail=False, methods=['GET'])
    def plot_frequencies(self, request):
        frequencies = Frequency.objects.all()
        values = [frequency.value for frequency in frequencies]
        # Generate x values from 0 to 2*pi with the same length as the frequency values
        x = np.linspace(0, 2*np.pi, len(values))
        # Generate y values using the frequency values as the amplitude of the sine wave
        y = np.sin(values * x)
        # Plot the sine wave
        plt.plot(x, y)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Sine Wave Plot')
        plt.show()
        return Response({'message': 'Sine wave plot generated'})

