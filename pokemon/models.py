from django.db import models
from colorfield.fields import ColorField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class PokemonType(models.Model):
    name = models.CharField(max_length=100)
    color = ColorField(default='#FF0000')
    def __str__(self):
        return self.name

class PokemonGeneration(models.Model):
    region = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.pk} ({self.region})"

class PokemonSpecies(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    generation = models.ForeignKey(PokemonGeneration,on_delete=models.CASCADE)
    national_pokedex_number = models.IntegerField(unique=True)
    type = models.ManyToManyField(PokemonType)
    if_starter = models.BooleanField(default=False)
    if_genderless = models.BooleanField(default=False)
    if_legendary = models.BooleanField(default=False)
    #picture?
    #attacksset
    #another basic stats

    def __str__(self):
        return self.name

class PokemonMonster(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    species = models.ForeignKey(PokemonSpecies, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True )
    level = models.IntegerField(default=1,
                                validators=[
                                    MinValueValidator(1),
                                    MaxValueValidator(100)
                                ])
    gender = models.CharField(max_length=7,choices=(("MALE", "Male"),("FEMALE","Female"),("UNKNOWN","Unknown")), default="MALE")

    def __str__(self):
        if self.name is None:
            return f"{self.species.name} [{str(self.level)}]"
        else:
            return f"{self.name} ({self.species.name}) [{str(self.level)}]"
