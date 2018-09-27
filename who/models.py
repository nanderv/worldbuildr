from django.db import models

# Create your models here.
from django.db.models import CharField, DateField, ManyToManyField, ForeignKey

from base.models import Significance


class Who (Significance):
    name = CharField(max_length=255)
    memberOf = ManyToManyField('MemberOf')


class Person (Who):
    dateOfBirth = DateField()
    dateOfDeath = DateField()


class Group (Who):
    pass


class MemberOf(Significance):
    member = ForeignKey(Who)
    of = ForeignKey(Group)
    fromDate = DateField()
    toDate = DateField()
