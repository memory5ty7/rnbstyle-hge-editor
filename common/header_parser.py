import re
from config import Config

abilityDefines = []
itemDefines = []
moveDefines = []
pokemonDefines  = []
speciesDefines = []
trainerMonTypeDefines = []
trainerClassDefines = []
trainerAdditionalFlagsDefines = []
natureDefines = []

def init_defines():
    global abilityDefines
    global itemDefines
    global moveDefines
    global pokemonDefines
    global speciesDefines
    global trainerClassDefines
    global trainerMonTypeDefines
    global trainerAdditionalFlagsDefines
    global natureDefines

    abilityData = extract_defines(Config.ABILITY_HEADER)
    itemData = extract_defines(Config.ITEM_HEADER)
    moveData = extract_defines(Config.MOVE_HEADER)
    pokemonData = extract_defines(Config.POKEMON_HEADER)
    speciesData = extract_defines(Config.SPECIES_HEADER)
    trainerData = extract_defines(Config.TRAINERCLASS_HEADER)

    abilityDefines = return_defines(abilityData, "ABILITY_")
    itemDefines = return_defines(itemData, "ITEM_")
    moveDefines = return_defines(moveData, "MOVE_")
    natureDefines = return_defines(pokemonData, "NATURE_")
    speciesDefines = return_defines(speciesData, "SPECIES_")
    trainerMonTypeDefines = return_defines(pokemonData, "TRAINER_DATA_TYPE_")
    trainerAdditionalFlagsDefines = return_defines(pokemonData, "TRAINER_DATA_EXTRA_TYPE_")
    trainerClassDefines = return_defines(trainerData, "TRAINERCLASS_")

def return_defines(data, prefix):
    return [d for d in data if d.startswith(prefix)]

def extract_defines(header_path):
    defines = []
    with open(header_path, 'r', encoding='utf-8') as f:
        for line in f:
            match = re.match(r"#define\s+(\w+)\s+.+", line)
            if match:
                name = match.group(1)
                defines.append(name)
    return defines

init_defines()