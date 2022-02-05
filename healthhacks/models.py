from django.db import models
from django.urls import reverse
import backend.calorie_calc


# Create your models here.

class MyModelName(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    ...

    # Metadata
    class Meta:
        ordering = ['-my_field_name']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name


class User(models.Model):
    # fields
    first_name = models.CharField(max_length=20, help_text='Enter first name.')
    last_name = models.CharField(max_length=20, help_text='Enter last name.')
    email = models.CharField(max_length=40, help_text='Enter email.')
    calorie_count = models.ForeignKey("CalorieCalc", on_delete=models.SET_NULL, null=True)
    fitness_plan = models.ForeignKey("FitnessPlan", on_delete=models.SET_NULL, null=True)

    # Metadata
    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return f'{self.first_name} ({self.last_name})'

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])


class CalorieCalc(models.Model):
    age = models.PositiveSmallIntegerField(help_text='Enter age.')
    weight = models.PositiveSmallIntegerField(help_text='Enter weight.')
    height = models.PositiveSmallIntegerField(help_text='Enter height in inches.')

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
        ('s', 'sedentary'),
        ('l', 'light'),
        ('m', 'moderate'),
        ('v', 'very'),
        ('e', 'extremely')
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

    BMR = backend.calorie_calc.calc(gender, weight, height, age)

    cals = backend.calorie_calc.cals(BMR, activity, goal)

    # Metadata
    class Meta:
        ordering = ['-age']

    def __str__(self):
        return f'{self.cals}'

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.cals)])


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
        choices=WORKOUT_DAYS,
        blank=True,
        default=1,
        help_text='Choose how many days you will work out in a week.'
    )

    # Metadata
    class Meta:
        ordering = ['-days']

    def __str__(self):
        return f'{self.days}'

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
