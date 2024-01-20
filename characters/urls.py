from django.urls import path

from characters.views import get_random_character_view


urlpatterns = [
    path("characters/random", get_random_character_view, name="characters_random"),
]


app_name = "characters"
