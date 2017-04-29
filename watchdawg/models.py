from django.db import models

# Create your models here.

class Crime(models.Model):
    is_victim = models.BooleanField(False)
    crime_type = models.CharField(max_length=400)
    date = models.DateTimeField('incident date and time')
    location = models.CharField(max_length=250)
    elements = models.CharField(max_length=150,validators=[validate_comma_separated_integer_list])
