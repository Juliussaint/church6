from django.urls import path
from . import views

urlpatterns = [
    path('', views.pelkat_index, name='pelkat-index'),
    path('<slug:slug>/', views.pelkat_detail, name='pelkat-detail'),
    path('<slug:slug>/event/<int:event_id>/', views.pelkat_event_detail, name='pelkat-event-detail'),
]
