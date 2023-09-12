import random

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
    short_description = models.CharField(max_length=200)
    description = models.TextField()

    picture_source = models.CharField(max_length=200, blank=True)

    generation = models.ForeignKey(PokemonGeneration,on_delete=models.CASCADE)
    national_pokedex_number = models.IntegerField(unique=True)
    type = models.ManyToManyField(PokemonType)

    if_starter = models.BooleanField(default=False)
    if_genderless = models.BooleanField(default=False)
    if_legendary = models.BooleanField(default=False)
    if_baby = models.BooleanField(default=False)

    if_evolve_by_level_up = models.BooleanField(default=False)
    evolve_level = models.IntegerField(default=0)
    evolve_species = models.ManyToManyField('PokemonSpecies',blank=True)

    def is_caught(self, request):
        return request.user.pokemonmonster_set.all().filter(species=self).count()>0



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
    exp = models.IntegerField(editable=False,default=-1)

    gender = models.CharField(max_length=7,choices=(("MALE", "Male"),("FEMALE","Female"),("UNKNOWN","Unknown")), default="MALE")

    def get_exp(self):
        if self.exp<=self.level**3:
           self.exp = self.level**3
        return self.exp

    def add_exp(self, points):
        self.get_exp()
        self.exp += points
        self.exp = min(self.exp, 1000000)
        was_leveled_up = False
        while self.exp >= (self.level+1)**3:
            self.level_up()
            was_leveled_up = True
        return was_leveled_up

    def level_up(self):
        if self.level == 100:
            return False
        self.level += 1
        if self.species.if_evolve_by_level_up:
            if self.level >= self.species.evolve_level:
                self.evolve()
                return True
        return False
        # attacks?

    def evolve(self):
        if self.species.evolve_species.count()==0:
            return False
        if self.species.evolve_species.count()>1:
            new_species = list(self.species.evolve_species.all())
            self.species = random.choice(new_species)
        else:
            self.species = self.species.evolve_species.all()[0]
        return True

        #attacks?


    def __str__(self):
        if self.name is None:
            return f"{self.species.name} [{str(self.level)}]"
        else:
            return f"{self.name} ({self.species.name}) [{str(self.level)}]"


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    picture_source = models.CharField(max_length=200)
    value = models.IntegerField()
    def __str__(self):
        return self.name

class EvolveItem(Item):
    pokemons = models.ManyToManyField(PokemonSpecies, blank=True)

class Pokeball(Item):
    chance_of_catching = models.FloatField()
