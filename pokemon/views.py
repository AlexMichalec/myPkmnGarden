from django.contrib.auth import login
from django.shortcuts import render, redirect, HttpResponse
from .models import PokemonSpecies, PokemonType, PokemonMonster
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import random
import time

def random_pokemon_name(where=None, legendary=True):
    if legendary:
        base = PokemonSpecies.objects.filter(if_starter=False)
    else:
        base = PokemonSpecies.objects.filter(if_starter=False).filter(if_legendary=False)
    all = list(base)

    if where == "sea":
        type = PokemonType.objects.get(name='Water')
        all = list(base.filter(type=type))

    elif where == "forest":
        type1 = PokemonType.objects.get(name='Grass')
        type2 = PokemonType.objects.get(name='Bug')
        type3 = PokemonType.objects.get(name='Normal')
        all = list(base.filter(type=type1)) + list(
            base.filter(type=type2)) + list(base.filter(type=type3))

    elif where == "cave":
        type1 = PokemonType.objects.get(name='Rock')
        type2 = PokemonType.objects.get(name='Ground')
        type3 = PokemonType.objects.get(name='Steel')
        all = list(base.filter(if_starter=False).filter(if_legendary=False).filter(type=type1)) + list(
            base.filter(if_starter=False).filter(type=type2)) + list(
            base.filter(if_starter=False).filter(type=type3))
        all = all + [PokemonSpecies.objects.get(name="Zubat")]*100

    elif where == "volcano":
        type1 = PokemonType.objects.get(name='Fire')
        all = list(base.filter(type=type1))

    elif where == "tundra":
        type1 = PokemonType.objects.get(name='Ice')
        all = list(base.filter(type=type1))

    elif where == "graveyard":
        type1 = PokemonType.objects.get(name='Dark')
        type2 = PokemonType.objects.get(name='Psychic')
        type3 = PokemonType.objects.get(name='Ghost')
        all = list(base.filter(type=type1)) + list(
            base.filter(type=type2)) + list(
            base.filter(type=type3))

    result=random.choice(all)
    if where:
        while result.if_baby or (len(result.pokemonspecies_set.all())>0 and not result.pokemonspecies_set.all()[0].if_baby):
            result = random.choice(all)


    return result.name


def home(request):
    if request.method=="POST":
        return redirect("pokemon_page",pokemon_id=request.POST["choice"])

    context={}
    if request.user.is_authenticated:
        pokemon_list = list(request.user.pokemonmonster_set.all())
        garden_pokemon_list = pokemon_list[:]
        random.shuffle(garden_pokemon_list)
        garden_pokemon_list = garden_pokemon_list[:10]
        temp = []
        for g in garden_pokemon_list:
            top = random.randint(40,80)
            left = random.randint(0,85)
            width = random.randint(5,20)
            style = f" top: {top}%; left: {left}%; width: {width}%"
            temp.append({'pokemon': g, 'style': style})
        garden_pokemon_list = temp
        name = request.user.username
        context = {
            'username': name,
            'pokemon_list': pokemon_list,
            'garden_pokemon_list': garden_pokemon_list,
        }

    return render(request, 'pokemon/home.html', context)


@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superuser)
def info(request):
    evolution_list=[]
    temp = PokemonSpecies.objects.all().order_by('national_pokedex_number').filter(if_evolve_by_level_up=True)
    for t in temp:
        for x in t.evolve_species.all():
            evolution_list.append(f"#{t.national_pokedex_number} {t.name} --{t.evolve_level}lv.--> {x.name}")

    context = {
        'name': 'Alex',
        'pokemon_list': PokemonSpecies.objects.all().order_by('national_pokedex_number'),
        'type_list': PokemonType.objects.all().order_by('name'),
        'evolution_list': evolution_list,
    }
    return render(request, 'pokemon/info.html', context)


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

@login_required(login_url='login')
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
                                 gender=random.choice(("Male", "Female")))
    new_pokemon.save()
    return redirect('home')

@login_required(login_url='login')
def pokemon_page(request, pokemon_id):
    if PokemonMonster.objects.get(id=pokemon_id).owner != request.user:
        return redirect('home')
    context = {
        'pokemon': PokemonMonster.objects.get(id=pokemon_id),
    }
    return render(request, 'pokemon/pokemon_page.html', context)

@login_required(login_url='login')
def explore(request, where=None):
    if where is None:
        if request.method == 'POST':
            where = request.POST['choice'].lower()
        else:
            return render(request, 'pokemon/explore_choice.html')

    next_step = random.randint(1, 10)
    pokemon = "..."
    pokemon_pic_src = None
    where_pic = 'pokemon/images/' + where + '.jpg'
    if request.method == 'POST' and PokemonSpecies.objects.filter(name=request.POST['choice']).count():
        pokemon = request.POST['choice']
        lines = ["*" for i in range(random.randint(3, 7))]
        if next_step < 6:
            pokemon_pic_src = PokemonSpecies.objects.get(name=pokemon).picture_source
            lines.append("Pokemon escaped from Pokeball")
            lines.append("What are you doing?")
            buttons = [(pokemon, "Try to catch it(again)"), ("F", "Flee")]
        elif next_step < 8:
            pokemon = "..."
            lines.append("Pokemon escaped from Pokeball")
            lines.append(f"It disappeared into the {where}")
            lines.append("Which way now?")
            buttons = [("L", "Left"), ("S", "Straight ahead"), ("R", "Right")]
        else:
            pokemon_pic_src = 'https://static.wikia.nocookie.net/pokemon-fano/images/6/6f/Poke_Ball.png/revision/latest?cb=20140520015336'
            pokemon_level = random.randint(3, 10)
            lines.append("Success!")
            lines.append(f"You caught: {pokemon} ({pokemon_level})")
            lines.append("Which way now?")
            buttons = [("L", "Left"), ("S", "Straight ahead"), ("R", "Right")]
            p = PokemonMonster(species=PokemonSpecies.objects.get(name=pokemon),
                               level=random.randint(3, 10),
                               owner=request.user,
                               gender=random.choice(("Male", "Female")))
            if p.species.if_genderless:
                p.gender = "Unknown"
            p.save()

    else:
        lines = [random.randint(0, 30) for i in range(random.randint(3, 7))]
        lines = ["." * (5 + i) + ("swim" if where == "sea" else "walk") + "." * (40 - i) for i in lines]
        if next_step < 8:
            lines.append("Which way now?")
            buttons = [("L", "Left"), ("S", "Straight ahead"), ("R", "Right")]
        else:
            lines.append("Wild pokemon appeared!")
            pokemon = random_pokemon_name(where,legendary=False)
            lines.append("It's " + pokemon)
            lines.append("What are you doing?")
            buttons = [(pokemon, "Try to catch it"), ("F", "Flee")]
            pokemon_pic_src = PokemonSpecies.objects.get(name=pokemon).picture_source
    if len(lines) >4:
        lines = lines[-4:]
    context = {'where': where,
               'where_pic': where_pic,
               'pokemon': pokemon,
               'pokemon_pic_src': pokemon_pic_src,
               'lines': lines,
               'buttons': buttons, }
    return render(request, 'pokemon/explore.html', context)




@login_required(login_url='login')
def pokedex(request):
    if request.method=="POST" and PokemonSpecies.objects.filter(name=request.POST['choice']).count()>0:
        return render(request, 'pokemon/pokedex_page.html',
                      {'pokemon':PokemonSpecies.objects.get(name=request.POST['choice'])})

    pokemon_list = PokemonSpecies.objects.all().order_by('national_pokedex_number')
    pokemon_list = [(x.is_caught(request),x) for x in pokemon_list]
    return render(request, 'pokemon/pokedex.html', {"pokemon_list": pokemon_list})

@login_required(login_url='login')
def who_that_pokemon(request, pokemon_id):
    if PokemonMonster.objects.get(id=pokemon_id).owner != request.user:
        return redirect('home')
    pokemon = random_pokemon_name(legendary=True)
    pokemon_img = PokemonSpecies.objects.get(name=pokemon).picture_source
    pokemon_names = {pokemon}
    while len(pokemon_names)<4:
        pokemon_names.add(random_pokemon_name())
    pokemon_names = list(pokemon_names)
    random.shuffle(pokemon_names)
    trained_pokemon = PokemonMonster.objects.get(id=pokemon_id)
    if request.method=="POST" and request.POST['choice'] == "True":
        trained_pokemon.add_exp(20)
        trained_pokemon.save()
    if trained_pokemon.name is None:
        name = trained_pokemon.species.name
    else:
        name = trained_pokemon.name
    exp_now = trained_pokemon.get_exp() - trained_pokemon.level ** 3
    exp_next_level = (trained_pokemon.level + 1) ** 3 - trained_pokemon.level ** 3
    level = trained_pokemon.level

    context={
        'pokemon': pokemon,
        'pokemon_names': pokemon_names,
        'pokemon_image': pokemon_img,
        'name': name,
        'level': level,
        'exp_now': exp_now,
        'exp_next_level': exp_next_level
    }
    time.sleep(0.5)
    return render(request, "pokemon/who_that_pokemon.html",context)