import re
from pokemon.models import PokemonSpecies, PokemonType, PokemonGeneration
def pokemon_names(liczba):
    text ="""
Meowscarada0908	Meowscarada	GRASS
DARK	530	76	110	70	81	70	123
Fuecoco0909	Fuecoco	FIRE
310	67	45	59	63	40	36
Crocalor0910	Crocalor	FIRE
411	81	55	78	90	58	49
Skeledirge0911	Skeledirge	FIRE
GHOST	530	104	75	100	110	75	66
Quaxly0912	Quaxly	WATER
310	55	65	45	50	45	50
Quaxwell0913	Quaxwell	WATER
410	70	85	65	65	60	65
Quaquaval0914	Quaquaval	WATER
FIGHTING	530	85	120	80	85	75	85
Lechonk0915	Lechonk	NORMAL
254	54	45	40	35	45	35
Tarountula0917	Tarountula	BUG
210	35	41	45	29	40	20
Spidops0918	Spidops	BUG
404	60	79	92	52	86	35
Nymble0919	Nymble	BUG
210	33	46	40	21	25	45
Lokix0920	Lokix	BUG
DARK	450	71	102	78	52	55	92
Pawmi0921	Pawmi	ELECTRIC
240	45	50	20	40	25	60
Pawmo0922	Pawmo	ELECTRIC
FIGHTING	350	60	75	40	50	40	85
Pawmot0923	Pawmot	ELECTRIC
FIGHTING	490	70	115	70	70	60	105
Tandemaus0924	Tandemaus	NORMAL
305	50	50	45	40	4evolutions
"""

    text = re.sub("\t[0-9].*"," ",text)
    text = re.sub("Mega .*\n", " ", text)
    text = re.sub("\n[0-9][0-9][0-9]\n", "\n", text)
    text = re.sub("\n[0-9][0-9][0-9] \n", "\n", text)
    text = re.sub("Alolan.*\n", "", text)
    text = re.sub("Galarian.*\n", "", text)
    text = re.sub("Hisuian.*\n", "", text)
    text = re.sub("\n\t[A-Z][A-Z].*", "", text)
    text = re.sub("\n  [A-Z][A-Z].*", "", text)
    text = re.sub("\n  [0-9].*", "", text)
    text = re.sub("[A-Z][a-z]*0","0",text)
    text = re.sub("[A-Z][a-z]*1", "1", text)

    lista = text.split("\n")
    for i in range(len(lista)):
        if i>=1 and len(lista[i]) and len(lista[i-1]):
            if lista[i][0].isupper() and lista[i-1][-1].isupper():
                lista[i-1] = lista [i-1] + "\t" + lista[i]
                lista[i] = ""
    lista = [line for line in lista if line != ""]
    text = "\n".join(lista)

    text = re.sub("\n[A-Z]* *\n","\n",text)

    lista = text.split("\n")[liczba:]
    lista = [x.split('\t') for x in lista]
    lista = [x for x in lista if len(x) == 3 or len(x) == 4]
    counter =0


    for pok in lista:
        if PokemonSpecies.objects.filter(name=pok[1].capitalize().strip()).count() == 0:
            counter += 1
            gen = 0
            num = int(pok[0])
            if num >151 and num<252:
                gen = 1
            if num >251 and num <= 386:
                gen = 2
            if num > 386 and num <= 494:
                gen = 3
            if num > 494:
                gen = 4
            gen = PokemonGeneration.objects.all()[gen]
            pokemon = PokemonSpecies(name=pok[1], national_pokedex_number=int(pok[0]), description="None",
                           short_description="Pokemon", generation=gen)
            pokemon.save()
            type_name = pok[2].capitalize().strip()
            if type_name == "Flying":
                type_name = "Fly"
            if type_name == "Fighting":
                type_name = "Fight"
            t = PokemonType.objects.get(name=type_name)
            pokemon.type.add(t)
            if len(pok)>3:
                type_name = pok[3].capitalize().strip()
                if type_name == "Flying":
                    type_name = "Fly"
                if type_name == "Fighting":
                    type_name = "Fight"
                t = PokemonType.objects.get(name=type_name)
                pokemon.type.add(t)
            pokemon.picture_source=f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{str(int(pok[0])):0>3}.png"
            pokemon.save()

    print(counter)


