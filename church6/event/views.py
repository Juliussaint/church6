from django.shortcuts import render, get_object_or_404
from .models import Event
from django.utils import timezone

def event_list(request):
    events = Event.objects.order_by('-date')
    return render(request, 'event/event_list.html', {
        'events': events,
        'now': timezone.now(),
    })

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'event/event_detail.html', {'event': event})
