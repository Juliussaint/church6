from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class PelayananKategorial(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = CKEditor5Field('Text', config_name='extends')
    logo = models.ImageField(upload_to='logos/pelkat/', blank=True, null=True)
    banner = models.ImageField(upload_to='banners/pelkat/', blank=True, null=True)

    class Meta:
        verbose_name = "Pelayanan Kategorial"
        verbose_name_plural = "Pelayanan Kategorial"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def latest_event(self):
        return self.events.filter(date__lte=timezone.now()).order_by('-date').first()


class GalleryImage(models.Model):
    pelkat = models.ForeignKey(PelayananKategorial, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='gallery/pelkat/')
    caption = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.pelkat.name}"


class Schedule(models.Model):
    pelkat = models.ForeignKey(PelayananKategorial, on_delete=models.CASCADE, related_name='schedules')
    title = models.CharField(max_length=100)
    day = models.CharField(max_length=20)  # e.g., "Minggu", "Sabtu"
    time = models.TimeField()
    location = models.CharField(max_length=200, blank=True)
    description = CKEditor5Field('Text', config_name='extends', blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.day} at {self.time}"


class Pengurus(models.Model):
    pelkat = models.ForeignKey(PelayananKategorial, on_delete=models.CASCADE, related_name='pengurus')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='pengurus/pelkat/', blank=True, null=True)
    contact_number = models.CharField(
        max_length=20, 
        blank=True, 
        null=True,
        help_text="Masukkan nomor WhatsApp tanpa spasi atau tanda +, misalnya: 6281944848000"
    )  

    def __str__(self):
        return f"{self.name} - {self.position}"


class PelkatEvent(models.Model):
    pelkat = models.ForeignKey(PelayananKategorial, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=200)
    description = CKEditor5Field('Text', config_name='extends')
    date = models.DateField()
    location = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='events/pelkat/', blank=True, null=True)
    
    class Meta:
        ordering = ['-date']  # Latest events first
        verbose_name = "Event Pelkat"
        verbose_name_plural = "Event Pelkat"

    def __str__(self):
        return f"{self.title} ({self.date})"
    

class PelkatEventImage(models.Model):
    event = models.ForeignKey(PelkatEvent, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='events/pelkat/gallery/')
    caption = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Foto Event Pelkat"
        verbose_name_plural = "Foto-Foto Event Pelkat"

    def __str__(self):
        return f"Gambar untuk {self.event.title}"
