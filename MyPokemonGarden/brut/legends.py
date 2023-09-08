from pokemon.models import PokemonSpecies

def gen():
    text="""
    
    Sub-Legendary Pokémon
    
    Articuno
     
    Pressure
    Snow Cloak
    
    Zapdos
     
    Pressure
    Static
    
    Moltres
     
    Pressure
    Flame Body
    
    Raikou
    
    Pressure
    Inner Focus
    
    Entei
    
    Pressure
    Inner Focus
    
    Suicune
    
    Pressure
    Inner Focus
    
    Regirock
    
    Clear Body
    Sturdy
    
    Regice
    
    Clear Body
    Ice Body
    
    Registeel
    
    Clear Body
    Light Metal
    
    Latias
     
    Levitate
    
    Latios
     
    Levitate
    
    Uxie
    
    Levitate
    
    Mesprit
    
    Levitate
    
    Azelf
    
    Levitate
    
    Heatran
     
    Flash Fire
    Flame Body
    
    Regigigas
    
    Slow Start
    
    Cresselia
    
    Levitate
    
    Cobalion
     
    Justified
    
    Terrakion
     
    Justified
    
    Virizion
     
    Justified
    
    Tornadus
    
    Prankster
    Defiant
    
    Thundurus
     
    Prankster
    Defiant
    
    Landorus
     
    Sand Force
    Sheer Force
    
    Type: Null
    
    Battle Armor
    
    Silvally
    
    RKS System
    
    Tapu Koko
     
    Electric Surge
    Telepathy
    
    Tapu Lele
     
    Psychic Surge
    Telepathy
    
    Tapu Bulu
     
    Grassy Surge
    Telepathy
    
    Tapu Fini
     
    Misty Surge
    Telepathy
    
    Nihilego
     
    Beast Boost
    
    Buzzwole
     
    Beast Boost
    
    Pheromosa
     
    Beast Boost
    
    Xurkitree
    
    Beast Boost
    
    Celesteela
     
    Beast Boost
    
    Kartana
     
    Beast Boost
    
    Guzzlord
     
    Beast Boost
    
    Poipole
    
    Beast Boost
    
    Naganadel
     
    Beast Boost
    
    Stakataka
     
    Beast Boost
    
    Blacephalon
     
    Beast Boost
    
    Kubfu
    
    Inner Focus
    
    Urshifu
     
    Unseen Fist
    
    Regieleki
    
    Transistor
    
    Regidrago
    
    Dragon's Maw
    
    Glastrier
    
    Chilling Neigh
    
    Spectrier
    
    Grim Neigh
    
    Enamorus
     
    Healer
    Contrary
    
    Wo-Chien
     
    
    Chien-Pao
     
    
    Ting-Lu
     
    
    Chi-Yu
     
     
    Legendary Pokémon
    
    Mewtwo
    
    Pressure
    Unnerve
    
    Lugia
     
    Pressure
    Multiscale
    
    Ho-Oh
     
    Pressure
    Regenerator
    
    Kyogre
    
    Drizzle
    
    Groudon
    
    Drought
    
    Rayquaza
     
    Air Lock
    
    Dialga
     
    Pressure
    Telepathy
    
    Palkia
     
    Pressure
    Telepathy
    
    Giratina
     
    Pressure
    Telepathy
    
    Reshiram
     
    Turboblaze
    
    Zekrom
     
    Teravolt
    
    Kyurem
     
    Pressure
    
    Xerneas
    
    Fairy Aura
    
    Yveltal
     
    Dark Aura
    
    Zygarde
     
    Aura Break
    
    Cosmog
    
    Unaware
    
    Cosmoem
    
    Sturdy
    
    Solgaleo
     
    Full Metal Body
    
    Lunala
     
    Shadow Shield
    
    Necrozma
    
    Prism Armor
    
    Zacian
     
    Intrepid Sword
    
    Zamazenta
     
    Dauntless Shield
    
    Eternatus
     
    Pressure
    
    Calyrex
     
    Unnerve
    
    Koraidon
     
    
    Miraidon
     
    
    Mew
    
    Synchronize
    
    Celebi
     
    Natural Cure
    
    Jirachi
     
    Serene Grace
    
    Deoxys
    
    Pressure
    
    Phione
    
    Hydration
    
    Manaphy
    
    Hydration
    
    Darkrai
    
    Bad Dreams
    
    Shaymin
    
    Natural Cure
    
    Arceus
    
    Multitype
    
    Victini
     
    Victory Star
    
    Keldeo
     
    Justified
    
    Meloetta
     
    Serene Grace
    
    Genesect
     
    Download
    
    Diancie
     
    Clear Body
    
    Hoopa
     
    Magician
    
    Volcanion
     
    Water Absorb
    
    Magearna
     
    Soul-Heart
    
    Marshadow
     
    Technician
    
    Zeraora
    
    Volt Absorb
    
    Meltan
    
    Magnet Pull
    
    Melmetal
    
    Iron Fist
    
    Zarude
     
    Leaf Guard
    
    
    """

    lista = text.split()

    counter = 0
    for x in lista:
        if len(PokemonSpecies.objects.filter(name=x))!=0:

            pok = PokemonSpecies.objects.get(name=x)
            if not pok.if_legendary:
                counter +=1
            pok.if_legendary = True
            pok.save()

    print(counter)