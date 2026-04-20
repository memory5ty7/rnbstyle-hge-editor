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

    if not(CheckTrainerParamValidity(trainer.trainermontype, trainerMonTypeDefines, trainer.id)
    and CheckTrainerParamValidity(trainer.trainerclass, trainerClassDefines, trainer.id)
    and CheckTrainerParamValidity(trainer.item, itemDefines, trainer.id)
    ):
        return False

    for mon in trainer.party:
        if not(CheckTrainerParamValidity(mon.pokemon[0], speciesDefines, trainer.id)
        and CheckTrainerParamValidity(mon.item, itemDefines, trainer.id)
        and CheckTrainerParamValidity(mon.move, moveDefines, trainer.id)
        and CheckTrainerParamValidity(mon.ability, abilityDefines, trainer.id)
        and CheckTrainerParamValidity(mon.ball, itemDefines, trainer.id)
        and CheckTrainerParamValidity(mon.nature, natureDefines, trainer.id)
        and CheckTrainerParamValidity(mon.additionalFlags, trainerAdditionalFlagsDefines, trainer.id)
        ):
            return False
        
    return True

def CheckTrainerParamValidity(param, defines, id):
    if isinstance(param, list) or isinstance(param, set) or isinstance(param, tuple) or isinstance(param, List):
        for obj in param:
            if obj not in defines:
                print(f"Unknown value for trainer {id} : {obj}")
                return False
    elif param not in defines:
        print(f"Unknown value for trainer {id} : {param}")
        return False
    return True