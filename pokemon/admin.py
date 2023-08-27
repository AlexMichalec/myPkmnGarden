from django.contrib import admin

# Register your models here.

from .models import PokemonType, PokemonGeneration, PokemonSpecies, PokemonMonster

admin.site.register(PokemonType)
admin.site.register(PokemonGeneration)
admin.site.register(PokemonSpecies)
admin.site.register(PokemonMonster)
