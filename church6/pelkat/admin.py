from django.contrib import admin
from .models import (
    PelayananKategorial,
    GalleryImage,
    Schedule,
    Pengurus,
    PelkatEvent,
    PelkatEventImage,
)

class GalleryInline(admin.TabularInline):
    model = GalleryImage
    extra = 1

class ScheduleInline(admin.StackedInline):
    model = Schedule
    extra = 0

class PengurusInline(admin.StackedInline):
    model = Pengurus
    extra = 1

class EventInline(admin.StackedInline):
    model = PelkatEvent
    extra = 0

class PelkatEventImageInline(admin.TabularInline):  # atau StackedInline
    model = PelkatEventImage
    extra = 3  # Jumlah form kosong awal yang ditampilkan

@admin.register(PelayananKategorial)
class PelayananKategorialAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [GalleryInline, ScheduleInline, PengurusInline, EventInline]

@admin.register(PelkatEvent)
class PelkatEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'pelkat', 'date', 'location')
    list_filter = ('pelkat', 'date')
    search_fields = ('title', 'description', 'location')
    inlines = [PelkatEventImageInline] 
