from django.shortcuts import render
from .models import User, CalorieCalc, FitnessPlan


# Create your views here.

def index(request):
    return render(request, 'index.html')
