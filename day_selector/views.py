from django.shortcuts import render
from django.http import HttpResponse
from forms import forms

# The index will prompt users for a number of days
def index(request):
    if request.method == "POST":
        form = forms.DayForm(request.POST)

        if form.is_valid():
            return HttpResponse(form.cleaned_data['day'])
    else:
        form = forms.DayForm()

    return render(request, 'day_selector/index.html', {'form': form})


def day_selected(request, day):
    if 1 <= day <= 6:
        return HttpResponse("%s" % day)
    else:
        return HttpResponse("Invalid number of days")