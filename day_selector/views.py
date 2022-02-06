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
            user.fitness_plan = FitnessPlan.objects.get(pk=form.cleaned_data['day'])
            return_http_response = render(request, 'just_navbar.html')
            return_http_response.write(user.fitness_plan.workout_desc)
        return return_http_response
    else:
        form = forms.DayForm()

    return render(request, 'day_selector/index.html', {'form': form})

# /day_selector/day
def day_selected(request, day):
    if 1 <= day <= 6:
        return HttpResponse("%s" % day)
    else:
        return HttpResponse("Invalid number of days")
