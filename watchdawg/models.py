from django.db import models
from django.core.validators import validate_comma_separated_integer_list
from django.contrib.models import User as AuthedUser

# Create your models here.

class Crime(models.Model):
    user_key = models.ForeignKey(AuthedUser, on_delete=models.CASCADE)
    is_victim = models.BooleanField(False)
    crime_type = models.CharField(max_length=1000)
    date = models.DateTimeField('incident date and time')
    location = models.CharField(max_length=250)
    elements = models.CharField(max_length=150,validators=[validate_comma_separated_integer_list])
