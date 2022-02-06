from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from forms import forms
from healthhacks.models import *


# The index will prompt users for a number of days
# /dayselector/
@login_required(login_url='/healthhacks/login')
def index(request):
    if request.method == "POST":
        form = forms.DayForm(request.POST)

        if form.is_valid():
            user = list(User.objects.filter(username__exact=request.user.username))[0]
            # return HttpResponse(form.cleaned_data['day'])
            # instead of returning form data, render the button html file
            if form.cleaned_data['day'] == 1:
                fit_plan = FitnessPlan.objects.get(pk=1)
                user.fitness_plan = fit_plan
            elif form.cleaned_data['day'] == 2:
                user.fitness_plan = FitnessPlan.objects.get(pk=2)
            elif form.cleaned_data['day'] == 3:
                user.fitness_plan = FitnessPlan.objects.get(pk=3)
            elif form.cleaned_data['day'] == 4:
                user.fitness_plan = FitnessPlan.objects.get(pk=4)
            elif form.cleaned_data['day'] == 5:
                user.fitness_plan = FitnessPlan.objects.get(pk=5)
            elif form.cleaned_data['day'] == 6:
                user.fitness_plan = FitnessPlan.objects.get(pk=6)
        return HttpResponse(user.fitness_plan.workout_desc)
    else:
        form = forms.DayForm()

    return render(request, 'day_selector/index.html', {'form': form})

# /day_selector/day
def day_selected(request, day):
    if 1 <= day <= 6:
        return HttpResponse("%s" % day)
    else:
        return HttpResponse("Invalid number of days")
