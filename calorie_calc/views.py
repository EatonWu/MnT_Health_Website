from django.shortcuts import render, redirect
from django.http import HttpResponse
from forms import forms
from backend import calorie_calc
from healthhacks.models import User, CalorieCalc


# Create your views here.
def index(request):
    user = list(User.objects.filter(username__exact=request.user.username))[0]
    calculated = bool(user.calorie_count)

    calorie_count = 0
    if calculated:
        calorie_count = user.calorie_count.get_goal()

    if request.method == "POST":
        form = forms.CalorieForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            if user.calorie_count:
                user.calorie_count.delete()

            calorie = CalorieCalc(age=data['age'], weight=data['weight'], height=data['height'], gender=data['gender'],
                        activity=data['activity'], goal=data['goal'])
            calorie.save()
            user.calorie_count = calorie
            user.save()
            return redirect('calorie_complete')
    else:
        form = forms.CalorieForm()

    context = {
        'form': form,
        'calculated': calculated,
        'calorie_count': calorie_count,
    }

    return render(request, 'calorie_calc/index.html', context=context)


def day_selected(request, day):
    if 1 <= day <= 6:
        return HttpResponse("%s" % day)
    else:
        return HttpResponse("Invalid number of days")


def calculate_success(request):
    user = list(User.objects.filter(username__exact=request.user.username))[0]
    cal = user.calorie_count

    context = {
        'calorie_goal': cal.get_goal(),
    }

    return render(request, 'calorie_calc/complete.html', context=context)
