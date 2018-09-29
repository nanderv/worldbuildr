import when.schema
import graphene

from graphene_django.debug import DjangoDebug

import who.schema


class Query(when.schema.Query, who.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
