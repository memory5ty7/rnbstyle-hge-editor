import re

speciesReplacement = {
    "Nidoran♂" : ("Nidoran M", 0),
    "Nidoran♀" : ("Nidoran F", 0),
    "Ho-oh" : ("Ho Oh", 0),
    "Farfetch'd" : ("Farfetchd", 0),
    "Mr. Mime" : ("Mr Mime", 0),
    "Mime Jr." : ("Mime Jr", 0),
    "Porygon-Z" : ("Porygon Z", 0),
    "Flabébé" : ("Flabebe", 0),
    "Type: Null" : ("Type Null", 0),
    "Jangmo-o" : ("Jangmo O", 0),
    "Hakamo-o" : ("Hakamo O", 0),
    "Kommo-o" : ("Kommo O", 0),
    "Sirfetch'd" : ("Sirfetchd", 0),
    "Mr. Rime" : ("Mr Rime", 0),
    "Wo-Chien" : ("Wo Chien", 0),
    "Chien-Pao" : ("Chien Pao", 0),
    "Ting-Lu" : ("Ting Lu", 0),
    "Chi-Yu" : ("Chi Yu", 0),
}

forms = {
    "Pikachu-Cosplay" : ("Pikachu", 1),
    "Pikachu-Rockstar" : ("Pikachu", 2),
    "Pikachu-Belle" : ("Pikachu", 3),
    "Pikachu-Popstar" : ("Pikachu", 4),
    "Pikachu-PhD" : ("Pikachu", 5),
    "Pikachu-Libre" : ("Pikachu", 6),
    "Pikachu-Original" : ("Pikachu", 7),
    "Pikachu-Hoenn" : ("Pikachu", 8),
    "Pikachu-Sinnoh" : ("Pikachu", 9),
    "Pikachu-Unova" : ("Pikachu", 10),
    "Pikachu-Kalos" : ("Pikachu", 11),
    "Pikachu-Alola" : ("Pikachu", 12),
    "Pikachu-Partner" : ("Pikachu", 13),
    "Pikachu-World" : ("Pikachu", 14),
    "Pikachu-Partner" : ("Pikachu", 15),

    "Castform-Sunny" : ("Castform", 1),
    "Castform-Rainy" : ("Castform", 2),
    "Castform-Snowy" : ("Castform", 3),

    "Deoxys-A" : ("Deoxys", 1),
    "Deoxys-D" : ("Deoxys", 2),
    "Deoxys-S" : ("Deoxys", 3),
    "Wormadam-Sandy" : ("Wormadam", 1),
    "Wormadam-Trash" : ("Wormadam", 2),
    "Rotom-Heat" : ("Rotom", 1),
    "Rotom-Wash" : ("Rotom", 2),
    "Rotom-Frost" : ("Rotom", 3),
    "Rotom-Fan" : ("Rotom", 4),
    "Rotom-Mow" : ("Rotom", 5),
    "Giratina-O" : ("Giratina", 1),
    "Shaymin-S" : ("Shaymin", 1),

    "Shellos-E" : ("Shellos", 1),
    "Gastrodon-E" : ("Gastrodon", 1),
    "Cherrim-Sunshine" : ("Cherrim", 1),

    "Dialga-O" : ("Dialga", 1),
    "Palkia-O" : ("Palkia", 1),

    "Deerling-Summer" : ("Deerling", 1),
    "Deerling-Autumn" : ("Deerling", 2),
    "Deerling-Winter" : ("Deerling", 3),
    "Sawsbuck-Summer" : ("Sawsbuck", 1),
    "Sawsbuck-Autumn" : ("Sawsbuck", 2),
    "Sawsbuck-Winter" : ("Sawsbuck", 3),
    "Tornadus-T" : ("Tornadus", 1),
    "Thundurus-T" : ("Thundurus", 1),
    "Landorus-T" : ("Landorus", 1),
    "Kyurem-W" : ("Kyurem", 1),
    "Kyurem-B" : ("Kyurem", 2),
    "Keldeo-R" : ("Keldeo", 1),
    "Meloetta-P" : ("Meloetta", 1),
    "Genesect-D" : ("Genesect", 1),
    "Genesect-S" : ("Genesect", 2),
    "Genesect-B" : ("Genesect", 3),
    "Genesect-C" : ("Genesect", 4),

    "Greninja-Ash" : ("Greninja", 2),
    "Vivillon-Polar" : ("Vivillon", 1),
    "Vivillon-Tundra" : ("Vivillon", 2),
    "Vivillon-Continental" : ("Vivillon", 3),
    "Vivillon-Garden" : ("Vivillon", 4),
    "Vivillon-Elegant" : ("Vivillon", 5),
    "Vivillon-Meadow" : ("Vivillon", 6),
    "Vivillon-Modern" : ("Vivillon", 7),
    "Vivillon-Marine" : ("Vivillon", 8),
    "Vivillon-Archipelago" : ("Vivillon", 9),
    "Vivillon-High Plains" : ("Vivillon", 10),
    "Vivillon-Sandstorm" : ("Vivillon", 11),
    "Vivillon-River" : ("Vivillon", 12),
    "Vivillon-Monsoon" : ("Vivillon", 13),
    "Vivillon-Savanna" : ("Vivillon", 14),
    "Vivillon-Sun" : ("Vivillon", 15),
    "Vivillon-Ocean" : ("Vivillon", 16),
    "Vivillon-Jungle" : ("Vivillon", 17),
    "Vivillon-Fancy" : ("Vivillon", 18),
    "Vivillon-Poké Ball" : ("Vivillon", 19),
    "Flabébé-Y" : ("Flabébé", 1),
    "Flabébé-O" : ("Flabébé", 2),
    "Flabébé-B" : ("Flabébé", 3),
    "Flabébé-W" : ("Flabébé", 4),
    "Floette-Y" : ("Floette", 1),
    "Floette-O" : ("Floette", 2),
    "Floette-B" : ("Floette", 3),
    "Floette-N" : ("Floette", 4),
    "Floette-E" : ("Floette", 5),
    "Florges-Y" : ("Florges", 1),
    "Florges-O" : ("Florges", 2),
    "Florges-B" : ("Florges", 3),
    "Florges-N" : ("Florges", 4),
    "Furfrou-Heart" : ("Furfrou", 1),
    "Furfrou-Star" : ("Furfrou", 2),
    "Furfrou-Diamond" : ("Furfrou", 3),
    "Furfrou-Debutante" : ("Furfrou", 4),
    "Furfrou-Matron" : ("Furfrou", 5),
    "Furfrou-Dandy" : ("Furfrou", 6),
    "Furfrou-La-Reine" : ("Furfrou", 7),
    "Furfrou-Kabuki" : ("Furfrou", 8),
    "Furfrou-Pharaoh" : ("Furfrou", 9),
    "Aegislash-B" : ("Aegislash", 1),
    "Pumpkaboo-Small" : ("Pumpkaboo", 1),
    "Pumpkaboo-Large" : ("Pumpkaboo", 2),
    "Pumpkaboo-Super" : ("Pumpkaboo", 3),
    "Gourgeist-Small" : ("Gourgeist", 1),
    "Gourgeist-Large" : ("Gourgeist", 2),
    "Gourgeist-Super" : ("Gourgeist", 3),
    "Zygarde-10%" : ("Zygarde", 1),
    "Zygarde-C" : ("Zygarde", 5),
    "Magearna-O" : ("Magearna", 1),
    "Hoopa-U" : ("Hoopa", 1),

    "Lycanroc-Midnight" : ("Lycanroc", 1),
    "Lycanroc-Dusk" : ("Lycanroc", 2),
    "Oricorio-P-P" : ("Oricorio", 1),
    "Oricorio-P" : ("Oricorio", 2),
    "Oricorio-S" : ("Oricorio", 3),
    "Wishiwashi-S" : ("Wishiwashi", 1),
    "Mimikyu-B" : ("Mimikyu", 1),
    "Minior-R" : ("Minior", 1),
    "Minior-O" : ("Minior", 2),
    "Minior-Y" : ("Minior", 3),
    "Minior-G" : ("Minior", 4),
    "Minior-B" : ("Minior", 5),
    "Minior-I" : ("Minior", 6),
    "Minior-V" : ("Minior", 7),
    "Minior-C-R" : ("Minior", 8),
    "Minior-C-O" : ("Minior", 9),
    "Minior-C-Y" : ("Minior", 10),
    "Minior-C-G" : ("Minior", 11),
    "Minior-C-B" : ("Minior", 12),
    "Minior-C-I" : ("Minior", 13),
    "Minior-C-V" : ("Minior", 14),
    "Necrozma-D-M" : ("Necrozma", 1),
    "Necrozma-D-W" : ("Necrozma", 2),
    "Necrozma-U" : ("Necrozma", 3),

    "Rattata-A" : ("Rattata", 1),
    "Raticate-A" : ("Raticate", 1),
    "Raichu-A" : ("Raichu", 1),
    "Sandshrew-A" : ("Sandshrew", 1),
    "Sandslash-A" : ("Sandslash", 1),
    "Vulpix-A" : ("Vulpix", 1),
    "Ninetales-A" : ("Ninetales", 1),
    "Diglett-A" : ("Diglett", 1),
    "Dugtrio-A" : ("Dugtrio", 1),
    "Meowth-A" : ("Meowth", 1),
    "Persian-A" : ("Persian", 1),
    "Geodude-A" : ("Geodude", 1),
    "Graveler-A" : ("Graveler", 1),
    "Golem-A" : ("Golem", 1),
    "Grimer-A" : ("Grimer", 1),
    "Muk-A" : ("Muk", 1),
    "Exeggutor-A" : ("Exeggutor", 1),
    "Marowak-A" : ("Marowak", 1),

    "Morpeko-H" : ("Morpeko", 1),
    "Toxtricity-L-K" : ("Toxtricity", 1),
    "Cramorant-Gulping" : ("Cramorant", 1),
    "Cramorant-Gorging" : ("Cramorant", 2),
    "Eiscue-N" : ("Eiscue", 1),
    "Zacian-C" : ("Zacian", 1),
    "Zamazenta-C" : ("Zamazenta", 1),
    "Urshifu-S-S" : ("Urshifu", 0),
    "Urshifu-R-S" : ("Urshifu", 1),
    "Zarude-D" : ("Zarude", 1),

    "Meowth-G" : ("Meowth", 2),
    "Ponyta-G" : ("Ponyta", 1),
    "Rapidash-G" : ("Rapidash", 1),
    "Slowpoke-G" : ("Slowpoke", 1),
    "Slowbro-G" : ("Slowbro", 2),
    "Farfetch'd-G" : ("Farfetch'd", 1),
    "Weezing-G" : ("Weezing", 1),
    "Mr. Mime-G" : ("Mr. Mime", 1),
    "Articuno-G" : ("Articuno", 1),
    "Zapdos-G" : ("Zapdos", 1),
    "Moltres-G" : ("Moltres", 1),
    "Slowking-G" : ("Slowking", 1),
    "Corsola-G" : ("Corsola", 1),
    "Zigzagoon-G" : ("Zigzagoon", 1),
    "Linoone-G" : ("Linoone", 1),
    "Darumaka-G" : ("Darumaka", 1),
    "Darmanitan-G" : ("Darmanitan", 1),
    "Darmanitan-Z" : ("Darmanitan", 2),
    "Darmanitan-G-Z" : ("Darmanitan", 3),
    "Yamask-G" : ("Yamask", 1),
    "Stunfisk-G" : ("Stunfisk", 1),

    "Growlithe-H" : ("Growlithe", 1),
    "Arcanine-H" : ("Arcanine", 1),
    "Voltorb-H" : ("Voltorb", 1),
    "Electrode-H" : ("Electrode", 1),
    "Typhlosion-H" : ("Typhlosion", 1),
    "Qwilfish-H" : ("Qwilfish", 1),
    "Sneasel-H" : ("Sneasel", 1),
    "Samurott-H" : ("Samurott", 1),
    "Lilligant-H" : ("Lilligant", 1),
    "Zorua-H" : ("Zorua", 1),
    "Zoroark-H" : ("Zoroark", 1),
    "Braviary-H" : ("Braviary", 1),
    "Sliggoo-H" : ("Sliggoo", 1),
    "Goodra-H" : ("Goodra", 1),
    "Avalugg-H" : ("Avalugg", 1),
    "Decidueye-H" : ("Decidueye", 1),

    "Enamorus-T" : ("Enamorus", 1),

    "Maushold-F" : ("Maushold", 1),
    "Squawkabilly-B" : ("Squawkabilly", 1),
    "Squawkabilly-Y" : ("Squawkabilly", 2),
    "Squawkabilly-W" : ("Squawkabilly", 3),
    "Palafin-H" : ("Palafin", 1),
    "Tatsugiri-Droopy" : ("Tatsugiri", 1),
    "Tatsugiri-Stretchy" : ("Tatsugiri", 2),
    "Dudunsparce-T-S" : ("Dudunsparce", 1),
    "Gimmighoul-R" : ("Gimmighoul", 1),
    "Wooper-P" : ("Wooper", 1),
    "Tauros-P-C" : ("Tauros", 1),
    "Tauros-P-B" : ("Tauros", 2),
    "Tauros-P-A" : ("Tauros", 3),
    "Oinkologne-F" : ("Oinkologne", 1),
    "Ogerpon-W" : ("Ogerpon", 1),
    "Ogerpon-H" : ("Ogerpon", 2),
    "Ogerpon-C" : ("Ogerpon", 3),
    "Ogerpon-T-T" : ("Ogerpon", 4),
    "Ogerpon-W-T" : ("Ogerpon", 5),
    "Ogerpon-H-T" : ("Ogerpon", 6),
    "Ogerpon-C-T" : ("Ogerpon", 7),
    "Ursaluna-BM" : ("Ursaluna", 1),
    "Terapagos-T" : ("Terapagos", 1),
    "Terapagos-S" : ("Terapagos", 2),

    "Calyrex-Ice" : ("Calyrex", 1),
    "Calyrex-Shadow" : ("Calyrex", 2),

    "Unfezant-F" : ("Unfezant", 1),
    "Frillish-F" : ("Frillish", 1),
    "Jellicent-F" : ("Jellicent", 1),
    "Pyroar-F" : ("Pyroar", 1),
    "Meowstic-M" : ("Meowstic", 0),
    "Meowstic-F" : ("Meowstic", 1),
    "Indeedee-F" : ("Indeedee", 1),
    "Basculegion-F" : ("Basculegion", 1),
}

# Unsupported Forms (for now)

#  SPECIES_ALCREMIE_BERRY_SWEET (SPECIES_MISC_FORM_START + 133)
#  SPECIES_ALCREMIE_LOVE_SWEET (SPECIES_MISC_FORM_START + 134)
#  SPECIES_ALCREMIE_STAR_SWEET (SPECIES_MISC_FORM_START + 135)
#  SPECIES_ALCREMIE_CLOVER_SWEET (SPECIES_MISC_FORM_START + 136)
#  SPECIES_ALCREMIE_FLOWER_SWEET (SPECIES_MISC_FORM_START + 137)
#  SPECIES_ALCREMIE_RIBBON_SWEET (SPECIES_MISC_FORM_START + 138)
#  SPECIES_ALCREMIE_FILLER_1 (SPECIES_MISC_FORM_START + 139)
#  SPECIES_ALCREMIE_FILLER_2 (SPECIES_MISC_FORM_START + 140)

megas = {
    "Charizard-M-X" : ("Charizard", 1),
    "Charizard-M-Y" : ("Charizard", 2),
    "Mewtwo-M-X" : ("Mewtwo", 1),
    "Mewtwo-M-Y" : ("Mewtwo", 2),
}

megaStones = {
    ("Venusaur", 1) : "Venusaurite",
    ("Charizard", 1) : "Charizardite Y",
    ("Charizard", 2) : "Charizardite X",
    ("Blastoise", 1) : "Blastoisinite",
    ("Beedrill", 1) : "Beedrillite",
    ("Pidgeot", 1) : "Pidgeotite",
    ("Alakazam", 1) : "Alakazite",
    ("Gengar", 1) : "Gengarite",
    ("Kangaskhan", 1) : "Kangaskhanite",
    ("Pinsir", 1) : "Pinsirite",
    ("Gyarados", 1) : "Gyaradosite",
    ("Aerodactyl", 1) : "Aerodactylite",
    ("Mewtwo", 1) : "Mewtwonite Y",
    ("Mewtwo", 2) : "Mewtwonite X",
    ("Ampharos", 1) : "Ampharosite",
    ("Steelix", 1) : "Steelixite",
    ("Scizor", 1) : "Scizorite",
    ("Heracross", 1) : "Heracronite",
    ("Houndoom", 1) : "Houndoominite",
    ("Tyranitar", 1) : "Tyranitarite",
    ("Sceptile", 1) : "Sceptilite",
    ("Blaziken", 1) : "Blazikenite",
    ("Swampert", 1) : "Swampertite",
    ("Gardevoir", 1) : "Gardevoirite",
    ("Sableye", 1) : "Sablenite",
    ("Mawile", 1) : "Mawilite",
    ("Aggron", 1) : "Aggronite",
    ("Medicham", 1) : "Medichamite",
    ("Manectric", 1) : "Manectite",
    ("Sharpedo", 1) : "Sharpedonite",
    ("Camerupt", 1) : "Cameruptite",
    ("Altaria", 1) : "Altarianite",
    ("Banette", 1) : "Banettite",
    ("Absol", 1) : "Absolite",
    ("Glalie", 1) : "Glalitite",
    ("Salamence", 1) : "Salamencite",
    ("Metagross", 1) : "Metagrossite",
    ("Latias", 1) : "Latiasite",
    ("Latios", 1) : "Latiosite",
    ("Lopunny", 1) : "Lopunnite",
    ("Garchomp", 1) : "Garchompite",
    ("Lucario", 1) : "Lucarionite",
    ("Abomasnow", 1) : "Abomasite",
    ("Gallade", 1) : "Galladite",
    ("Audino", 1) : "Audinite",
    ("Diancie", 1) : "Diancite",
}

def ResolvePokemon(cell):
    pokemon = (cell, 0)

    pokemon = speciesReplacement.get(cell, pokemon)

    if pokemon[0].endswith("-M") and pokemon[0] != "Unown":
        return (pokemon[0][:-2], 1)
    
    # Handle Megas
    pokemon = megas.get(pokemon[0], pokemon)
    
    # Handle Primals
    if pokemon[0].endswith("-P"):
        return (pokemon[0], 1)

    return forms.get(pokemon[0], pokemon)

def ResolvePokemonToCSV(mon, item, shinylock):

    species = mon.pokemon[0].replace("SPECIES_","").replace("_"," ").title()
    form = mon.pokemon[1]

    species = next((k for k, v in speciesReplacement.items() if v == (species, form)), species)
    if species == "None":
        return ""
      
    species = next((k for k, v in forms.items() if v == (species, int(form))), species)

    
    if any(s == species and v == item for (s, f), v in megaStones.items()):
        species += "-M"

    if shinylock:
        species += '*'

    return species

movesReplacement = {
    "Vise Grip" : "Vice Grip",
    "Forest’s Curse" : "Forests Curse",
    "King’s Shield" : "Kings Shield",
    "Land’s Wrath" : "Lands Wrath",
}
    
def ResolveMove(move):

    if(move == "MOVE_NONE"):
        return move

    move = movesReplacement.get(move, move)

    return "MOVE_"+move.upper().replace(" ", "_").replace('-','_')

def ResolveMoveToCSV(move):
    move = move.replace("MOVE_","").replace("_"," ").title()

    move = next((k for k, v in movesReplacement.items() if v == move), move)

    if move == "None":
        return "-"

    return move

abilitiesReplacement = {
    "Dragon’s Maw" : "Dragons Maw",
    "As One (Glastrier)" : "As One Glastrier",
    "As One (Spectrier)" : "As One Spectrier",
}

def ResolveAbility(ability):
    ability = abilitiesReplacement.get(ability, ability).replace('-','_')

    return "ABILITY_"+ability.upper().replace(" ", "_")

def ResolveAbilityToCSV(ability):

    return ability.replace("ABILITY_","").replace("_"," ").title()

itemsReplacement = {
    "King’s Rock" : "Kings Rock",
    "Poké Ball" : "Poke Ball"
}

def ResolveItem(item):

    item = itemsReplacement.get(item, item).replace('-','_')

    return "ITEM_"+item.upper().replace(" ", "_")

def ResolveItemToCSV(item):

    item = item.replace("ITEM_","").replace("_"," ").title()

    item = next((k for k, v in itemsReplacement.items() if v == item), item)

    if item == "None":
        return ""

    return item

def ResolveBall(ball):
    ballsReplacement = {

    }

    ball = ballsReplacement.get(ball, ball)

    return ball.upper().replace(" ", "_")

def ResolveNature(nature):
    naturesReplacement = {

    }

    nature = naturesReplacement.get(nature, nature)

    return "NATURE_"+nature.upper().replace(" ", "_")

def ResolveNatureToCSV(nature):

    return nature.replace("NATURE_","").title()

statusReplacement = {
    "Poisoned": 0x8,
    "Badly Poisoned": 0x80,
    "Burned": 0x10,
    "Paralyzed": 0x40,
    "Frozen": 0x20,
    "Asleep": 0x1,
    "Asleep (1 Turn)": 0x1,
    "Asleep (2 Turns)": 0x2,
    "Asleep (3 Turns)": 0x3,
    "Asleep (4 Turns)": 0x4,
    "Asleep (5 Turns)": 0x5,
    "Asleep (6 Turns)": 0x6,
    "Asleep (7 Turns)": 0x7,
}

def ResolveStatus(status):
    status = statusReplacement.get(status)

    return status

def ResolveStatusToCSV(status):
    
    status = int(str(status), 16)

    status = next((k for k, v in statusReplacement.items() if v == (status)), status)

    return status

def ResolveTypes(cell):
    typesReplacement = {

    }

    type1 = typesReplacement.get(cell[0], "TYPE_"+cell[0].upper())
    type2 = typesReplacement.get(cell[1], "TYPE_"+cell[1].upper())

    types= (type1, type2)

    return types

def ResolveNickname(nickname: str) -> str:
    nickname_parts = []

    for char in nickname:
        if char.isupper():
            nickname_parts.append(f"_{char}")
        elif char.islower():
            nickname_parts.append(f"_{char}_")
        else:
            raise ValueError(f"Unsupported character in nickname: {char}")

    # Pad to 12 fields (nickname + _endstr + 0 padding)
    nickname_parts.append("_endstr")
    while len(nickname_parts) < 11:
        nickname_parts.append("0")

    return ", ".join(nickname_parts)

def ResolveItemForm(pokemon, item):

    if megaStones.get(pokemon) == item:
        temp_list = list(pokemon)
        temp_list[1] = 0
        pokemon = tuple(temp_list)

    return pokemon, item

specialTrainerClasses = {
    "Ethan" : "TRAINERCLASS_PKMN_TRAINER_ETHAN",
    "Lyra" : "TRAINERCLASS_PKMN_TRAINER_LYRA",
    "Falkner" : "TRAINERCLASS_LEADER_FALKNER",
    "Bugsy" : "TRAINERCLASS_LEADER_BUGSY",
    "Whitney" : "TRAINERCLASS_LEADER_WHITNEY",
    "Morty" : "TRAINERCLASS_LEADER_MORTY",
    "Pryce" : "TRAINERCLASS_LEADER_PRYCE",
    "Jasmine" : "TRAINERCLASS_LEADER_JASMINE",
    "Chuck" : "TRAINERCLASS_LEADER_CHUCK",
    "Clair" : "TRAINERCLASS_LEADER_CLAIR",
    "Lance" : "TRAINERCLASS_CHAMPION",
    "Will" : "TRAINERCLASS_ELITE_FOUR_WILL",
    "Karen" : "TRAINERCLASS_ELITE_FOUR_KAREN",
    "Koga" : "TRAINERCLASS_ELITE_FOUR_KOGA",
    "Cheryl (Partner)" : "TRAINERCLASS_PKMN_TRAINER_CHERYL",
    "Riley (Partner)" : "TRAINERCLASS_PKMN_TRAINER_RILEY",
    "Buck (Partner)" : "TRAINERCLASS_PKMN_TRAINER_BUCK",
    "Mira (Partner)" : "TRAINERCLASS_PKMN_TRAINER_MIRA",
    "Marley (Partner)" : "TRAINERCLASS_PKMN_TRAINER_MARLEY",
    "Lucas" : "TRAINERCLASS_PKMN_TRAINER_FTR_LUCAS",
    "Dawn" : "TRAINERCLASS_PKMN_TRAINER_FTR_DAWN",
    "Palmer" : "TRAINERCLASS_TOWER_TYCOON",
    "Brock" : "TRAINERCLASS_LEADER_BROCK",
    "Argenta" : "TRAINERCLASS_HALL_MATRON",
    "Thorton" : "TRAINERCLASS_FACTORY_HEAD",
    "Dahlia" : "TRAINERCLASS_ARCADE_STAR",
    "Darach" : "TRAINERCLASS_CASTLE_VALET",
    "Misty" : "TRAINERCLASS_LEADER_MISTY",
    "Lt. Surge" : "TRAINERCLASS_LEADER_LT_SURGE",
    "Erika" : "TRAINERCLASS_LEADER_ERIKA",
    "Janine" : "TRAINERCLASS_LEADER_JANINE",
    "Sabrina" : "TRAINERCLASS_LEADER_SABRINA",
    "Blaine" : "TRAINERCLASS_LEADER_BLAINE",
    "Red" : "TRAINERCLASS_PKMN_TRAINER_RED",
    "Blue" : "TRAINERCLASS_LEADER_BLUE",
    "Bruno" : "TRAINERCLASS_ELITE_FOUR_BRUNO",
    "Ariana" : "TRAINERCLASS_EXECUTIVE_ARIANA",
    "Archer" : "TRAINERCLASS_EXECUTIVE_ARCHER",
    "Proton" : "TRAINERCLASS_EXECUTIVE_PROTON",
    "Petrel" : "TRAINERCLASS_EXECUTIVE_PETREL",
    "Lance (Partner)" : "TRAINERCLASS_PKMN_TRAINER_LANCE",
    "Giovanni" : "TRAINERCLASS_ROCKET_BOSS",
    "Lucas DP" : "TRAINERCLASS_PKMN_TRAINER_LUCAS_DP",
    "Dawn DP" : "TRAINERCLASS_PKMN_TRAINER_DAWN_DP",
    "Lucas PT" : "TRAINERCLASS_PKMN_TRAINER_LUCAS_PT",
    "Dawn PT" : "TRAINERCLASS_PKMN_TRAINER_DAWN_PT",
}

regularTrainerClasses = {
    "Cyclist♂" : "TRAINERCLASS_CYCLIST_M",
    "Cyclist♀" : "TRAINERCLASS_CYCLIST_F",
    "Breeder♂" : "TRAINERCLASS_PKMN_BREEDER_M",
    "Breeder♀" : "TRAINERCLASS_PKMN_BREEDER_F", 
    "Pokéfan♂" : "TRAINERCLASS_POKEFAN_M",
    "Pokéfan♀" : "TRAINERCLASS_POKEFAN",
    "Poké Kid" : "TRAINERCLASS_POKE_KID",
    "Ace Trainer♂" : "TRAINERCLASS_ACE_TRAINER_M",
    "Ace Trainer♀" : "TRAINERCLASS_ACE_TRAINER_F",
    "Bird Keeper DPPT" : "TRAINERCLASS_BIRD_KEEPER",
    "Ranger♂" : "TRAINERCLASS_PKMN_RANGER_M",
    "Ranger♀" : "TRAINERCLASS_PKMN_RANGER_F",
    "Scientist DPPT" : "TRAINERCLASS_SCIENTIST",
    "Swimmer♂" : "TRAINERCLASS_SWIMMER_M",
    "Swimmer♀" : "TRAINERCLASS_SWIMMER_F",
    "Tuber♂" : "TRAINERCLASS_TUBER_M",
    "Tuber♀" : "TRAINERCLASS_TUBER_F",
    "Psychic♂" : "TRAINERCLASS_PSYCHIC_M",
    "Psychic♀" : "TRAINERCLASS_PSYCHIC_F",
    "Ace Trainer DPPT♂" : "TRAINERCLASS_ACE_TRAINER_M_GS",
    "Ace Trainer DPPT♀" : "TRAINERCLASS_ACE_TRAINER_F_GS",
    "Rocket Grunt♂" : "TRAINERCLASS_TEAM_ROCKET",
    "School Kid♂" : "TRAINERCLASS_SCHOOL_KID_M",
    "School Kid♀" : "TRAINERCLASS_SCHOOL_KID_F",
    "Rocket Grunt♀" : "TRAINERCLASS_TEAM_ROCKET_F",
    "Poké Maniac" : "TRAINERCLASS_POKE_MANIAC",
    "Bird Keeper" : "TRAINERCLASS_BIRD_KEEPER_GS",
    "Scientist" : "TRAINERCLASS_SCIENTIST_GS",
}

trainerClassesToCSV = {
    "Cyclist M" : "Cyclist♂",
    "Cyclist F" : "Cyclist♀",
    "Pkmn Breeder M" : "Breeder♂",
    "Pkmn Breeder F" : "Breeder♀",
    "Pokefan M" : "Pokéfan♂",
    "Pokefan" : "Pokéfan♀",
    "Poke Kid" : "Poké Kid",
    "Ace Trainer M" : "Ace Trainer♂",
    "Ace Trainer F" : "Ace Trainer♀",
    "Bird Keeper" : "Bird Keeper DPPT",
    "Ranger M" : "Ranger♂",
    "Ranger F" : "Ranger♀",
    "Scientist" : "Scientist DPPT",
    "Swimmer M" : "Swimmer♂",
    "Swimmer F" : "Swimmer♀",
    "Tuber M" : "Tuber♂",
    "Tuber F" : "Tuber♀",
    "Psychic M" : "Psychic♂",
    "Psychic F" : "Psychic♀",
    "Ace Trainer M Gs" : "Ace Trainer DPPT♂",
    "Ace Trainer F Gs" : "Ace Trainer DPPT♀",
    "Team Rocket" : "Rocket Grunt♂",
    "School Kid M" : "School Kid♂",
    "School Kid F" : "School Kid♀",
    "Team Rocket F" : "Rocket Grunt♀",
    "Poke Maniac" : "Poké Maniac",
    "Bird Keeper Gs" : "Bird Keeper",
    "Scientist Gs" : "Scientist",  
}

def ResolveTrainerClass(trclass, trname):
    
    if trname in specialTrainerClasses:
        return specialTrainerClasses[trname]

    if trclass in regularTrainerClasses:
        return regularTrainerClasses[trclass]
    
    return "TRAINERCLASS_"+trclass.upper().replace(' ', '_')

def ResolveTrainerClassToCSV(trclass, trname):
    trclass = trclass.replace("TRAINERCLASS_","").replace("_"," ").title()

    if trclass.startswith("Pkmn Trainer"):
        return "Trainer"
    
    if trclass.startswith("Leader"):
        return "Leader"
    
    if trclass.startswith("Elite Four"):
        return "Elite Four"
        
    if trclass.startswith("Executive"):
        return "Executive"

    trclass = trainerClassesToCSV.get(trclass, trclass)

    return trclass

def ResolvePPCount(cell):

    ppcount = 0

    match = re.search(r"^(.*) - (\d+)$", cell)
    if match:
        move = match.group(1) 
        ppcount = int(match.group(2))
    else:
        move = cell

    return move, ppcount