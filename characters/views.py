from random import choice

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from characters.models import Character
from characters.serializers import CharacterSerializer


@api_view(["GET"])
def get_random_character_view(requests: Request) -> Response:
    pks = Character.objects.values_list("pk", flat=True)
    random_id = choice(pks)
    random_character = Character.objects.get(pk=random_id)
    serializer = CharacterSerializer(random_character)
    return Response(serializer.data, status=status.HTTP_200_OK)
