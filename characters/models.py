from django.db import models
from django.utils.translation import gettext_lazy as _


class Character(models.Model):
    class StatusChoices(models.TextChoices):
        ALIVE = "Alive"
        DEAD = "Dead"
        UNKNOWN = "unknown"

    class GenderChoices(models.TextChoices):
        FEMALE = "Female"
        MALE = "Male"
        UNKNOWN = "unknown"
        GENDERLESS = "Genderless"

    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=StatusChoices.choices)
    species = models.CharField(max_length=255)
    gender = models.CharField(max_length=50, choices=GenderChoices.choices)
    image = models.URLField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name
