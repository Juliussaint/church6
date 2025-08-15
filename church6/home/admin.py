# home/admin.py
from django.contrib import admin
from .models import Pelayanan

@admin.register(Pelayanan)
class PelayananAdmin(admin.ModelAdmin):
    list_display = ['nama', 'slug', 'url_target']
    prepopulated_fields = {"slug": ("nama",)}
