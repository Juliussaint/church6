# home/models.py

from django.db import models
from django.urls import reverse

class Pelayanan(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True)
    ikon = models.CharField(max_length=50, help_text="Gunakan nama ikon bootstrap atau ikon FontAwesome.")
    slug = models.SlugField(unique=True)
    url_target = models.CharField(max_length=100, help_text="Contoh: 'pelkat-index', 'musik:index'", blank=True)

    def __str__(self):
        return self.nama

    def get_absolute_url(self):
        if self.url_target:
            return reverse(self.url_target)
        return "#"
