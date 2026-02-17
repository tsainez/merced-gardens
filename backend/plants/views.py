from django.shortcuts import render, get_object_or_404
from .models import Plant

def plant_detail(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    care_events = plant.care_events.all().order_by('-date')
    return render(request, 'plants/plant_detail.html', {'plant': plant, 'care_events': care_events})
