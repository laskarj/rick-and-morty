import requests

from django.conf import settings
from django.db import IntegrityError
from characters.models import Character


def scrape_characters() -> [Character]:
    next_url_to_scrape = settings.RICK_AND_MORTY_API_CHARACTERS_URL

    characters = []
    while next_url_to_scrape is not None:
        characters_response = requests.get(next_url_to_scrape).json()
        for characters_data in characters_response["results"]:
            characters.append(
                Character(
                    api_id=characters_data["id"],
                    name=characters_data["name"],
                    status=characters_data["status"],
                    species=characters_data["species"],
                    gender=characters_data["gender"],
                    image=characters_data["image"],
                )
            )
        next_url_to_scrape = characters_response["info"]["next"]

    return characters


def save_characters(characters: [Character]) -> None:
    for character in characters:
        try:
            character.save()
        except IntegrityError:
            print(f"Character already exist with {character.api_id} id")


def sync_characters_with_api() -> None:
    characters = scrape_characters()
    save_characters(characters)
