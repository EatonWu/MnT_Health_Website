from django.db import models
from django.urls import reverse


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
    age = models.IntegerField(max_length=3, help_text='Enter age.')
    weight = models.IntegerField(max_length=4, help_text='Enter weight.')
    height = models.IntegerField(max_length=3, help_text='Enter height.')
    gender = models.CharField(max_length=1, help_text='Enter gender (M or F).')

    # Metadata
    class Meta:
        ordering = ['-my_field_name']

    def __str__(self):
        return self.first_name + self.last_name

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
