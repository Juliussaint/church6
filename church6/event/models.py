from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field

class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = CKEditor5Field('Text', config_name='extends')
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    banner = models.ImageField(upload_to='events/event_banners/', blank=True, null=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']  # Latest first

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.date.date()}")
        super().save(*args, **kwargs)

    def is_upcoming(self):
        return self.date > timezone.now()

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
