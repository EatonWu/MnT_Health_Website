from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='calorie_index'),
    path('complete', views.calculate_success, name='calorie_complete')
]