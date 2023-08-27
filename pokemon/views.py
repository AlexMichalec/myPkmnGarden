from django.contrib.auth import login
from django.shortcuts import render, redirect, HttpResponse
from .models import PokemonSpecies, PokemonType, PokemonMonster
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import random


def home(request):
    if request.user.is_authenticated:
        pokemon_list = request.user.pokemonmonster_set.all()
        name = request.user.username
    else:
        pokemon_list = []
        name = ""
    context = {
        'name': name,
        'pokemon_list': pokemon_list,
    }
    return render(request,'pokemon/home.html', context)

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superuser)
def info(request):
    context = {
        'name': 'Alex',
        'pokemon_list': PokemonSpecies.objects.all().order_by('national_pokedex_number'),
        'type_list': PokemonType.objects.all().order_by('name'),
    }
    return render(request,'pokemon/info.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password doesn't match")


    context = {
        'page': 'login',
    }
    return render(request, 'pokemon/login_register.html', context)

def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('starters')
    context = {
        'form': form
    }
    return render(request, 'pokemon/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def starters(request):
    if request.user.pokemonmonster_set.count() > 0:
        return redirect('home')
    grass_list = PokemonType.objects.get(name='Grass').pokemonspecies_set.filter(if_starter=True)
    grass_starter = random.choice(grass_list)
    fire_list = PokemonType.objects.get(name='Fire').pokemonspecies_set.filter(if_starter=True)
    fire_starter = random.choice(fire_list)
    water_list = PokemonType.objects.get(name='Water').pokemonspecies_set.filter(if_starter=True)
    water_starter = random.choice(water_list)

    context = {
        'grass_starter': grass_starter,
        'fire_starter': fire_starter,
        'water_starter': water_starter,
    }
    return render(request, 'pokemon/starters.html', context)


@login_required(login_url='login')
def starter_chosen(request):
    if request.user.pokemonmonster_set.count() > 0:
        return redirect('home')
    new_pokemon = PokemonMonster(owner=request.user,
                                 species=PokemonSpecies.objects.get(name=request.POST['choice']),
                                 level=5,
                                 gender=random.choice(("MALE","FEMALE")))
    new_pokemon.save()
    return redirect('home')

def pokemon_page(request, pokemon_id):
    context = {
        'pokemon': PokemonMonster.objects.get(id=pokemon_id),
    }
    return render(request, 'pokemon/pokemon_page.html', context)