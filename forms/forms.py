from django import forms
from django.urls import reverse


class DayForm(forms.Form):
    day = forms.IntegerField(label='How many days of the week do you want to exercise?', max_value=6, min_value=1)


class CalorieForm(forms.Form):
    age = forms.IntegerField(label='Enter age:', help_text='\n', min_value=0)
    weight = forms.IntegerField(label='Enter weight:', help_text='\n', min_value=0)
    height = forms.IntegerField(label='Enter height:', help_text='\n', min_value=0)

    GENDER_ID = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    gender = forms.CharField(
        max_length=1,
        widget=forms.Select(choices=GENDER_ID),
        label='Select gender:',
        help_text='\n'
    )

    ACTIVITY_LEVEL = (
        ('s', 'Sedentary'),
        ('l', 'Light Activity'),
        ('m', 'Moderate Activity'),
        ('v', 'Very Active'),
        ('e', 'Extremely Active')
    )

    activity = forms.CharField(
        max_length=1,
        widget=forms.Select(choices=ACTIVITY_LEVEL),
        label='Select activity level:',
        help_text='\n'
    )

    GOAL_WEIGHT = (
        ('l', 'Lose Weight'),
        ('m', 'Maintain'),
        ('g', 'Gain Weight')
    )

    goal = forms.CharField(
        max_length=1,
        widget=forms.Select(choices=GOAL_WEIGHT),
        label='Select weight goal:',
        help_text='\n'
    )
