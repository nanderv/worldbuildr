from graphene import ObjectType
from graphene_django import DjangoObjectType
import graphene
from graphene_django.filter import DjangoFilterConnectionField

from who.models import *


class PersonNode(DjangoObjectType):
    class Meta:
        # Assume you have an Animal model defined with the following fields
        model = Person
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'id': ['exact'],
            'memberOf': ['exact'],

        }
        interfaces = (graphene.relay.Node,)


class Query(ObjectType):
    person = graphene.Field(PersonNode,
                            id=graphene.Int(),
                            name=graphene.String())
    all_persons = DjangoFilterConnectionField(PersonNode)

    def resolve_person(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Person.objects.get(pk=id)

        if name is not None:
            return Person.objects.get(name=name)

        return None
