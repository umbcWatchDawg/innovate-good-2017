from django.db import models
from django.core.validators import validate_comma_separated_integer_list
from django.contrib.auth.models import User as AuthedUser

class Crime(models.Model):

    CRIME_TYPES = {
        ('ast', 'Assault'),
        ('ca', 'Car Accident'),
        ('hsmt', 'Harassment'),
        ('tft', 'Theft'),
        ('oth', 'Other')
    }

    user_key = models.ForeignKey(AuthedUser,on_delete=models.CASCADE)
    is_victim = models.NullBooleanField()
    crime_type = models.CharField(max_length=1000,null=True,choice=CRIME_TYPES)
    date = models.DateTimeField('incident date and time')
    location = models.CharField(max_length=250,null=True)
    elements = models.CharField(max_length=150,validators=[validate_comma_separated_integer_list],null=True)
