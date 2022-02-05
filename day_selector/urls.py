from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:day>/', views.day_selected, name='day_selected')
]