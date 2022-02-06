from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='fitness_index'),
    path('success/', views.index),
]