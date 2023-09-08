from pokemon.models import PokemonSpecies
def gen():
    text = """
    0081	Magnemite	Magnemite
    Electric	Steel	Mineral
    0082	Magneton	Magneton
    Electric	Steel	Mineral
    0100	Voltorb	Voltorb
    Electric	Mineral
    0101	Electrode	Electrode
    Electric	Mineral
    0120	Staryu	Staryu
    Water	Water 3
    0121	Starmie	Starmie
    Water	Psychic	Water 3
    0137	Porygon	Porygon
    Normal	Mineral
    0233	Porygon2	Porygon2
    Normal	Mineral
    0292	Shedinja	Shedinja
    Bug	Ghost	Mineral
    0337	Lunatone	Lunatone
    Rock	Psychic	Mineral
    0338	Solrock	Solrock
    Rock	Psychic	Mineral
    0343	Baltoy	Baltoy
    Ground	Psychic	Mineral
    0344	Claydol	Claydol
    Ground	Psychic	Mineral
    0374	Beldum	Beldum
    Steel	Psychic	Mineral
    0375	Metang	Metang
    Steel	Psychic	Mineral
    0376	Metagross	Metagross
    Steel	Psychic	Mineral
    0436	Bronzor	Bronzor
    Steel	Psychic	Mineral
    0437	Bronzong	Bronzong
    Steel	Psychic	Mineral
    0462	Magnezone	Magnezone
    Electric	Steel	Mineral
    0474	Porygon-Z	Porygon-Z
    Normal	Mineral
    0479	Rotom	Rotom
    Electric	Ghost	Amorphous
    0479	Rotom	Rotom
    Heat Rotom	Electric	Fire	Amorphous
    0479	Rotom	Rotom
    Wash Rotom	Electric	Water	Amorphous
    0479	Rotom	Rotom
    Frost Rotom	Electric	Ice	Amorphous
    0479	Rotom	Rotom
    Fan Rotom	Electric	Flying	Amorphous
    0479	Rotom	Rotom
    Mow Rotom	Electric	Grass	Amorphous
    0489	Phione	Phione
    Water	Water 1/Fairy
    0490	Manaphy	Manaphy
    Water	Water 1/Fairy
    0599	Klink	Klink
    Steel	Mineral
    0600	Klang	Klang
    Steel	Mineral
    0601	Klinklang	Klinklang
    Steel	Mineral
    0615	Cryogonal	Cryogonal
    Ice	Mineral
    0622	Golett	Golett
    Ground	Ghost	Mineral
    0623	Golurk	Golurk
    Ground	Ghost	Mineral
    0703	Carbink	Carbink
    Rock	Fairy	Fairy/Mineral
    0774	Minior	Minior
    Rock	Flying	Mineral
    0781	Dhelmise	Dhelmise
    Ghost	Grass	Mineral
    0854	Sinistea	Sinistea
    Ghost	Mineral/Amorphous
    0855	Polteageist	Polteageist
    Ghost	Mineral/Amorphous
    0870	Falinks	Falinks
    Fighting	Fairy/Mineral
    0924	Tandemaus	Tandemaus
    Normal	Field/Fairy
    0925	Maushold	Maushold
    Normal	Field/Fairy
    
    Unbreedable
    #	 	Pokémon	Type	Egg Groups
    0132	Ditto	Ditto
    Normal	Ditto
    0144	Articuno	Articuno
    Ice	Flying	No Eggs Discovered
    0144	Articuno	Articuno
    Galarian Form	Psychic	Flying	No Eggs Discovered
    0145	Zapdos	Zapdos
    Electric	Flying	No Eggs Discovered
    0145	Zapdos	Zapdos
    Galarian Form	Fighting	Flying	No Eggs Discovered
    0146	Moltres	Moltres
    Fire	Flying	No Eggs Discovered
    0146	Moltres	Moltres
    Galarian Form	Dark	Flying	No Eggs Discovered
    0150	Mewtwo	Mewtwo
    Psychic	No Eggs Discovered
    0151	Mew	Mew
    Psychic	No Eggs Discovered
    0201	Unown	Unown
    Psychic	No Eggs Discovered
    0243	Raikou	Raikou
    Electric	No Eggs Discovered
    0244	Entei	Entei
    Fire	No Eggs Discovered
    0245	Suicune	Suicune
    Water	No Eggs Discovered
    0249	Lugia	Lugia
    Psychic	Flying	No Eggs Discovered
    0250	Ho-Oh	Ho-Oh
    Fire	Flying	No Eggs Discovered
    0251	Celebi	Celebi
    Psychic	Grass	No Eggs Discovered
    0377	Regirock	Regirock
    Rock	No Eggs Discovered
    0378	Regice	Regice
    Ice	No Eggs Discovered
    0379	Registeel	Registeel
    Steel	No Eggs Discovered
    0382	Kyogre	Kyogre
    Water	No Eggs Discovered
    0383	Groudon	Groudon
    Ground	No Eggs Discovered
    0384	Rayquaza	Rayquaza
    Dragon	Flying	No Eggs Discovered
    0385	Jirachi	Jirachi
    Steel	Psychic	No Eggs Discovered
    0386	Deoxys	Deoxys
    Normal Forme	Psychic	No Eggs Discovered
    0386	Deoxys	Deoxys
    Attack Forme	Psychic	No Eggs Discovered
    0386	Deoxys	Deoxys
    Defense Forme	Psychic	No Eggs Discovered
    0386	Deoxys	Deoxys
    Speed Forme	Psychic	No Eggs Discovered
    0480	Uxie	Uxie
    Psychic	No Eggs Discovered
    0481	Mesprit	Mesprit
    Psychic	No Eggs Discovered
    0482	Azelf	Azelf
    Psychic	No Eggs Discovered
    0483	Dialga	Dialga
    Steel	Dragon	No Eggs Discovered
    0484	Palkia	Palkia
    Water	Dragon	No Eggs Discovered
    0486	Regigigas	Regigigas
    Normal	No Eggs Discovered
    0487	Giratina	Giratina
    Altered Forme	Ghost	Dragon	No Eggs Discovered
    0487	Giratina	Giratina
    Origin Forme	Ghost	Dragon	No Eggs Discovered
    0491	Darkrai	Darkrai
    Dark	No Eggs Discovered
    0492	Shaymin	Shaymin
    Land Forme	Grass	No Eggs Discovered
    0492	Shaymin	Shaymin
    Sky Forme	Grass	Flying	No Eggs Discovered
    0493	Arceus	Arceus
    Normal	No Eggs Discovered
    0494	Victini	Victini
    Psychic	Fire	No Eggs Discovered
    0638	Cobalion	Cobalion
    Steel	Fighting	No Eggs Discovered
    0639	Terrakion	Terrakion
    Rock	Fighting	No Eggs Discovered
    0640	Virizion	Virizion
    Grass	Fighting	No Eggs Discovered
    0643	Reshiram	Reshiram
    Dragon	Fire	No Eggs Discovered
    0644	Zekrom	Zekrom
    Dragon	Electric	No Eggs Discovered
    0646	Kyurem	Kyurem
    Dragon	Ice	No Eggs Discovered
    0646	Kyurem	Kyurem
    Black Kyurem	Dragon	Ice	No Eggs Discovered
    0646	Kyurem	Kyurem
    White Kyurem	Dragon	Ice	No Eggs Discovered
    0647	Keldeo	Keldeo
    Ordinary Form	Water	Fighting	No Eggs Discovered
    0647	Keldeo	Keldeo
    Resolute Form	Water	Fighting	No Eggs Discovered
    0648	Meloetta	Meloetta
    Normal	Psychic	No Eggs Discovered
    0649	Genesect	Genesect
    Bug	Steel	No Eggs Discovered
    0716	Xerneas	Xerneas
    Fairy	No Eggs Discovered
    0717	Yveltal	Yveltal
    Dark	Flying	No Eggs Discovered
    0718	Zygarde	Zygarde
    Dragon	Ground	No Eggs Discovered
    0719	Diancie	Diancie
    Rock	Fairy	No Eggs Discovered
    0720	Hoopa	Hoopa
    Hoopa Confined	Psychic	Ghost	No Eggs Discovered
    0720	Hoopa	Hoopa
    Hoopa Unbound	Psychic	Dark	No Eggs Discovered
    0721	Volcanion	Volcanion
    Fire	Water	No Eggs Discovered
    0772	Type: Null	Type: Null
    Normal	No Eggs Discovered
    0773	Silvally	Silvally
    Normal	No Eggs Discovered
    0785	Tapu Koko	Tapu Koko
    Electric	Fairy	No Eggs Discovered
    0786	Tapu Lele	Tapu Lele
    Psychic	Fairy	No Eggs Discovered
    0787	Tapu Bulu	Tapu Bulu
    Grass	Fairy	No Eggs Discovered
    0788	Tapu Fini	Tapu Fini
    Water	Fairy	No Eggs Discovered
    0789	Cosmog	Cosmog
    Psychic	No Eggs Discovered
    0790	Cosmoem	Cosmoem
    Psychic	No Eggs Discovered
    0791	Solgaleo	Solgaleo
    Psychic	Steel	No Eggs Discovered
    0792	Lunala	Lunala
    Psychic	Ghost	No Eggs Discovered
    0793	Nihilego	Nihilego
    Rock	Poison	No Eggs Discovered
    0794	Buzzwole	Buzzwole
    Bug	Fighting	No Eggs Discovered
    0795	Pheromosa	Pheromosa
    Bug	Fighting	No Eggs Discovered
    0796	Xurkitree	Xurkitree
    Electric	No Eggs Discovered
    0797	Celesteela	Celesteela
    Steel	Flying	No Eggs Discovered
    0798	Kartana	Kartana
    Grass	Steel	No Eggs Discovered
    0799	Guzzlord	Guzzlord
    Dark	Dragon	No Eggs Discovered
    0800	Necrozma	Necrozma
    Psychic	No Eggs Discovered
    0800	Necrozma	Necrozma
    Dusk Mane	Psychic	Steel	No Eggs Discovered
    0800	Necrozma	Necrozma
    Dawn Wings	Psychic	Ghost	No Eggs Discovered
    0801	Magearna	Magearna
    Steel	Fairy	No Eggs Discovered
    0802	Marshadow	Marshadow
    Fighting	Ghost	No Eggs Discovered
    0803	Poipole	Poipole
    Poison	No Eggs Discovered
    0804	Naganadel	Naganadel
    Poison	Dragon	No Eggs Discovered
    0805	Stakataka	Stakataka
    Rock	Steel	No Eggs Discovered
    0806	Blacephalon	Blacephalon
    Fire	Ghost	No Eggs Discovered
    0807	Zeraora	Zeraora
    Electric	No Eggs Discovered
    0808	Meltan	Meltan
    Steel	No Eggs Discovered
    0809	Melmetal	Melmetal
    Steel	No Eggs Discovered
    0880	Dracozolt	Dracozolt
    Electric	Dragon	No Eggs Discovered
    0881	Arctozolt	Arctozolt
    Electric	Ice	No Eggs Discovered
    0882	Dracovish	Dracovish
    Water	Dragon	No Eggs Discovered
    0883	Arctovish	Arctovish
    Water	Ice	No Eggs Discovered
    0888	Zacian	Zacian
    Fairy	No Eggs Discovered
    0889	Zamazenta	Zamazenta
    Fighting	No Eggs Discovered
    0890	Eternatus	Eternatus
    Poison	Dragon	No Eggs Discovered
    0893	Zarude	Zarude
    Dark	Grass	No Eggs Discovered
    0894	Regieleki	Regieleki
    Electric	No Eggs Discovered
    0895	Regidrago	Regidrago
    Dragon	No Eggs Discovered
    0896	Glastrier	Glastrier
    Ice	No Eggs Discovered
    0897	Spectrier	Spectrier
    Ghost	No Eggs Discovered
    0898	Calyrex	Calyrex
    Psychic	Grass	No Eggs Discovered
    0898	Calyrex	Calyrex
    Ice Rider	Psychic	Ice	No Eggs Discovered
    0898	Calyrex	Calyrex
    Shadow Rider	Psychic	Ghost	No Eggs Discovered
    0984	Great Tusk	Great Tusk
    Ground	Fighting	No Eggs Discovered
    0985	Scream Tail	Scream Tail
    Fairy	Psychic	No Eggs Discovered
    0986	Brute Bonnet	Brute Bonnet
    Grass	Dark	No Eggs Discovered
    0987	Flutter Mane	Flutter Mane
    Ghost	Fairy	No Eggs Discovered
    0988	Slither Wing	Slither Wing
    Bug	Fighting	No Eggs Discovered
    0989	Sandy Shocks	Sandy Shocks
    Electric	Ground	No Eggs Discovered
    0990	Iron Treads	Iron Treads
    Ground	Steel	No Eggs Discovered
    0991	Iron Bundle	Iron Bundle
    Ice	Water	No Eggs Discovered
    0992	Iron Hands	Iron Hands
    Fighting	Electric	No Eggs Discovered
    0993	Iron Jugulis	Iron Jugulis
    Dark	Flying	No Eggs Discovered
    0994	Iron Moth	Iron Moth
    Fire	Poison	No Eggs Discovered
    0995	Iron Thorns	Iron Thorns
    Rock	Electric	No Eggs Discovered
    0999	Gimmighoul	Gimmighoul
    Chest Form	Ghost	No Eggs Discovered
    0999	Gimmighoul	Gimmighoul
    Roaming Form	Ghost	No Eggs Discovered
    1000	Gholdengo	Gholdengo
    Steel	Ghost	No Eggs Discovered
    1001	Wo-Chien	Wo-Chien
    Dark	Grass	No Eggs Discovered
    1002	Chien-Pao	Chien-Pao
    Dark	Ice	No Eggs Discovered
    1003	Ting-Lu	Ting-Lu
    Dark	Ground	No Eggs Discovered
    1004	Chi-Yu	Chi-Yu
    Dark	Fire	No Eggs Discovered
    1005	Roaring Moon	Roaring Moon
    Dragon	Dark	No Eggs Discovered
    1006	Iron Valiant	Iron Valiant
    Fairy	Fighting	No Eggs Discovered
    1007	Koraidon	Koraidon
    Fighting	Dragon	No Eggs Discovered
    1008	Miraidon	Miraidon
    Electric	Dragon	No Eggs Discovered
    """ #list copied from Bulbapedia

    pokemon_list = text.split()
    counter = 0
    for pokemon in pokemon_list:
        if len(PokemonSpecies.objects.filter(name=pokemon)) != 0:
            pok = PokemonSpecies.objects.get(name=pokemon)
            pok.if_genderless = True
            pok.save()
            counter += 1
    print(counter)