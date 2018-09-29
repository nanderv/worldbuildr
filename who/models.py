from django.db import models

# Create your models here.
from django.db.models import CharField, DateField, ManyToManyField, ForeignKey

from base.models import Significance


class Who (Significance):
    name = CharField(max_length=255)


class Person (Who):
    dateOfBirth = DateField()
    dateOfDeath = DateField()


class Group (Who):
    pass


class MemberOf(Significance):
    member = ForeignKey(Who, on_delete=models.CASCADE, related_name='memberMemberOf')
    of = ForeignKey(Group, on_delete=models.CASCADE, related_name='ofMemberOf')
    fromDate = DateField()
    toDate = DateField()
