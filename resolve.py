def ResolvePokemon(cell):
    pokemon = (cell, 0)

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

    pokemon = speciesReplacement.get(cell, pokemon)

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

    # Handle Megas
    megas = {
        "Charizard-M-X" : ("Charizard", 1),
        "Charizard-M-Y" : ("Charizard", 2),
        "Mewtwo-M-X" : ("Mewtwo", 1),
        "Mewtwo-M-Y" : ("Mewtwo", 2),
    }

    if pokemon[0].endswith("-M") and pokemon[0] != "Unown":
        return (pokemon[0][:-2], 1)
    
    pokemon = megas.get(pokemon[0], pokemon)
    
    # Handle Primals
    if pokemon[0].endswith("-P"):
        return (pokemon[0], 1)

    return forms.get(pokemon[0], pokemon)

# Unsupported Forms (for now)

#  SPECIES_VIVILLON_POLAR (SPECIES_MISC_FORM_START + 45)
#  SPECIES_VIVILLON_TUNDRA (SPECIES_MISC_FORM_START + 46)
#  SPECIES_VIVILLON_CONTINENTAL (SPECIES_MISC_FORM_START + 47)
#  SPECIES_VIVILLON_GARDEN (SPECIES_MISC_FORM_START + 48)
#  SPECIES_VIVILLON_ELEGANT (SPECIES_MISC_FORM_START + 49)
#  SPECIES_VIVILLON_MEADOW (SPECIES_MISC_FORM_START + 50)
#  SPECIES_VIVILLON_MODERN (SPECIES_MISC_FORM_START + 51)
#  SPECIES_VIVILLON_MARINE (SPECIES_MISC_FORM_START + 52)
#  SPECIES_VIVILLON_ARCHIPELAGO (SPECIES_MISC_FORM_START + 53)
#  SPECIES_VIVILLON_HIGH_PLAINS (SPECIES_MISC_FORM_START + 54)
#  SPECIES_VIVILLON_SANDSTORM (SPECIES_MISC_FORM_START + 55)
#  SPECIES_VIVILLON_RIVER (SPECIES_MISC_FORM_START + 56)
#  SPECIES_VIVILLON_MONSOON (SPECIES_MISC_FORM_START + 57)
#  SPECIES_VIVILLON_SAVANNA (SPECIES_MISC_FORM_START + 58)
#  SPECIES_VIVILLON_SUN (SPECIES_MISC_FORM_START + 59)
#  SPECIES_VIVILLON_OCEAN (SPECIES_MISC_FORM_START + 60)
#  SPECIES_VIVILLON_JUNGLE (SPECIES_MISC_FORM_START + 61)
#  SPECIES_VIVILLON_FANCY (SPECIES_MISC_FORM_START + 62)
#  SPECIES_VIVILLON_POKE_BALL (SPECIES_MISC_FORM_START + 63)

#  SPECIES_FLABEBE_YELLOW_FLOWER (SPECIES_MISC_FORM_START + 64)
#  SPECIES_FLABEBE_ORANGE_FLOWER (SPECIES_MISC_FORM_START + 65)
#  SPECIES_FLABEBE_BLUE_FLOWER (SPECIES_MISC_FORM_START + 66)
#  SPECIES_FLABEBE_WHITE_FLOWER (SPECIES_MISC_FORM_START + 67)

#  SPECIES_FLOETTE_YELLOW_FLOWER (SPECIES_MISC_FORM_START + 68)
#  SPECIES_FLOETTE_ORANGE_FLOWER (SPECIES_MISC_FORM_START + 69)
#  SPECIES_FLOETTE_BLUE_FLOWER (SPECIES_MISC_FORM_START + 70)
#  SPECIES_FLOETTE_WHITE_FLOWER (SPECIES_MISC_FORM_START + 71)
#  SPECIES_FLOETTE_ETERNAL_FLOWER (SPECIES_MISC_FORM_START + 72)

#  SPECIES_FLORGES_YELLOW_FLOWER (SPECIES_MISC_FORM_START + 73)
#  SPECIES_FLORGES_ORANGE_FLOWER (SPECIES_MISC_FORM_START + 74)
#  SPECIES_FLORGES_BLUE_FLOWER (SPECIES_MISC_FORM_START + 75)
#  SPECIES_FLORGES_WHITE_FLOWER (SPECIES_MISC_FORM_START + 76)

#  SPECIES_MINIOR_METEOR_ORANGE (SPECIES_MISC_FORM_START + 107)
#  SPECIES_MINIOR_METEOR_YELLOW (SPECIES_MISC_FORM_START + 108)
#  SPECIES_MINIOR_METEOR_GREEN (SPECIES_MISC_FORM_START + 109)
#  SPECIES_MINIOR_METEOR_BLUE (SPECIES_MISC_FORM_START + 110)
#  SPECIES_MINIOR_METEOR_INDIGO (SPECIES_MISC_FORM_START + 111)
#  SPECIES_MINIOR_METEOR_VIOLET (SPECIES_MISC_FORM_START + 112)
#  SPECIES_MINIOR_CORE_RED (SPECIES_MISC_FORM_START + 113)
#  SPECIES_MINIOR_CORE_ORANGE (SPECIES_MISC_FORM_START + 114)
#  SPECIES_MINIOR_CORE_YELLOW (SPECIES_MISC_FORM_START + 115)
#  SPECIES_MINIOR_CORE_GREEN (SPECIES_MISC_FORM_START + 116)
#  SPECIES_MINIOR_CORE_BLUE (SPECIES_MISC_FORM_START + 117)
#  SPECIES_MINIOR_CORE_INDIGO (SPECIES_MISC_FORM_START + 118)
#  SPECIES_MINIOR_CORE_VIOLET (SPECIES_MISC_FORM_START + 119)

#  SPECIES_ALCREMIE_BERRY_SWEET (SPECIES_MISC_FORM_START + 133)
#  SPECIES_ALCREMIE_LOVE_SWEET (SPECIES_MISC_FORM_START + 134)
#  SPECIES_ALCREMIE_STAR_SWEET (SPECIES_MISC_FORM_START + 135)
#  SPECIES_ALCREMIE_CLOVER_SWEET (SPECIES_MISC_FORM_START + 136)
#  SPECIES_ALCREMIE_FLOWER_SWEET (SPECIES_MISC_FORM_START + 137)
#  SPECIES_ALCREMIE_RIBBON_SWEET (SPECIES_MISC_FORM_START + 138)
#  SPECIES_ALCREMIE_FILLER_1 (SPECIES_MISC_FORM_START + 139)
#  SPECIES_ALCREMIE_FILLER_2 (SPECIES_MISC_FORM_START + 140)

def ResolveMove(move):
    movesReplacement = {
        "Vise Grip" : "Vice Grip",
        "Forest’s Curse" : "Forests Curse",
        "King’s Shield" : "Kings Shield",
        "Land’s Wrath" : "Lands Wrath",
    }

    move = movesReplacement.get(move, move)

    return "MOVE_"+move.upper().replace(" ", "_").replace('-','_')
    
def ResolveAbility(ability):
    abilitiesReplacement = {
        "Dragon’s Maw" : "Dragons Maw",
        "As One (Glastrier)" : "As One Glastrier",
        "As One (Spectrier)" : "As On Spectrier",
    }

    ability = abilitiesReplacement.get(ability, ability).replace('-','_')

    return "ABILITY_"+ability.upper().replace(" ", "_")

def ResolveItem(item):
    itemsReplacement = {
        "King’s Rock" : "Kings Rock",
    }

    item = itemsReplacement.get(item, item).replace('-','_')

    return "ITEM_"+item.upper().replace(" ", "_")

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

def ResolveStatus(status):
    statusReplacement = {
        "Poisoned": "Poison",
        "Burned": "Burn",
        "Paralyzed": "Paralysis",
        "Frozen": "Freeze",
        "Asleep": "Sleep",
    }

    status = statusReplacement.get(status, status)

    return "CONDITION_"+status.upper().replace(" ", "_")

def ResolveTypes(types):
    typesReplacement = {

    }

    types[0] = typesReplacement.get(types[0], types[0]).upper()
    types[1] = typesReplacement.get(types[1], types[1]).upper()

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
    while len(nickname_parts) < 12:
        nickname_parts.append("0")

    return "nickname " + ", ".join(nickname_parts)

def ResolveItemForm(pokemon, item):

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

    if megaStones.get(pokemon) == item:
        temp_list = list(pokemon)
        temp_list[1] = 0
        pokemon = tuple(temp_list)

    return pokemon, item