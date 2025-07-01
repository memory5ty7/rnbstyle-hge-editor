from typing import List, Tuple, Set
from config import Config
from csvhge.header_parser import extract_defines
from common.trainer import TrainerData, TrainerMon

abilityDefines = []
battleDefines = []
itemDefines = []
moveDefines = []
pokemonDefines  = []
speciesDefines = []
trainerClassDefines = []

def init_defines():
    global abilityDefines
    global battleDefines
    global itemDefines
    global moveDefines
    global pokemonDefines
    global speciesDefines
    global trainerClassDefines

    abilityDefines = extract_defines(Config.ABILITY_HEADER)
    battleDefines = extract_defines(Config.BATTLE_HEADER)
    itemDefines = extract_defines(Config.ITEM_HEADER)
    moveDefines = extract_defines(Config.MOVE_HEADER)
    pokemonDefines = extract_defines(Config.POKEMON_HEADER)
    speciesDefines = extract_defines(Config.SPECIES_HEADER)
    trainerClassDefines = extract_defines(Config.TRAINERCLASS_HEADER)

def CheckTrainerValidity(trainer):
    global abilityDefines
    global battleDefines
    global itemDefines
    global moveDefines
    global pokemonDefines
    global speciesDefines
    global trainerClassDefines

    CheckTrainerParamValidity(trainer.trainermontype, pokemonDefines)
    CheckTrainerParamValidity(trainer.trainerclass, trainerClassDefines)
    CheckTrainerParamValidity(trainer.item, itemDefines)

    for mon in trainer.party:
        CheckTrainerParamValidity(mon.pokemon[0], speciesDefines)
        CheckTrainerParamValidity(mon.item, itemDefines)
        CheckTrainerParamValidity(mon.move, moveDefines)
        CheckTrainerParamValidity(mon.ability, abilityDefines)
        CheckTrainerParamValidity(mon.ball, itemDefines)
        CheckTrainerParamValidity(mon.nature, pokemonDefines)
        CheckTrainerParamValidity(mon.additionalFlags, pokemonDefines)
        # CheckTrainerParamValidity(mon.types, battleDefines)

def CheckTrainerParamValidity(param, defines):
    if isinstance(param, list) or isinstance(param, set) or isinstance(param, tuple) or isinstance(param, List):
        for obj in param:
            if obj not in defines:
                print(f"Unknown value : {obj}")
    elif param not in defines:
        print(f"Unknown value : {param}")