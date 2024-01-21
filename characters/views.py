from random import choice

from django.db.models.query import QuerySet
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

from characters.models import Character
from characters.serializers import CharacterSerializer


def get_random_character() -> Character:
    """Get random character from database"""
    pks = Character.objects.values_list("pk", flat=True)
    random_id = choice(pks)
    return Character.objects.get(pk=random_id)


@extend_schema(responses={status.HTTP_200_OK: CharacterSerializer})
@api_view(["GET"])
def get_random_character_view(requests: Request) -> Response:
    random_character = get_random_character()
    serializer = CharacterSerializer(random_character)
    return Response(serializer.data, status=status.HTTP_200_OK)


class CharacterListView(ListAPIView):
    serializer_class = CharacterSerializer

    def get_queryset(self) -> QuerySet:
        queryset = Character.objects.all()
        name = self.request.query_params.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="name",
                description="Filtering by name insensitive contains",
                required=False,
                location=OpenApiParameter.QUERY,
                type=OpenApiTypes.STR,
            )
        ]
    )
    def get(self, request: Request, *args, **kwargs) -> Response:
        """List characters with filter by names"""
        return super().get(request, *args, **kwargs)
