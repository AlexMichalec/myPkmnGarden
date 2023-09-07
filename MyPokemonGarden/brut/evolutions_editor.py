import re
from pokemon.models import PokemonSpecies

def evo():
    text = """

Generation 1
Bulbasaur
#0001
Bulbasaur
Grass · Poison
(Level 16)
Ivysaur
#0002
Ivysaur
Grass · Poison
(Level 32)
Venusaur
#0003
Venusaur
Grass · Poison
Charmander
#0004
Charmander
Fire
(Level 16)
Charmeleon
#0005
Charmeleon
Fire
(Level 36)
Charizard
#0006
Charizard
Fire · Flying
Squirtle
#0007
Squirtle
Water
(Level 16)
Wartortle
#0008
Wartortle
Water
(Level 36)
Blastoise
#0009
Blastoise
Water
Caterpie
#0010
Caterpie
Bug
(Level 7)
Metapod
#0011
Metapod
Bug
(Level 10)
Butterfree
#0012
Butterfree
Bug · Flying
Weedle
#0013
Weedle
Bug · Poison
(Level 7)
Kakuna
#0014
Kakuna
Bug · Poison
(Level 10)
Beedrill
#0015
Beedrill
Bug · Poison
Pidgey
#0016
Pidgey
Normal · Flying
(Level 18)
Pidgeotto
#0017
Pidgeotto
Normal · Flying
(Level 36)
Pidgeot
#0018
Pidgeot
Normal · Flying
Rattata
#0019
Rattata
Normal
(Level 20)
Raticate
#0020
Raticate
Normal
Alolan Rattata
#0019
Rattata
Alolan Rattata
Dark · Normal
(Level 20, Nighttime)
Alolan Raticate
#0020
Raticate
Alolan Raticate
Dark · Normal
Spearow
#0021
Spearow
Normal · Flying
(Level 20)
Fearow
#0022
Fearow
Normal · Flying
Ekans
#0023
Ekans
Poison
(Level 22)
Arbok
#0024
Arbok
Poison
Pichu
#0172
Pichu
Electric
(high Friendship)
Pikachu
#0025
Pikachu
Electric
(use Thunder Stone, outside Alola)
Raichu
#0026
Raichu
Electric
(use Thunder Stone, in Alola)
Alolan Raichu
#0026
Raichu
Alolan Raichu
Electric · Psychic
Sandshrew
#0027
Sandshrew
Ground
(Level 22)
Sandslash
#0028
Sandslash
Ground
Alolan Sandshrew
#0027
Sandshrew
Alolan Sandshrew
Ice · Steel
(use Ice Stone)
Alolan Sandslash
#0028
Sandslash
Alolan Sandslash
Ice · Steel
Nidoran♀
#0029
Nidoran♀
Poison
(Level 16)
Nidorina
#0030
Nidorina
Poison
(use Moon Stone)
Nidoqueen
#0031
Nidoqueen
Poison · Ground
Nidoran♂
#0032
Nidoran♂
Poison
(Level 16)
Nidorino
#0033
Nidorino
Poison
(use Moon Stone)
Nidoking
#0034
Nidoking
Poison · Ground
Cleffa
#0173
Cleffa
Fairy
(high Friendship)
Clefairy
#0035
Clefairy
Fairy
(use Moon Stone)
Clefable
#0036
Clefable
Fairy
Vulpix
#0037
Vulpix
Fire
(use Fire Stone)
Ninetales
#0038
Ninetales
Fire
Alolan Vulpix
#0037
Vulpix
Alolan Vulpix
Ice
(use Ice Stone)
Alolan Ninetales
#0038
Ninetales
Alolan Ninetales
Ice · Fairy
Igglybuff
#0174
Igglybuff
Normal · Fairy
(high Friendship)
Jigglypuff
#0039
Jigglypuff
Normal · Fairy
(use Moon Stone)
Wigglytuff
#0040
Wigglytuff
Normal · Fairy
Zubat
#0041
Zubat
Poison · Flying
(Level 22)
Golbat
#0042
Golbat
Poison · Flying
(high Friendship)
Crobat
#0169
Crobat
Poison · Flying
Oddish
#0043
Oddish
Grass · Poison
(Level 21)
Gloom
#0044
Gloom
Grass · Poison
(use Leaf Stone)
Vileplume
#0045
Vileplume
Grass · Poison
(use Sun Stone)
Bellossom
#0182
Bellossom
Grass
Paras
#0046
Paras
Bug · Grass
(Level 24)
Parasect
#0047
Parasect
Bug · Grass
Venonat
#0048
Venonat
Bug · Poison
(Level 31)
Venomoth
#0049
Venomoth
Bug · Poison
Diglett
#0050
Diglett
Ground
(Level 26)
Dugtrio
#0051
Dugtrio
Ground
Alolan Diglett
#0050
Diglett
Alolan Diglett
Ground · Steel
(Level 26)
Alolan Dugtrio
#0051
Dugtrio
Alolan Dugtrio
Ground · Steel
Meowth
#0052
Meowth
Normal
(Level 28)
Persian
#0053
Persian
Normal
Alolan Meowth
#0052
Meowth
Alolan Meowth
Dark
(high Friendship)
Alolan Persian
#0053
Persian
Alolan Persian
Dark
Galarian Meowth
#0052
Meowth
Galarian Meowth
Steel
(Level 28)
Perrserker
#0863
Perrserker
Steel
Psyduck
#0054
Psyduck
Water
(Level 33)
Golduck
#0055
Golduck
Water
Mankey
#0056
Mankey
Fighting
(Level 28)
Primeape
#0057
Primeape
Fighting
(Use Rage Fist 20 times)
Annihilape
#0979
Annihilape
Fighting · Ghost
Growlithe
#0058
Growlithe
Fire
(use Fire Stone)
Arcanine
#0059
Arcanine
Fire
Growlithe (Hisuian Growlithe)
#0058
Growlithe
Hisuian Growlithe
Fire · Rock
(use Fire Stone)
Arcanine (Hisuian Arcanine)
#0059
Arcanine
Hisuian Arcanine
Fire · Rock
Poliwag
#0060
Poliwag
Water
(Level 25)
Poliwhirl
#0061
Poliwhirl
Water
(use Water Stone)
Poliwrath
#0062
Poliwrath
Water · Fighting
(trade holding Kings Rock)
Politoed
#0186
Politoed
Water
Abra
#0063
Abra
Psychic
(Level 16)
Kadabra
#0064
Kadabra
Psychic
(Trade)
Alakazam
#0065
Alakazam
Psychic
Machop
#0066
Machop
Fighting
(Level 28)
Machoke
#0067
Machoke
Fighting
(Trade)
Machamp
#0068
Machamp
Fighting
Bellsprout
#0069
Bellsprout
Grass · Poison
(Level 21)
Weepinbell
#0070
Weepinbell
Grass · Poison
(use Leaf Stone)
Victreebel
#0071
Victreebel
Grass · Poison
Tentacool
#0072
Tentacool
Water · Poison
(Level 30)
Tentacruel
#0073
Tentacruel
Water · Poison
Geodude
#0074
Geodude
Rock · Ground
(Level 25)
Graveler
#0075
Graveler
Rock · Ground
(Trade)
Golem
#0076
Golem
Rock · Ground
Alolan Geodude
#0074
Geodude
Alolan Geodude
Rock · Electric
(Level 25)
Alolan Graveler
#0075
Graveler
Alolan Graveler
Rock · Electric
(Trade)
Alolan Golem
#0076
Golem
Alolan Golem
Rock · Electric
Ponyta
#0077
Ponyta
Fire
(Level 40)
Rapidash
#0078
Rapidash
Fire
Galarian Ponyta
#0077
Ponyta
Galarian Ponyta
Psychic
(Level 40)
Galarian Rapidash
#0078
Rapidash
Galarian Rapidash
Psychic · Fairy
Slowpoke
#0079
Slowpoke
Water · Psychic
(Level 37)
Slowbro
#0080
Slowbro
Water · Psychic
(trade holding Kings Rock)
Slowking
#0199
Slowking
Water · Psychic
Galarian Slowpoke
#0079
Slowpoke
Galarian Slowpoke
Psychic
(use Galarica Cuff)
Galarian Slowbro
#0080
Slowbro
Galarian Slowbro
Poison · Psychic
(use Galarica Wreath)
Galarian Slowking
#0199
Slowking
Galarian Slowking
Poison · Psychic
Magnemite
#0081
Magnemite
Electric · Steel
(Level 30)
Magneton
#0082
Magneton
Electric · Steel
(use Thunder Stone, in Gen 8+, or level up in a Magnetic Field area)
Magnezone
#0462
Magnezone
Electric · Steel
Doduo
#0084
Doduo
Normal · Flying
(Level 31)
Dodrio
#0085
Dodrio
Normal · Flying
Seel
#0086
Seel
Water
(Level 34)
Dewgong
#0087
Dewgong
Water · Ice
Grimer
#0088
Grimer
Poison
(Level 38)
Muk
#0089
Muk
Poison
Alolan Grimer
#0088
Grimer
Alolan Grimer
Poison · Dark
(Level 38)
Alolan Muk
#0089
Muk
Alolan Muk
Poison · Dark
Shellder
#0090
Shellder
Water
(use Water Stone)
Cloyster
#0091
Cloyster
Water · Ice
Gastly
#0092
Gastly
Ghost · Poison
(Level 25)
Haunter
#0093
Haunter
Ghost · Poison
(Trade)
Gengar
#0094
Gengar
Ghost · Poison
Onix
#0095
Onix
Rock · Ground
(trade holding Metal Coat)
Steelix
#0208
Steelix
Steel · Ground
Drowzee
#0096
Drowzee
Psychic
(Level 26)
Hypno
#0097
Hypno
Psychic
Krabby
#0098
Krabby
Water
(Level 28)
Kingler
#0099
Kingler
Water
Voltorb
#0100
Voltorb
Electric
(Level 30)
Electrode
#0101
Electrode
Electric
Voltorb (Hisuian Voltorb)
#0100
Voltorb
Hisuian Voltorb
Electric · Grass
(use Leaf Stone)
Electrode (Hisuian Electrode)
#0101
Electrode
Hisuian Electrode
Electric · Grass
Exeggcute
#0102
Exeggcute
Grass · Psychic
(use Leaf Stone, outside Alola)
Exeggutor
#0103
Exeggutor
Grass · Psychic
(use Leaf Stone, in Alola)
Alolan Exeggutor
#0103
Exeggutor
Alolan Exeggutor
Grass · Dragon
Cubone
#0104
Cubone
Ground
(Level 28, outside Alola)
Marowak
#0105
Marowak
Ground
(Level 28, Nighttime, in Alola)
Alolan Marowak
#0105
Marowak
Alolan Marowak
Fire · Ghost
Tyrogue
#0236
Tyrogue
Fighting
(Level 20, Attack > Defense)
Hitmonlee
#0106
Hitmonlee
Fighting
(Level 20, Attack < Defense)
Hitmonchan
#0107
Hitmonchan
Fighting
(Level 20, Attack = Defense)
Hitmontop
#0237
Hitmontop
Fighting
Lickitung
#0108
Lickitung
Normal
(after Rollout learned)
Lickilicky
#0463
Lickilicky
Normal
Koffing
#0109
Koffing
Poison
(Level 35, outside Galar)
Weezing
#0110
Weezing
Poison
(Level 35, in Galar)
Galarian Weezing
#0110
Weezing
Galarian Weezing
Poison · Fairy
Rhyhorn
#0111
Rhyhorn
Ground · Rock
(Level 42)
Rhydon
#0112
Rhydon
Ground · Rock
(trade holding Protector)
Rhyperior
#0464
Rhyperior
Ground · Rock
Happiny
#0440
Happiny
Normal
(hold Oval Stone, Daytime)
Chansey
#0113
Chansey
Normal
(high Friendship)
Blissey
#0242
Blissey
Normal
Tangela
#0114
Tangela
Grass
(after Ancient Power learned)
Tangrowth
#0465
Tangrowth
Grass
Horsea
#0116
Horsea
Water
(Level 32)
Seadra
#0117
Seadra
Water
(trade holding Dragon Scale)
Kingdra
#0230
Kingdra
Water · Dragon
Goldeen
#0118
Goldeen
Water
(Level 33)
Seaking
#0119
Seaking
Water
Staryu
#0120
Staryu
Water
(use Water Stone)
Starmie
#0121
Starmie
Water · Psychic
Mime Jr.
#0439
Mime Jr.
Psychic · Fairy
(after Mimic learned, outside Galar)
Mr. Mime
#0122
Mr. Mime
Psychic · Fairy
(after Mimic learned, in Galar)
Galarian Mr. Mime
#0122
Mr. Mime
Galarian Mr. Mime
Ice · Psychic
(Level 42)
Mr. Rime
#0866
Mr. Rime
Ice · Psychic
Scyther
#0123
Scyther
Bug · Flying
(trade holding Metal Coat)
Scizor
#0212
Scizor
Bug · Steel
(use Black Augurite)
Kleavor
#0900
Kleavor
Bug · Rock
Smoochum
#0238
Smoochum
Ice · Psychic
(Level 30)
Jynx
#0124
Jynx
Ice · Psychic
Elekid
#0239
Elekid
Electric
(Level 30)
Electabuzz
#0125
Electabuzz
Electric
(trade holding Electirizer)
Electivire
#0466
Electivire
Electric
Magby
#0240
Magby
Fire
(Level 30)
Magmar
#0126
Magmar
Fire
(trade holding Magmarizer)
Magmortar
#0467
Magmortar
Fire
Magikarp
#0129
Magikarp
Water
(Level 20)
Gyarados
#0130
Gyarados
Water · Flying
Eevee
#0133
Eevee
Normal
(use Water Stone)
Vaporeon
#0134
Vaporeon
Water
(use Thunder Stone)
Jolteon
#0135
Jolteon
Electric
(use Fire Stone)
Flareon
#0136
Flareon
Fire
Eevee
#0133
Eevee
Normal
(high Friendship, Daytime)
Espeon
#0196
Espeon
Psychic
(high Friendship, Nighttime)
Umbreon
#0197
Umbreon
Dark
Eevee
#0133
Eevee
Normal
(use Leaf Stone, or level up near a Mossy Rock)
Leafeon
#0470
Leafeon
Grass
(use Ice Stone, or level up near an Icy Rock)
Glaceon
#0471
Glaceon
Ice
Eevee
#0133
Eevee
Normal
(after Fairy-type move learned, and either ♥♥ Affection in Gen 6-7 or high friendship in Gen 8+)
Sylveon
#0700
Sylveon
Fairy
Porygon
#0137
Porygon
Normal
(trade holding Upgrade)
Porygon2
#0233
Porygon2
Normal
(trade holding Dubious Disc)
Porygon-Z
#0474
Porygon-Z
Normal
Omanyte
#0138
Omanyte
Rock · Water
(Level 40)
Omastar
#0139
Omastar
Rock · Water
Kabuto
#0140
Kabuto
Rock · Water
(Level 40)
Kabutops
#0141
Kabutops
Rock · Water
Munchlax
#0446
Munchlax
Normal
(high Friendship)
Snorlax
#0143
Snorlax
Normal
Dratini
#0147
Dratini
Dragon
(Level 30)
Dragonair
#0148
Dragonair
Dragon
(Level 55)
Dragonite
#0149
Dragonite
Dragon · Flying
Generation 2
Chikorita
#0152
Chikorita
Grass
(Level 16)
Bayleef
#0153
Bayleef
Grass
(Level 32)
Meganium
#0154
Meganium
Grass
Cyndaquil
#0155
Cyndaquil
Fire
(Level 14, or Level 17 in Legends: Arceus)
Quilava
#0156
Quilava
Fire
(Level 36)
Typhlosion
#0157
Typhlosion
Fire
(Level 36, in Legends: Arceus)
Typhlosion (Hisuian Typhlosion)
#0157
Typhlosion
Hisuian Typhlosion
Fire · Ghost
Totodile
#0158
Totodile
Water
(Level 18)
Croconaw
#0159
Croconaw
Water
(Level 30)
Feraligatr
#0160
Feraligatr
Water
Sentret
#0161
Sentret
Normal
(Level 15)
Furret
#0162
Furret
Normal
Hoothoot
#0163
Hoothoot
Normal · Flying
(Level 20)
Noctowl
#0164
Noctowl
Normal · Flying
Ledyba
#0165
Ledyba
Bug · Flying
(Level 18)
Ledian
#0166
Ledian
Bug · Flying
Spinarak
#0167
Spinarak
Bug · Poison
(Level 22)
Ariados
#0168
Ariados
Bug · Poison
Chinchou
#0170
Chinchou
Water · Electric
(Level 27)
Lanturn
#0171
Lanturn
Water · Electric
Togepi
#0175
Togepi
Fairy
(high Friendship)
Togetic
#0176
Togetic
Fairy · Flying
(use Shiny Stone)
Togekiss
#0468
Togekiss
Fairy · Flying
Natu
#0177
Natu
Psychic · Flying
(Level 25)
Xatu
#0178
Xatu
Psychic · Flying
Mareep
#0179
Mareep
Electric
(Level 15)
Flaaffy
#0180
Flaaffy
Electric
(Level 30)
Ampharos
#0181
Ampharos
Electric
Azurill
#0298
Azurill
Normal · Fairy
(high Friendship)
Marill
#0183
Marill
Water · Fairy
(Level 18)
Azumarill
#0184
Azumarill
Water · Fairy
Bonsly
#0438
Bonsly
Rock
(after Mimic learned)
Sudowoodo
#0185
Sudowoodo
Rock
Hoppip
#0187
Hoppip
Grass · Flying
(Level 18)
Skiploom
#0188
Skiploom
Grass · Flying
(Level 27)
Jumpluff
#0189
Jumpluff
Grass · Flying
Aipom
#0190
Aipom
Normal
(after Double Hit learned)
Ambipom
#0424
Ambipom
Normal
Sunkern
#0191
Sunkern
Grass
(use Sun Stone)
Sunflora
#0192
Sunflora
Grass
Yanma
#0193
Yanma
Bug · Flying
(after Ancient Power learned)
Yanmega
#0469
Yanmega
Bug · Flying
Wooper
#0194
Wooper
Water · Ground
(Level 20)
Quagsire
#0195
Quagsire
Water · Ground
Wooper (Paldean Wooper)
#0194
Wooper
Paldean Wooper
Poison · Ground
(Level 20)
Clodsire
#0980
Clodsire
Poison · Ground
Murkrow
#0198
Murkrow
Dark · Flying
(use Dusk Stone)
Honchkrow
#0430
Honchkrow
Dark · Flying
Misdreavus
#0200
Misdreavus
Ghost
(use Dusk Stone)
Mismagius
#0429
Mismagius
Ghost
Wynaut
#0360
Wynaut
Psychic
(Level 15)
Wobbuffet
#0202
Wobbuffet
Psychic
Pineco
#0204
Pineco
Bug
(Level 31)
Forretress
#0205
Forretress
Bug · Steel
Gligar
#0207
Gligar
Ground · Flying
(hold Razor Fang, Nighttime)
Gliscor
#0472
Gliscor
Ground · Flying
Snubbull
#0209
Snubbull
Fairy
(Level 23)
Granbull
#0210
Granbull
Fairy
Sneasel
#0215
Sneasel
Dark · Ice
(hold Razor Claw, Nighttime)
Weavile
#0461
Weavile
Dark · Ice
Sneasel (Hisuian Sneasel)
#0215
Sneasel
Hisuian Sneasel
Fighting · Poison
(use Razor Claw, Daytime)
Sneasler
#0903
Sneasler
Fighting · Poison
Teddiursa
#0216
Teddiursa
Normal
(Level 30)
Ursaring
#0217
Ursaring
Normal
(use Peat Block, under a full moon, in Legends: Arceus)
Ursaluna
#0901
Ursaluna
Ground · Normal
Slugma
#0218
Slugma
Fire
(Level 38)
Magcargo
#0219
Magcargo
Fire · Rock
Swinub
#0220
Swinub
Ice · Ground
(Level 33)
Piloswine
#0221
Piloswine
Ice · Ground
(after Ancient Power learned)
Mamoswine
#0473
Mamoswine
Ice · Ground
Remoraid
#0223
Remoraid
Water
(Level 25)
Octillery
#0224
Octillery
Water
Mantyke
#0458
Mantyke
Water · Flying
(with Remoraid in party)
Mantine
#0226
Mantine
Water · Flying
Houndour
#0228
Houndour
Dark · Fire
(Level 24)
Houndoom
#0229
Houndoom
Dark · Fire
Phanpy
#0231
Phanpy
Ground
(Level 25)
Donphan
#0232
Donphan
Ground
Larvitar
#0246
Larvitar
Rock · Ground
(Level 30)
Pupitar
#0247
Pupitar
Rock · Ground
(Level 55)
Tyranitar
#0248
Tyranitar
Rock · Dark
Stantler
#0234
Stantler
Normal
(use Psyshield Bash 20 times in Agile Style)
Wyrdeer
#0899
Wyrdeer
Normal · Psychic
Girafarig
#0203
Girafarig
Normal · Psychic
(after Twin Beam learned)
Farigiraf
#0981
Farigiraf
Normal · Psychic
Dunsparce
#0206
Dunsparce
Normal
(after Hyper Drill learned)
Dudunsparce (Two-Segment Form)
#0982
Dudunsparce
Two-Segment Form
Normal
(after Hyper Drill learned, rare)
Dudunsparce (Three-Segment Form)
#0982
Dudunsparce
Three-Segment Form
Normal
Generation 3
Treecko
#0252
Treecko
Grass
(Level 16)
Grovyle
#0253
Grovyle
Grass
(Level 36)
Sceptile
#0254
Sceptile
Grass
Torchic
#0255
Torchic
Fire
(Level 16)
Combusken
#0256
Combusken
Fire · Fighting
(Level 36)
Blaziken
#0257
Blaziken
Fire · Fighting
Mudkip
#0258
Mudkip
Water
(Level 16)
Marshtomp
#0259
Marshtomp
Water · Ground
(Level 36)
Swampert
#0260
Swampert
Water · Ground
Poochyena
#0261
Poochyena
Dark
(Level 18)
Mightyena
#0262
Mightyena
Dark
Zigzagoon
#0263
Zigzagoon
Normal
(Level 20)
Linoone
#0264
Linoone
Normal
Galarian Zigzagoon
#0263
Zigzagoon
Galarian Zigzagoon
Dark · Normal
(Level 20)
Galarian Linoone
#0264
Linoone
Galarian Linoone
Dark · Normal
(Level 35, Nighttime)
Obstagoon
#0862
Obstagoon
Dark · Normal
Wurmple
#0265
Wurmple
Bug
(Level 7, random based on personality)
Silcoon
#0266
Silcoon
Bug
(Level 10)
Beautifly
#0267
Beautifly
Bug · Flying
(Level 7, random based on personality)
Cascoon
#0268
Cascoon
Bug
(Level 10)
Dustox
#0269
Dustox
Bug · Poison
Lotad
#0270
Lotad
Water · Grass
(Level 14)
Lombre
#0271
Lombre
Water · Grass
(use Water Stone)
Ludicolo
#0272
Ludicolo
Water · Grass
Seedot
#0273
Seedot
Grass
(Level 14)
Nuzleaf
#0274
Nuzleaf
Grass · Dark
(use Leaf Stone)
Shiftry
#0275
Shiftry
Grass · Dark
Taillow
#0276
Taillow
Normal · Flying
(Level 22)
Swellow
#0277
Swellow
Normal · Flying
Wingull
#0278
Wingull
Water · Flying
(Level 25)
Pelipper
#0279
Pelipper
Water · Flying
Ralts
#0280
Ralts
Psychic · Fairy
(Level 20)
Kirlia
#0281
Kirlia
Psychic · Fairy
(Level 30)
Gardevoir
#0282
Gardevoir
Psychic · Fairy
(use Dawn Stone, Male)
Gallade
#0475
Gallade
Psychic · Fighting
Surskit
#0283
Surskit
Bug · Water
(Level 22)
Masquerain
#0284
Masquerain
Bug · Flying
Shroomish
#0285
Shroomish
Grass
(Level 23)
Breloom
#0286
Breloom
Grass · Fighting
Slakoth
#0287
Slakoth
Normal
(Level 18)
Vigoroth
#0288
Vigoroth
Normal
(Level 36)
Slaking
#0289
Slaking
Normal
Nincada
#0290
Nincada
Bug · Ground
(Level 20)
Ninjask
#0291
Ninjask
Bug · Flying
(Level 20, empty spot in party, Pokéball in bag)
Ninjask
#0291
Ninjask
Bug · Flying
+
Shedinja
#0292
Shedinja
Bug · Ghost
Whismur
#0293
Whismur
Normal
(Level 20)
Loudred
#0294
Loudred
Normal
(Level 40)
Exploud
#0295
Exploud
Normal
Makuhita
#0296
Makuhita
Fighting
(Level 24)
Hariyama
#0297
Hariyama
Fighting
Nosepass
#0299
Nosepass
Rock
(level up in a Magnetic Field area)
Probopass
#0476
Probopass
Rock · Steel
Skitty
#0300
Skitty
Normal
(use Moon Stone)
Delcatty
#0301
Delcatty
Normal
Aron
#0304
Aron
Steel · Rock
(Level 32)
Lairon
#0305
Lairon
Steel · Rock
(Level 42)
Aggron
#0306
Aggron
Steel · Rock
Meditite
#0307
Meditite
Fighting · Psychic
(Level 37)
Medicham
#0308
Medicham
Fighting · Psychic
Electrike
#0309
Electrike
Electric
(Level 26)
Manectric
#0310
Manectric
Electric
Budew
#0406
Budew
Grass · Poison
(high Friendship, Daytime)
Roselia
#0315
Roselia
Grass · Poison
(use Shiny Stone)
Roserade
#0407
Roserade
Grass · Poison
Gulpin
#0316
Gulpin
Poison
(Level 26)
Swalot
#0317
Swalot
Poison
Carvanha
#0318
Carvanha
Water · Dark
(Level 30)
Sharpedo
#0319
Sharpedo
Water · Dark
Wailmer
#0320
Wailmer
Water
(Level 40)
Wailord
#0321
Wailord
Water
Numel
#0322
Numel
Fire · Ground
(Level 33)
Camerupt
#0323
Camerupt
Fire · Ground
Spoink
#0325
Spoink
Psychic
(Level 32)
Grumpig
#0326
Grumpig
Psychic
Trapinch
#0328
Trapinch
Ground
(Level 35)
Vibrava
#0329
Vibrava
Ground · Dragon
(Level 45)
Flygon
#0330
Flygon
Ground · Dragon
Cacnea
#0331
Cacnea
Grass
(Level 32)
Cacturne
#0332
Cacturne
Grass · Dark
Swablu
#0333
Swablu
Normal · Flying
(Level 35)
Altaria
#0334
Altaria
Dragon · Flying
Barboach
#0339
Barboach
Water · Ground
(Level 30)
Whiscash
#0340
Whiscash
Water · Ground
Corphish
#0341
Corphish
Water
(Level 30)
Crawdaunt
#0342
Crawdaunt
Water · Dark
Baltoy
#0343
Baltoy
Ground · Psychic
(Level 36)
Claydol
#0344
Claydol
Ground · Psychic
Lileep
#0345
Lileep
Rock · Grass
(Level 40)
Cradily
#0346
Cradily
Rock · Grass
Anorith
#0347
Anorith
Rock · Bug
(Level 40)
Armaldo
#0348
Armaldo
Rock · Bug
Feebas
#0349
Feebas
Water
(trade holding Prism Scale, or level up with max Beauty)
Milotic
#0350
Milotic
Water
Shuppet
#0353
Shuppet
Ghost
(Level 37)
Banette
#0354
Banette
Ghost
Duskull
#0355
Duskull
Ghost
(Level 37)
Dusclops
#0356
Dusclops
Ghost
(trade holding Reaper Cloth)
Dusknoir
#0477
Dusknoir
Ghost
Chingling
#0433
Chingling
Psychic
(high Friendship, Nighttime)
Chimecho
#0358
Chimecho
Psychic
Snorunt
#0361
Snorunt
Ice
(Level 42)
Glalie
#0362
Glalie
Ice
(use Dawn Stone, Female)
Froslass
#0478
Froslass
Ice · Ghost
Spheal
#0363
Spheal
Ice · Water
(Level 32)
Sealeo
#0364
Sealeo
Ice · Water
(Level 44)
Walrein
#0365
Walrein
Ice · Water
Clamperl
#0366
Clamperl
Water
(trade holding Deep Sea Tooth)
Huntail
#0367
Huntail
Water
(trade holding Deep Sea Scale)
Gorebyss
#0368
Gorebyss
Water
Bagon
#0371
Bagon
Dragon
(Level 30)
Shelgon
#0372
Shelgon
Dragon
(Level 50)
Salamence
#0373
Salamence
Dragon · Flying
Beldum
#0374
Beldum
Steel · Psychic
(Level 20)
Metang
#0375
Metang
Steel · Psychic
(Level 45)
Metagross
#0376
Metagross
Steel · Psychic
Generation 4
Turtwig
#0387
Turtwig
Grass
(Level 18)
Grotle
#0388
Grotle
Grass
(Level 32)
Torterra
#0389
Torterra
Grass · Ground
Chimchar
#0390
Chimchar
Fire
(Level 14)
Monferno
#0391
Monferno
Fire · Fighting
(Level 36)
Infernape
#0392
Infernape
Fire · Fighting
Piplup
#0393
Piplup
Water
(Level 16)
Prinplup
#0394
Prinplup
Water
(Level 36)
Empoleon
#0395
Empoleon
Water · Steel
Starly
#0396
Starly
Normal · Flying
(Level 14)
Staravia
#0397
Staravia
Normal · Flying
(Level 34)
Staraptor
#0398
Staraptor
Normal · Flying
Bidoof
#0399
Bidoof
Normal
(Level 15)
Bibarel
#0400
Bibarel
Normal · Water
Kricketot
#0401
Kricketot
Bug
(Level 10)
Kricketune
#0402
Kricketune
Bug
Shinx
#0403
Shinx
Electric
(Level 15)
Luxio
#0404
Luxio
Electric
(Level 30)
Luxray
#0405
Luxray
Electric
Cranidos
#0408
Cranidos
Rock
(Level 30)
Rampardos
#0409
Rampardos
Rock
Shieldon
#0410
Shieldon
Rock · Steel
(Level 30)
Bastiodon
#0411
Bastiodon
Rock · Steel
Burmy (Plant Cloak)
#0412
Burmy
All forms
Bug
(Level 20, Male)
Mothim
#0414
Mothim
Bug · Flying
Burmy (Plant Cloak)
#0412
Burmy
Plant Cloak
Bug
(Level 20, Female, in grass)
Wormadam (Plant Cloak)
#0413
Wormadam
Plant Cloak
Bug · Grass
Burmy (Sandy Cloak)
#0412
Burmy
Sandy Cloak
Bug
(Level 20, Female, in caves)
Wormadam (Sandy Cloak)
#0413
Wormadam
Sandy Cloak
Bug · Ground
Burmy (Trash Cloak)
#0412
Burmy
Trash Cloak
Bug
(Level 20, Female, in buildings)
Wormadam (Trash Cloak)
#0413
Wormadam
Trash Cloak
Bug · Steel
Combee
#0415
Combee
Bug · Flying
(Level 21, Female)
Vespiquen
#0416
Vespiquen
Bug · Flying
Buizel
#0418
Buizel
Water
(Level 26)
Floatzel
#0419
Floatzel
Water
Cherubi
#0420
Cherubi
Grass
(Level 25)
Cherrim
#0421
Cherrim
Grass
Shellos
#0422
Shellos
Water
(Level 30)
Gastrodon
#0423
Gastrodon
Water · Ground
Drifloon
#0425
Drifloon
Ghost · Flying
(Level 28)
Drifblim
#0426
Drifblim
Ghost · Flying
Buneary
#0427
Buneary
Normal
(high Friendship)
Lopunny
#0428
Lopunny
Normal
Glameow
#0431
Glameow
Normal
(Level 38)
Purugly
#0432
Purugly
Normal
Stunky
#0434
Stunky
Poison · Dark
(Level 34)
Skuntank
#0435
Skuntank
Poison · Dark
Bronzor
#0436
Bronzor
Steel · Psychic
(Level 33)
Bronzong
#0437
Bronzong
Steel · Psychic
Gible
#0443
Gible
Dragon · Ground
(Level 24)
Gabite
#0444
Gabite
Dragon · Ground
(Level 48)
Garchomp
#0445
Garchomp
Dragon · Ground
Riolu
#0447
Riolu
Fighting
(high Friendship, Daytime)
Lucario
#0448
Lucario
Fighting · Steel
Hippopotas
#0449
Hippopotas
Ground
(Level 34)
Hippowdon
#0450
Hippowdon
Ground
Skorupi
#0451
Skorupi
Poison · Bug
(Level 40)
Drapion
#0452
Drapion
Poison · Dark
Croagunk
#0453
Croagunk
Poison · Fighting
(Level 37)
Toxicroak
#0454
Toxicroak
Poison · Fighting
Finneon
#0456
Finneon
Water
(Level 31)
Lumineon
#0457
Lumineon
Water
Snover
#0459
Snover
Grass · Ice
(Level 40)
Abomasnow
#0460
Abomasnow
Grass · Ice
Generation 5
Snivy
#0495
Snivy
Grass
(Level 17)
Servine
#0496
Servine
Grass
(Level 36)
Serperior
#0497
Serperior
Grass
Tepig
#0498
Tepig
Fire
(Level 17)
Pignite
#0499
Pignite
Fire · Fighting
(Level 36)
Emboar
#0500
Emboar
Fire · Fighting
Oshawott
#0501
Oshawott
Water
(Level 17)
Dewott
#0502
Dewott
Water
(Level 36)
Samurott
#0503
Samurott
Water
(Level 36, in Legends: Arceus)
Samurott (Hisuian Samurott)
#0503
Samurott
Hisuian Samurott
Water · Dark
Patrat
#0504
Patrat
Normal
(Level 20)
Watchog
#0505
Watchog
Normal
Lillipup
#0506
Lillipup
Normal
(Level 16)
Herdier
#0507
Herdier
Normal
(Level 32)
Stoutland
#0508
Stoutland
Normal
Purrloin
#0509
Purrloin
Dark
(Level 20)
Liepard
#0510
Liepard
Dark
Pansage
#0511
Pansage
Grass
(use Leaf Stone)
Simisage
#0512
Simisage
Grass
Pansear
#0513
Pansear
Fire
(use Fire Stone)
Simisear
#0514
Simisear
Fire
Panpour
#0515
Panpour
Water
(use Water Stone)
Simipour
#0516
Simipour
Water
Munna
#0517
Munna
Psychic
(use Moon Stone)
Musharna
#0518
Musharna
Psychic
Pidove
#0519
Pidove
Normal · Flying
(Level 21)
Tranquill
#0520
Tranquill
Normal · Flying
(Level 32)
Unfezant
#0521
Unfezant
Normal · Flying
Blitzle
#0522
Blitzle
Electric
(Level 27)
Zebstrika
#0523
Zebstrika
Electric
Roggenrola
#0524
Roggenrola
Rock
(Level 25)
Boldore
#0525
Boldore
Rock
(Trade)
Gigalith
#0526
Gigalith
Rock
Woobat
#0527
Woobat
Psychic · Flying
(high Friendship)
Swoobat
#0528
Swoobat
Psychic · Flying
Drilbur
#0529
Drilbur
Ground
(Level 31)
Excadrill
#0530
Excadrill
Ground · Steel
Timburr
#0532
Timburr
Fighting
(Level 25)
Gurdurr
#0533
Gurdurr
Fighting
(Trade)
Conkeldurr
#0534
Conkeldurr
Fighting
Tympole
#0535
Tympole
Water
(Level 25)
Palpitoad
#0536
Palpitoad
Water · Ground
(Level 36)
Seismitoad
#0537
Seismitoad
Water · Ground
Sewaddle
#0540
Sewaddle
Bug · Grass
(Level 20)
Swadloon
#0541
Swadloon
Bug · Grass
(high Friendship)
Leavanny
#0542
Leavanny
Bug · Grass
Venipede
#0543
Venipede
Bug · Poison
(Level 22)
Whirlipede
#0544
Whirlipede
Bug · Poison
(Level 30)
Scolipede
#0545
Scolipede
Bug · Poison
Cottonee
#0546
Cottonee
Grass · Fairy
(use Sun Stone)
Whimsicott
#0547
Whimsicott
Grass · Fairy
Petilil
#0548
Petilil
Grass
(use Sun Stone)
Lilligant
#0549
Lilligant
Grass
(use Sun Stone, in Legends: Arceus)
Lilligant (Hisuian Lilligant)
#0549
Lilligant
Hisuian Lilligant
Grass · Fighting
Sandile
#0551
Sandile
Ground · Dark
(Level 29)
Krokorok
#0552
Krokorok
Ground · Dark
(Level 40)
Krookodile
#0553
Krookodile
Ground · Dark
Darumaka
#0554
Darumaka
Fire
(Level 35)
Darmanitan (Standard Mode)
#0555
Darmanitan
Standard Mode
Fire
Galarian Darumaka
#0554
Darumaka
Galarian Darumaka
Ice
(use Ice Stone)
Darmanitan (Galarian Standard Mode)
#0555
Darmanitan
Galarian Standard Mode
Ice
Dwebble
#0557
Dwebble
Bug · Rock
(Level 34)
Crustle
#0558
Crustle
Bug · Rock
Scraggy
#0559
Scraggy
Dark · Fighting
(Level 39)
Scrafty
#0560
Scrafty
Dark · Fighting
Yamask
#0562
Yamask
Ghost
(Level 34)
Cofagrigus
#0563
Cofagrigus
Ghost
Galarian Yamask
#0562
Yamask
Galarian Yamask
Ground · Ghost
(near Dusty Bowl)
Runerigus
#0867
Runerigus
Ground · Ghost
Tirtouga
#0564
Tirtouga
Water · Rock
(Level 37)
Carracosta
#0565
Carracosta
Water · Rock
Archen
#0566
Archen
Rock · Flying
(Level 37)
Archeops
#0567
Archeops
Rock · Flying
Trubbish
#0568
Trubbish
Poison
(Level 36)
Garbodor
#0569
Garbodor
Poison
Zorua
#0570
Zorua
Dark
(Level 30)
Zoroark
#0571
Zoroark
Dark
Zorua (Hisuian Zorua)
#0570
Zorua
Hisuian Zorua
Normal · Ghost
(Level 30, in Legends: Arceus)
Zoroark (Hisuian Zoroark)
#0571
Zoroark
Hisuian Zoroark
Normal · Ghost
Minccino
#0572
Minccino
Normal
(use Shiny Stone)
Cinccino
#0573
Cinccino
Normal
Gothita
#0574
Gothita
Psychic
(Level 32)
Gothorita
#0575
Gothorita
Psychic
(Level 41)
Gothitelle
#0576
Gothitelle
Psychic
Solosis
#0577
Solosis
Psychic
(Level 32)
Duosion
#0578
Duosion
Psychic
(Level 41)
Reuniclus
#0579
Reuniclus
Psychic
Ducklett
#0580
Ducklett
Water · Flying
(Level 35)
Swanna
#0581
Swanna
Water · Flying
Vanillite
#0582
Vanillite
Ice
(Level 35)
Vanillish
#0583
Vanillish
Ice
(Level 47)
Vanilluxe
#0584
Vanilluxe
Ice
Deerling
#0585
Deerling
Normal · Grass
(Level 34)
Sawsbuck
#0586
Sawsbuck
Normal · Grass
Karrablast
#0588
Karrablast
Bug
(Trade with Shelmet)
Escavalier
#0589
Escavalier
Bug · Steel
Foongus
#0590
Foongus
Grass · Poison
(Level 39)
Amoonguss
#0591
Amoonguss
Grass · Poison
Frillish
#0592
Frillish
Water · Ghost
(Level 40)
Jellicent
#0593
Jellicent
Water · Ghost
Joltik
#0595
Joltik
Bug · Electric
(Level 36)
Galvantula
#0596
Galvantula
Bug · Electric
Ferroseed
#0597
Ferroseed
Grass · Steel
(Level 40)
Ferrothorn
#0598
Ferrothorn
Grass · Steel
Klink
#0599
Klink
Steel
(Level 38)
Klang
#0600
Klang
Steel
(Level 49)
Klinklang
#0601
Klinklang
Steel
Tynamo
#0602
Tynamo
Electric
(Level 39)
Eelektrik
#0603
Eelektrik
Electric
(use Thunder Stone)
Eelektross
#0604
Eelektross
Electric
Elgyem
#0605
Elgyem
Psychic
(Level 42)
Beheeyem
#0606
Beheeyem
Psychic
Litwick
#0607
Litwick
Ghost · Fire
(Level 41)
Lampent
#0608
Lampent
Ghost · Fire
(use Dusk Stone)
Chandelure
#0609
Chandelure
Ghost · Fire
Axew
#0610
Axew
Dragon
(Level 38)
Fraxure
#0611
Fraxure
Dragon
(Level 48)
Haxorus
#0612
Haxorus
Dragon
Cubchoo
#0613
Cubchoo
Ice
(Level 37)
Beartic
#0614
Beartic
Ice
Shelmet
#0616
Shelmet
Bug
(Trade with Karrablast)
Accelgor
#0617
Accelgor
Bug
Mienfoo
#0619
Mienfoo
Fighting
(Level 50)
Mienshao
#0620
Mienshao
Fighting
Golett
#0622
Golett
Ground · Ghost
(Level 43)
Golurk
#0623
Golurk
Ground · Ghost
Pawniard
#0624
Pawniard
Dark · Steel
(Level 52)
Bisharp
#0625
Bisharp
Dark · Steel
(defeat 3 Bisharp that are holding Leader's Crest)
Kingambit
#0983
Kingambit
Dark · Steel
Rufflet
#0627
Rufflet
Normal · Flying
(Level 54)
Braviary
#0628
Braviary
Normal · Flying
(Level 54, in Legends: Arceus)
Braviary (Hisuian Braviary)
#0628
Braviary
Hisuian Braviary
Psychic · Flying
Vullaby
#0629
Vullaby
Dark · Flying
(Level 54)
Mandibuzz
#0630
Mandibuzz
Dark · Flying
Deino
#0633
Deino
Dark · Dragon
(Level 50)
Zweilous
#0634
Zweilous
Dark · Dragon
(Level 64)
Hydreigon
#0635
Hydreigon
Dark · Dragon
Larvesta
#0636
Larvesta
Bug · Fire
(Level 59)
Volcarona
#0637
Volcarona
Bug · Fire
Generation 6
Chespin
#0650
Chespin
Grass
(Level 16)
Quilladin
#0651
Quilladin
Grass
(Level 36)
Chesnaught
#0652
Chesnaught
Grass · Fighting
Fennekin
#0653
Fennekin
Fire
(Level 16)
Braixen
#0654
Braixen
Fire
(Level 36)
Delphox
#0655
Delphox
Fire · Psychic
Froakie
#0656
Froakie
Water
(Level 16)
Frogadier
#0657
Frogadier
Water
(Level 36)
Greninja
#0658
Greninja
Water · Dark
Bunnelby
#0659
Bunnelby
Normal
(Level 20)
Diggersby
#0660
Diggersby
Normal · Ground
Fletchling
#0661
Fletchling
Normal · Flying
(Level 17)
Fletchinder
#0662
Fletchinder
Fire · Flying
(Level 35)
Talonflame
#0663
Talonflame
Fire · Flying
Scatterbug
#0664
Scatterbug
Bug
(Level 9)
Spewpa
#0665
Spewpa
Bug
(Level 12)
Vivillon
#0666
Vivillon
Bug · Flying
Litleo
#0667
Litleo
Fire · Normal
(Level 35)
Pyroar
#0668
Pyroar
Fire · Normal
Flabébé
#0669
Flabébé
Fairy
(Level 19)
Floette
#0670
Floette
Fairy
(use Shiny Stone)
Florges
#0671
Florges
Fairy
Skiddo
#0672
Skiddo
Grass
(Level 32)
Gogoat
#0673
Gogoat
Grass
Pancham
#0674
Pancham
Fighting
(Level 32, Dark type Pokémon in party)
Pangoro
#0675
Pangoro
Fighting · Dark
Espurr
#0677
Espurr
Psychic
(Level 25, Male)
Meowstic (Male)
#0678
Meowstic
Male
Psychic
(Level 25, Female)
Meowstic (Female)
#0678
Meowstic
Female
Psychic
Honedge
#0679
Honedge
Steel · Ghost
(Level 35)
Doublade
#0680
Doublade
Steel · Ghost
(use Dusk Stone)
Aegislash (Shield Forme)
#0681
Aegislash
Steel · Ghost
Spritzee
#0682
Spritzee
Fairy
(trade holding Sachet)
Aromatisse
#0683
Aromatisse
Fairy
Swirlix
#0684
Swirlix
Fairy
(trade holding Whipped Dream)
Slurpuff
#0685
Slurpuff
Fairy
Inkay
#0686
Inkay
Dark · Psychic
(Level 30, holding console upside down)
Malamar
#0687
Malamar
Dark · Psychic
Binacle
#0688
Binacle
Rock · Water
(Level 39)
Barbaracle
#0689
Barbaracle
Rock · Water
Skrelp
#0690
Skrelp
Poison · Water
(Level 48)
Dragalge
#0691
Dragalge
Poison · Dragon
Clauncher
#0692
Clauncher
Water
(Level 37)
Clawitzer
#0693
Clawitzer
Water
Helioptile
#0694
Helioptile
Electric · Normal
(use Sun Stone)
Heliolisk
#0695
Heliolisk
Electric · Normal
Tyrunt
#0696
Tyrunt
Rock · Dragon
(Level 39, Daytime)
Tyrantrum
#0697
Tyrantrum
Rock · Dragon
Amaura
#0698
Amaura
Rock · Ice
(Level 39, Nighttime)
Aurorus
#0699
Aurorus
Rock · Ice
Goomy
#0704
Goomy
Dragon
(Level 40)
Sliggoo
#0705
Sliggoo
Dragon
(Level 50, during rain)
Goodra
#0706
Goodra
Dragon
(Level 40, in Legends: Arceus)
Sliggoo (Hisuian Sliggoo)
#0705
Sliggoo
Hisuian Sliggoo
Steel · Dragon
(Level 50, during rain, in Legends: Arceus)
Goodra (Hisuian Goodra)
#0706
Goodra
Hisuian Goodra
Steel · Dragon
Phantump
#0708
Phantump
Ghost · Grass
(Trade)
Trevenant
#0709
Trevenant
Ghost · Grass
Pumpkaboo (Average Size)
#0710
Pumpkaboo
Ghost · Grass
(Trade)
Gourgeist (Average Size)
#0711
Gourgeist
Ghost · Grass
Bergmite
#0712
Bergmite
Ice
(Level 37)
Avalugg
#0713
Avalugg
Ice
(Level 37, in Legends: Arceus)
Avalugg (Hisuian Avalugg)
#0713
Avalugg
Hisuian Avalugg
Ice · Rock
Noibat
#0714
Noibat
Flying · Dragon
(Level 48)
Noivern
#0715
Noivern
Flying · Dragon
Generation 7
Rowlet
#0722
Rowlet
Grass · Flying
(Level 17)
Dartrix
#0723
Dartrix
Grass · Flying
(Level 34)
Decidueye
#0724
Decidueye
Grass · Ghost
(Level 36, in Legends: Arceus)
Decidueye (Hisuian Decidueye)
#0724
Decidueye
Hisuian Decidueye
Grass · Fighting
Litten
#0725
Litten
Fire
(Level 17)
Torracat
#0726
Torracat
Fire
(Level 34)
Incineroar
#0727
Incineroar
Fire · Dark
Popplio
#0728
Popplio
Water
(Level 17)
Brionne
#0729
Brionne
Water
(Level 34)
Primarina
#0730
Primarina
Water · Fairy
Pikipek
#0731
Pikipek
Normal · Flying
(Level 14)
Trumbeak
#0732
Trumbeak
Normal · Flying
(Level 28)
Toucannon
#0733
Toucannon
Normal · Flying
Yungoos
#0734
Yungoos
Normal
(Level 20, Daytime)
Gumshoos
#0735
Gumshoos
Normal
Grubbin
#0736
Grubbin
Bug
(Level 20)
Charjabug
#0737
Charjabug
Bug · Electric
(use Thunder Stone, in Gen 8, or level up in a Magnetic Field area)
Vikavolt
#0738
Vikavolt
Bug · Electric
Crabrawler
#0739
Crabrawler
Fighting
(use Ice Stone, or at Mount Lanakila in Alola)
Crabominable
#0740
Crabominable
Fighting · Ice
Cutiefly
#0742
Cutiefly
Bug · Fairy
(Level 25)
Ribombee
#0743
Ribombee
Bug · Fairy
Rockruff
#0744
Rockruff
Rock
(Level 25, Daytime)
Lycanroc (Midday Form)
#0745
Lycanroc
Midday Form
Rock
(Level 25, Nighttime)
Lycanroc (Midnight Form)
#0745
Lycanroc
Midnight Form
Rock
Rockruff (Own Tempo Rockruff)
#0744
Rockruff
Own Tempo Rockruff
Rock
(Level 25, Dusk)
Lycanroc (Dusk Form)
#0745
Lycanroc
Dusk Form
Rock
Mareanie
#0747
Mareanie
Poison · Water
(Level 38)
Toxapex
#0748
Toxapex
Poison · Water
Mudbray
#0749
Mudbray
Ground
(Level 30)
Mudsdale
#0750
Mudsdale
Ground
Dewpider
#0751
Dewpider
Water · Bug
(Level 22)
Araquanid
#0752
Araquanid
Water · Bug
Fomantis
#0753
Fomantis
Grass
(Level 34, Daytime)
Lurantis
#0754
Lurantis
Grass
Morelull
#0755
Morelull
Grass · Fairy
(Level 24)
Shiinotic
#0756
Shiinotic
Grass · Fairy
Salandit
#0757
Salandit
Poison · Fire
(Level 33, Female)
Salazzle
#0758
Salazzle
Poison · Fire
Stufful
#0759
Stufful
Normal · Fighting
(Level 27)
Bewear
#0760
Bewear
Normal · Fighting
Bounsweet
#0761
Bounsweet
Grass
(Level 18)
Steenee
#0762
Steenee
Grass
(after Stomp learned)
Tsareena
#0763
Tsareena
Grass
Wimpod
#0767
Wimpod
Bug · Water
(Level 30)
Golisopod
#0768
Golisopod
Bug · Water
Sandygast
#0769
Sandygast
Ghost · Ground
(Level 42)
Palossand
#0770
Palossand
Ghost · Ground
Type: Null
#0772
Type: Null
Normal
(high Friendship)
Silvally
#0773
Silvally
Normal
Jangmo-o
#0782
Jangmo-o
Dragon
(Level 35)
Hakamo-o
#0783
Hakamo-o
Dragon · Fighting
(Level 45)
Kommo-o
#0784
Kommo-o
Dragon · Fighting
Cosmog
#0789
Cosmog
Psychic
(Level 43)
Cosmoem
#0790
Cosmoem
Psychic
(Level 53, in Pokémon Sun or Ultra Sun)
Solgaleo
#0791
Solgaleo
Psychic · Steel
(Level 53, in Pokémon Moon or Ultra Moon)
Lunala
#0792
Lunala
Psychic · Ghost
Poipole
#0803
Poipole
Poison
(after Dragon Pulse learned)
Naganadel
#0804
Naganadel
Poison · Dragon
Meltan
#0808
Meltan
Steel
(Pokémon GO only, 400 Meltan Candies)
Melmetal
#0809
Melmetal
Steel
Generation 8
Grookey
#0810
Grookey
Grass
(Level 16)
Thwackey
#0811
Thwackey
Grass
(Level 35)
Rillaboom
#0812
Rillaboom
Grass
Scorbunny
#0813
Scorbunny
Fire
(Level 16)
Raboot
#0814
Raboot
Fire
(Level 35)
Cinderace
#0815
Cinderace
Fire
Sobble
#0816
Sobble
Water
(Level 16)
Drizzile
#0817
Drizzile
Water
(Level 35)
Inteleon
#0818
Inteleon
Water
Blipbug
#0824
Blipbug
Bug
(Level 10)
Dottler
#0825
Dottler
Bug · Psychic
(Level 30)
Orbeetle
#0826
Orbeetle
Bug · Psychic
Rookidee
#0821
Rookidee
Flying
(Level 18)
Corvisquire
#0822
Corvisquire
Flying
(Level 38)
Corviknight
#0823
Corviknight
Flying · Steel
Skwovet
#0819
Skwovet
Normal
(Level 24)
Greedent
#0820
Greedent
Normal
Nickit
#0827
Nickit
Dark
(Level 18)
Thievul
#0828
Thievul
Dark
Wooloo
#0831
Wooloo
Normal
(Level 24)
Dubwool
#0832
Dubwool
Normal
Chewtle
#0833
Chewtle
Water
(Level 22)
Drednaw
#0834
Drednaw
Water · Rock
Yamper
#0835
Yamper
Electric
(Level 25)
Boltund
#0836
Boltund
Electric
Gossifleur
#0829
Gossifleur
Grass
(Level 20)
Eldegoss
#0830
Eldegoss
Grass
Sizzlipede
#0850
Sizzlipede
Fire · Bug
(Level 28)
Centiskorch
#0851
Centiskorch
Fire · Bug
Rolycoly
#0837
Rolycoly
Rock
(Level 18)
Carkol
#0838
Carkol
Rock · Fire
(Level 34)
Coalossal
#0839
Coalossal
Rock · Fire
Arrokuda
#0846
Arrokuda
Water
(Level 26)
Barraskewda
#0847
Barraskewda
Water
Milcery
#0868
Milcery
Fairy
(spin around holding Sweet)
Alcremie
#0869
Alcremie
Fairy
Applin
#0840
Applin
Grass · Dragon
(use Tart Apple)
Flapple
#0841
Flapple
Grass · Dragon
(use Sweet Apple)
Appletun
#0842
Appletun
Grass · Dragon
Galarian Farfetch'd
#0083
Farfetch'd
Galarian Farfetch'd
Fighting
(achieve 3 critical hits in one battle)
Sirfetch'd
#0865
Sirfetch'd
Fighting
Galarian Corsola
#0222
Corsola
Galarian Corsola
Ghost
(Level 38)
Cursola
#0864
Cursola
Ghost
Impidimp
#0859
Impidimp
Dark · Fairy
(Level 32)
Morgrem
#0860
Morgrem
Dark · Fairy
(Level 42)
Grimmsnarl
#0861
Grimmsnarl
Dark · Fairy
Hatenna
#0856
Hatenna
Psychic
(Level 32)
Hattrem
#0857
Hattrem
Psychic
(Level 42)
Hatterene
#0858
Hatterene
Psychic · Fairy
Cufant
#0878
Cufant
Steel
(Level 34)
Copperajah
#0879
Copperajah
Steel
Toxel
#0848
Toxel
Electric · Poison
(Level 30, with an amped Nature)
Toxtricity (Amped Form)
#0849
Toxtricity
Amped Form
Electric · Poison
(Level 30, with a low key Nature)
Toxtricity (Low Key Form)
#0849
Toxtricity
Low Key Form
Electric · Poison
Silicobra
#0843
Silicobra
Ground
(Level 36)
Sandaconda
#0844
Sandaconda
Ground
Sinistea
#0854
Sinistea
Ghost
(use Cracked Pot)
Polteageist
#0855
Polteageist
Ghost
Snom
#0872
Snom
Ice · Bug
(high Friendship, Nighttime)
Frosmoth
#0873
Frosmoth
Ice · Bug
Clobbopus
#0852
Clobbopus
Fighting
(after Taunt learned)
Grapploct
#0853
Grapploct
Fighting
Dreepy
#0885
Dreepy
Dragon · Ghost
(Level 50)
Drakloak
#0886
Drakloak
Dragon · Ghost
(Level 60)
Dragapult
#0887
Dragapult
Dragon · Ghost
Kubfu
#0891
Kubfu
Fighting
(use Scroll Of Darkness, or in Tower of Darkness in Galar)
Urshifu (Single Strike Style)
#0892
Urshifu
Single Strike Style
Fighting · Dark
(use Scroll Of Waters, or in Tower of Water in Galar)
Urshifu (Rapid Strike Style)
#0892
Urshifu
Rapid Strike Style
Fighting · Water
Basculin (White-Striped Form)
#0550
Basculin
White-Striped Form
Water
(Male, receive 294 recoil damage in battle)
Basculegion (Male)
#0902
Basculegion
Male
Water · Ghost
(Female, receive 294 recoil damage in battle)
Basculegion (Female)
#0902
Basculegion
Female
Water · Ghost
Qwilfish (Hisuian Qwilfish)
#0211
Qwilfish
Hisuian Qwilfish
Dark · Poison
(use Barb Barrage 20 times in Strong Style)
Overqwil
#0904
Overqwil
Dark · Poison
Generation 9
Sprigatito
#0906
Sprigatito
Grass
(Level 16)
Floragato
#0907
Floragato
Grass
(Level 36)
Meowscarada
#0908
Meowscarada
Grass · Dark
Fuecoco
#0909
Fuecoco
Fire
(Level 16)
Crocalor
#0910
Crocalor
Fire
(Level 36)
Skeledirge
#0911
Skeledirge
Fire · Ghost
Quaxly
#0912
Quaxly
Water
(Level 16)
Quaxwell
#0913
Quaxwell
Water
(Level 36)
Quaquaval
#0914
Quaquaval
Water · Fighting
Lechonk
#0915
Lechonk
Normal
(Level 18, Male)
Oinkologne (Male)
#0916
Oinkologne
Male
Normal
(Level 18, Female)
Oinkologne (Female)
#0916
Oinkologne
Female
Normal
Tarountula
#0917
Tarountula
Bug
(Level 15)
Spidops
#0918
Spidops
Bug
Nymble
#0919
Nymble
Bug
(Level 24)
Lokix
#0920
Lokix
Bug · Dark
Rellor
#0953
Rellor
Bug
(walk 1,000 steps in Let's Go mode)
Rabsca
#0954
Rabsca
Bug · Psychic
Greavard
#0971
Greavard
Ghost
(Level 30, Nighttime)
Houndstone
#0972
Houndstone
Ghost
Flittle
#0955
Flittle
Psychic
(Level 35)
Espathra
#0956
Espathra
Psychic
Wiglett
#0960
Wiglett
Water
(Level 26)
Wugtrio
#0961
Wugtrio
Water
Finizen
#0963
Finizen
Water
(Level 38, while in multiplayer)
Palafin (Zero Form)
#0964
Palafin
Zero Form
Water
Smoliv
#0928
Smoliv
Grass · Normal
(Level 25)
Dolliv
#0929
Dolliv
Grass · Normal
(Level 35)
Arboliva
#0930
Arboliva
Grass · Normal
Capsakid
#0951
Capsakid
Grass
(use Fire Stone)
Scovillain
#0952
Scovillain
Grass · Fire
Tadbulb
#0938
Tadbulb
Electric
(use Thunder Stone)
Bellibolt
#0939
Bellibolt
Electric
Varoom
#0965
Varoom
Steel · Poison
(Level 40)
Revavroom
#0966
Revavroom
Steel · Poison
Tandemaus
#0924
Tandemaus
Normal
(Level 25, rare)
Maushold (Family of Three)
#0925
Maushold
Family of Three
Normal
(Level 25)
Maushold (Family of Four)
#0925
Maushold
Family of Four
Normal
Cetoddle
#0974
Cetoddle
Ice
(use Ice Stone)
Cetitan
#0975
Cetitan
Ice
Frigibax
#0996
Frigibax
Dragon · Ice
(Level 35)
Arctibax
#0997
Arctibax
Dragon · Ice
(Level 54)
Baxcalibur
#0998
Baxcalibur
Dragon · Ice
Pawmi
#0921
Pawmi
Electric
(Level 18)
Pawmo
#0922
Pawmo
Electric · Fighting
(walk 1,000 steps in Let's Go mode)
Pawmot
#0923
Pawmot
Electric · Fighting
Wattrel
#0940
Wattrel
Electric · Flying
(Level 25)
Kilowattrel
#0941
Kilowattrel
Electric · Flying
Nacli
#0932
Nacli
Rock
(Level 24)
Naclstack
#0933
Naclstack
Rock
(Level 38)
Garganacl
#0934
Garganacl
Rock
Glimmet
#0969
Glimmet
Rock · Poison
(Level 35)
Glimmora
#0970
Glimmora
Rock · Poison
Shroodle
#0944
Shroodle
Poison · Normal
(Level 28)
Grafaiai
#0945
Grafaiai
Poison · Normal
Fidough
#0926
Fidough
Fairy
(Level 26)
Dachsbun
#0927
Dachsbun
Fairy
Maschiff
#0942
Maschiff
Dark
(Level 30)
Mabosstiff
#0943
Mabosstiff
Dark
Bramblin
#0946
Bramblin
Grass · Ghost
(walk 1,000 steps in Let's Go mode)
Brambleghast
#0947
Brambleghast
Grass · Ghost
Gimmighoul (Chest Form)
#0999
Gimmighoul
Chest Form
Ghost
(collect 999 Coins from Roaming Form)
Gholdengo
#1000
Gholdengo
Steel · Ghost
Tinkatink
#0957
Tinkatink
Fairy · Steel
(Level 24)
Tinkatuff
#0958
Tinkatuff
Fairy · Steel
(Level 38)
Tinkaton
#0959
Tinkaton
Fairy · Steel
Charcadet
#0935
Charcadet
Fire
(use Auspicious Armor)
Armarouge
#0936
Armarouge
Fire · Psychic
(use Malicious Armor)
Ceruledge
#0937
Ceruledge
Fire · Ghost
Toedscool
#0948
Toedscool
Ground · Grass
(Level 30)
Toedscruel
#0949
Toedscruel
Ground · Grass
    """
    text = re.sub("\n#.*\n.*\n.*", "", text)
    print(len(text))
    text = re.sub("Generation.*\n","",text)
    text = re.sub(" \(Hisuian .*","", text)
    temp = []
    lista = text.split('\n')
    for i, line in enumerate(lista):
        if i+2 < len(lista) and "(Level " in lista[i+1]:
            if lista[i+1][8] == ')':
                temp.append([line, lista[i + 1][7:8], lista[i + 2]])
            else:
                temp.append([line,lista[i+1][7:9],lista[i+2]])
    #print(len(text),text)
    for t in temp:
        print(t)
    counter = 0
    for evo in temp:
        if len(PokemonSpecies.objects.filter(name=evo[0].capitalize().strip())) == 0:
            continue
        if len(PokemonSpecies.objects.filter(name=evo[2].capitalize().strip())) == 0:
            continue
        if not evo[1].isnumeric():
            continue
        if PokemonSpecies.objects.get(name=evo[2].capitalize().strip()) in PokemonSpecies.objects.get(name=evo[0].capitalize().strip()).evolve_species.all():
            continue
        pok = PokemonSpecies.objects.get(name=evo[0].capitalize().strip())
        pok.if_evolve_by_level_up = True
        pok.evolve_level = int(evo[1])
        pok.evolve_species.add(PokemonSpecies.objects.get(name=evo[2].capitalize().strip()))
        pok.save()

        counter+=1
    print(counter)
