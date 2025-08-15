# home/views.py
from django.shortcuts import render
from .models import Pelayanan
from event.models import Event
from django.utils import timezone

def home_index(request):
    pelayanan_list = Pelayanan.objects.all()
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')[:3]  # upcoming
    return render(request, 'home/index.html', {
        'pelayanan_list': pelayanan_list,
        'events': events
    })

