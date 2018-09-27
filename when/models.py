from django.db import models

# Create your models here.
from django.db.models import IntegerField, ForeignKey, CharField

from base.models import Significance


class Era (Significance):
    yearEnded = IntegerField()
    yearStarted = IntegerField()
    firstYear = IntegerField()
    name = CharField(max_length=255)


class Moment (models.Model):
    day = IntegerField()
    month = IntegerField()
    year = IntegerField()


class Period (Significance):
    pass
