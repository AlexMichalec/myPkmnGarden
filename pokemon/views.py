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
                                 gender=random.choice(("Male","Female")))
    new_pokemon.save()
    return redirect('home')

def pokemon_page(request, pokemon_id):
    context = {
        'pokemon': PokemonMonster.objects.get(id=pokemon_id),
    }
    return render(request, 'pokemon/pokemon_page.html', context)

def explore(request, where=None):
    if where is None:
        if request.method == 'POST':
            where = request.POST['choice'].lower()
        else:
            return render(request,'pokemon/explore_choice.html')

    next_step = random.randint(1, 10)
    to_post = "..."
    if request.method == 'POST':
        if PokemonSpecies.objects.filter(name=request.POST['choice']).count():
            to_post = request.POST['choice']
            lines = ["*" for i in range(random.randint(3, 7))]
            if next_step < 6:
                lines.append("Pokemon escaped from Pokeball")
                lines.append("What are you doing?")
                buttons = [(to_post,"Try to catch it(again)"), ("F","Flee")]
            elif next_step <8:
                lines.append("Pokemon escaped from Pokeball")
                lines.append("It disappeared into the forest")
                lines.append("Which way now?")
                buttons = [("L","Left"), ("S","Straight ahead"), ("R","Right")]
            else:
                lines.append("Success!")
                lines.append("You caught: " + to_post)
                lines.append("Which way now?")
                buttons = [("L","Left"), ("S","Straight ahead"), ("R","Right")]
                p = PokemonMonster(species=PokemonSpecies.objects.get(name=to_post),
                               level=random.randint(3,10),
                               owner=request.user,
                                gender=random.choice(("Male","Female")))
                if p.species.if_genderless:
                    p.gender="Unknown"
                p.save()
            context = {'where': where,
                       'to_post': to_post,
                    'lines': lines,
                   'buttons': buttons, }
            return render(request, 'pokemon/explore.html', context)

    lines = [random.randint(0, 30) for i in range(random.randint(3, 7))]
    lines = ["." * (5 + i) + "walk" + "." * (40 - i) for i in lines]
    if next_step <8:
        lines.append("Which way now?")
        buttons = [("L","Left"), ("S","Straight ahead"), ("R","Right")]
    else:
        lines.append("Wild pokemon appeared!")
        to_post = random_pokemon_name(where)
        lines.append("It's " + to_post)
        lines.append("What are you doing?")
        buttons = [(to_post,"Try to catch it"), ("F","Flee")]


    context ={'where': where,
              'to_post': to_post,
              'lines': lines,
              'buttons': buttons,}
    return render(request, 'pokemon/explore.html', context)

def random_pokemon_name(where='hujwie'):
    all = list(PokemonSpecies.objects.filter(if_starter=False))
    if where == "sea":
        type = PokemonType.objects.get(name='Water')
        all = list(PokemonSpecies.objects.filter(if_starter=False).filter(type=type))

    elif where == "forest":
        type1 = PokemonType.objects.get(name='Grass')
        type2 = PokemonType.objects.get(name='Bug')
        type3 = PokemonType.objects.get(name='Normal')
        all = list(PokemonSpecies.objects.filter(if_starter=False).filter(type=type1)) + list(PokemonSpecies.objects.filter(if_starter=False).filter(type=type2)) + list(PokemonSpecies.objects.filter(if_starter=False).filter(type=type3))

    elif where == "cave":
        type1 = PokemonType.objects.get(name='Rock')
        type2 = PokemonType.objects.get(name='Ground')
        type3 = PokemonType.objects.get(name='Steel')
        all = list(PokemonSpecies.objects.filter(if_starter=False).filter(type=type1)) + list(
            PokemonSpecies.objects.filter(if_starter=False).filter(type=type2)) + list(
            PokemonSpecies.objects.filter(if_starter=False).filter(type=type3))
        all.append(PokemonSpecies.objects.get(name="Zubat"))

    return random.choice(all).name