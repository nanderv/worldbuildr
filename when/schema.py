from graphene_django import DjangoObjectType
import graphene

from when.models import Moment


class MomentG(DjangoObjectType):
    class Meta:
        model = Moment


class Query(graphene.ObjectType):
    moment = graphene.List(MomentG)
    oneMoment = graphene.List(MomentG)

    def resolve_moment(self, info):
        return Moment.objects.all()

    def resolve_oneMoment(self, info):
        return Moment.object.filter(id=info)


schema = graphene.Schema(query=Query)