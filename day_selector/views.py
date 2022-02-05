from django.shortcuts import render
from django.http import HttpResponse

# The index will prompt users for a number of days
def index(request):
    return HttpResponse("Day Selection Page")

def day_selected(request, day):
    if 1 <= day <= 6:
        return HttpResponse("%s" % day)
    else:
        return HttpResponse("Invalid number of days")