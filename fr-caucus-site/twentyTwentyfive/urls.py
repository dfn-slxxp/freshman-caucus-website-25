from django.urls import path

from . import views

urlpatterins = [
    path('', views.home),
]