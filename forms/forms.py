from django import forms
from django.urls import reverse


class DayForm(forms.Form):
    day = forms.IntegerField(label='How many days of the week do you want to exercise?', max_value=6, min_value=1)


class CalorieForm(forms.Form):
    age = forms.IntegerField(help_text='Enter age.')
    weight = forms.IntegerField(help_text='Enter weight.')
    height = forms.IntegerField(help_text='Enter height in inches.')

    GENDER_ID = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    gender = forms.CharField(
        max_length=1,
        widget=forms.Select(choices=GENDER_ID),
        help_text='Enter gender.'
    )

    ACTIVITY_LEVEL = (
        ('s', 'sedentary'),
        ('l', 'light'),
        ('m', 'moderate'),
        ('v', 'very'),
        ('e', 'extremely')
    )

    activity = forms.CharField(
        max_length=1,
        widget=forms.Select(choices=ACTIVITY_LEVEL),
        help_text='Select your level of daily activity.'
    )

    GOAL_WEIGHT = (
        ('l', 'Lose Weight'),
        ('m', 'Maintain'),
        ('g', 'Gain Weight')
    )

    goal = forms.CharField(
        max_length=1,
        widget=forms.Select(choices=GOAL_WEIGHT),
        help_text='Select your weight goal.'
    )
