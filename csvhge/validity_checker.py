from typing import List, Tuple, Set
from common.trainer import TrainerData, TrainerMon
from common.header_parser import abilityDefines, itemDefines, moveDefines, pokemonDefines, speciesDefines, trainerClassDefines, trainerMonTypeDefines, trainerAdditionalFlagsDefines, natureDefines

def CheckTrainerValidity(trainer):
    global abilityDefines
    global itemDefines
    global moveDefines
    global pokemonDefines
    global speciesDefines
    global trainerClassDefines
    global trainerMonTypeDefines
    global trainerAdditionalFlagsDefines
    global natureDefines

    if not(CheckTrainerParamValidity(trainer.trainermontype, trainerMonTypeDefines)
    and CheckTrainerParamValidity(trainer.trainerclass, trainerClassDefines)
    and CheckTrainerParamValidity(trainer.item, itemDefines)
    ):
        return False

    for mon in trainer.party:
        if not(CheckTrainerParamValidity(mon.pokemon[0], speciesDefines)
        and CheckTrainerParamValidity(mon.item, itemDefines)
        and CheckTrainerParamValidity(mon.move, moveDefines)
        and CheckTrainerParamValidity(mon.ability, abilityDefines)
        and CheckTrainerParamValidity(mon.ball, itemDefines)
        and CheckTrainerParamValidity(mon.nature, natureDefines)
        and CheckTrainerParamValidity(mon.additionalFlags, trainerAdditionalFlagsDefines)
        ):
            return False
        
    return True

def CheckTrainerParamValidity(param, defines):
    if isinstance(param, list) or isinstance(param, set) or isinstance(param, tuple) or isinstance(param, List):
        for obj in param:
            if obj not in defines:
                print(f"Unknown value : {obj}")
                return False
    elif param not in defines:
        print(f"Unknown value : {param}")
        return False
    return True