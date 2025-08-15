from django.shortcuts import render, get_object_or_404
from .models import PelayananKategorial, PelkatEvent, PelkatEventImage


def pelkat_index(request):
    pelkats = PelayananKategorial.objects.all()
    return render(request, "pelkat/pelkat_index.html", {
        'title': 'Pelayanan Kategorial',
        'description': 'Pelayanan Kategorial Gereja',
        'keywords': 'pelayanan, kategorial, gereja, jemaat',
        'pelkats': pelkats,
    })


# Detail View
def pelkat_detail(request, slug):
    pelkat = get_object_or_404(PelayananKategorial, slug=slug)

    gallery = pelkat.gallery.all()
    schedules = pelkat.schedules.all()
    pengurus = pelkat.pengurus.all()
    latest_event = pelkat.latest_event()

    return render(request, 'pelkat/pelkat_detail.html', {
        'pelkat': pelkat,
        'gallery': gallery,
        'schedules': schedules,
        'pengurus': pengurus,
        'latest_event': latest_event,
    })

def pelkat_event_detail(request, slug, event_id):
    pelkat = get_object_or_404(PelayananKategorial, slug=slug)
    event = get_object_or_404(PelkatEvent, id=event_id, pelkat=pelkat)
    event_images = PelkatEventImage.objects.filter(event=event)

    return render(request, 'pelkat/pelkat_event_detail.html', {
        'pelkat': pelkat,
        'event': event,
        'images': event_images,
    })
