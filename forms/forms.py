from django import forms
from django.urls import reverse
from django.utils.safestring import mark_safe


class DayForm(forms.Form):
    day = forms.IntegerField(label=mark_safe('Select days of week you would like to exercise (1 - 6)'), max_value=6, min_value=1)


class CalorieForm(forms.Form):
    age = forms.IntegerField(label='Age (1-100):', help_text="", max_value=100, min_value=1, )
    weight = forms.IntegerField(help_text='Enter weight (lbs).', max_value=600, min_value=50)
    height = forms.IntegerField(help_text='Enter height (inches).', max_value=120, min_value=30)

    GENDER_ID = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    gender = forms.CharField(
        max_length=1,
        widget=forms.RadioSelect(choices=GENDER_ID),
        help_text='Enter gender.'
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
        widget=forms.RadioSelect(choices=ACTIVITY_LEVEL),
        help_text='Select activity level:'
    )

    GOAL_WEIGHT = (
        ('l', 'Lose Weight'),
        ('m', 'Maintain'),
        ('g', 'Gain Weight')
    )

    goal = forms.CharField(
        max_length=1,
        widget=forms.RadioSelect(choices=GOAL_WEIGHT),
        help_text='Select your weight goal.'
    )
