from django.contrib import admin
from .models import User, CalorieCalc, FitnessPlan

# Register your models here.
admin.site.register(User)
admin.site.register(CalorieCalc)
admin.site.register(FitnessPlan)
