from django.contrib import admin

# Register your models here.
from who.models import Person, Group

admin.site.register(Person)
admin.site.register(Group)