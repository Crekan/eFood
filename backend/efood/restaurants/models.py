from django.core.validators import RegexValidator
from django.db import models


class Restaurant(models.Model):
    image = models.ImageField(upload_to='restaurant_images/', blank=True)
    name = models.CharField(max_length=250)
    working_hours = models.TextField(validators=[
        RegexValidator(
            regex=r'^([0-1][0-9]|2[0-3]):([0-5][0-9]) - ([0-1][0-9]|2[0-3]):([0-5][0-9])$',
            message='Enter the hours of operation in the format "HH:MM - HH:MM".'
        )
    ])

    def __str__(self):
        return self.name
