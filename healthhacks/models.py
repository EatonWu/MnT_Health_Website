import math

from django.db import models
from django.urls import reverse
from backend.calorie_calc import *


# Create your models here.

class User(models.Model):
    # fields
    first_name = models.CharField(max_length=20, help_text='Enter first name.')
    last_name = models.CharField(max_length=20, help_text='Enter last name.')
    email = models.CharField(max_length=40, help_text='Enter email.')
    username = models.CharField(max_length=150, help_text='Enter username.', default="user")
    calorie_count = models.ForeignKey("CalorieCalc", on_delete=models.SET_NULL, null=True)
    fitness_plan = models.ForeignKey("FitnessPlan", on_delete=models.SET_NULL, null=True)

    # Metadata
    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return f'{self.username}'


class CalorieCalc(models.Model):
    age = models.PositiveSmallIntegerField(help_text='Enter age.')
    weight = models.PositiveSmallIntegerField(help_text='Enter weight (lbs).')
    height = models.PositiveSmallIntegerField(help_text='Enter height (inches).')

    GENDER_ID = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    gender = models.CharField(
        max_length=1,
        choices=GENDER_ID,
        blank=True,
        default='M',
        help_text='Enter gender.'
    )

    ACTIVITY_LEVEL = (
        ('s', 'Sedentary'),
        ('l', 'Light'),
        ('m', 'Moderate'),
        ('v', 'Very'),
        ('e', 'Extremely')
    )

    activity = models.CharField(
        max_length=1,
        choices=ACTIVITY_LEVEL,
        blank=True,
        default='s',
        help_text='Select your level of daily activity.'
    )

    GOAL_WEIGHT = (
        ('l', 'Lose Weight'),
        ('m', 'Maintain'),
        ('g', 'Gain Weight')
    )

    goal = models.CharField(
        max_length=1,
        choices=GOAL_WEIGHT,
        blank=True,
        default='m',
        help_text='Select your weight goal.'
    )

    # Metadata
    class Meta:
        ordering = ['-age']

    def get_goal(self):
        bmr = calculate_BMR(self.gender, self.weight, self.height, self.age)
        return str(math.floor(find_goal(bmr, self.activity, self.goal))) + " calories"

    def __str__(self):
        return f'{self.get_goal()}'


class Exercise(models.Model):
    name = models.CharField(max_length=100)


class FitnessPlan(models.Model):
    WORKOUT_DAYS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7')
    )

    days = models.PositiveSmallIntegerField(
        primary_key=True,
        choices=WORKOUT_DAYS,
        blank=True,
        default=1,
        help_text='Choose how many days you will work out in a week.'
    )

    workout_desc = models.CharField(max_length=3000, help_text='', default='')

    # Metadata
    class Meta:
        ordering = ['-days']

    def __str__(self):
        return f'{self.days}'
