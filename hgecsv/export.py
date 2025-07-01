import csv
import io
from typing import List
from common.trainer import TrainerData, TrainerMon
from common.resolve import ResolvePokemonToCSV, ResolveItemToCSV, ResolveAbilityToCSV, ResolveNatureToCSV, ResolveStatusToCSV, ResolveMoveToCSV, ResolveTrainerClassToCSV
from config import Config

def print_data(data: List[TrainerData], output_file: str):
    for trainer in data:
        output_file.write(trainerdata_to_csv(trainer))

def getRow(label, trainer):
    return (str(label), [
            get_or_dash([mon.level for mon in trainer.party], i) if i < trainer.nummons else ""
            for i in range(len(trainer.party))
        ]),

labelsFlags = {
    "Ability" : "TRAINER_DATA_TYPE_ABILITY",
    "Held Item" : "TRAINER_DATA_TYPE_ITEMS",
    "Ball" : "TRAINER_DATA_TYPE_BALL",
    "IVs" : "TRAINER_DATA_TYPE_IV_EV_SET",
    "EVs" : "TRAINER_DATA_TYPE_IV_EV_SET",
    "Nature" : "TRAINER_DATA_TYPE_NATURE_SET",
    "Ball Type" : "TRAINER_DATA_TYPE_BALL"
}

labelsAdditionalFlags = {
    "Status" : "TRAINER_DATA_EXTRA_TYPE_STATUS",
    "Stats" : "TRAINER_DATA_EXTRA_TYPE_HP",
    "Nickname" : "TRAINER_DATA_EXTRA_TYPE_NICKNAME",
}

labelsFlagsExclude = {
    "DV" : "TRAINER_DATA_TYPE_IV_EV_SET",
    "Ability Slot" : "TRAINER_DATA_TYPE_ABILITY",
}

def trainerdata_to_csv(trainer: TrainerData) -> str:

    output = io.StringIO()
    writer = csv.writer(output)

    if trainer.battletype == "DOUBLE_BATTLE":
        writer.writerow(["Name - " + str(trainer.id), ResolveTrainerClassToCSV(trainer.trainerclass, trainer.name) + " " + trainer.name+" [Double]"])
    else:
        writer.writerow(["Name - " + str(trainer.id), ResolveTrainerClassToCSV(trainer.trainerclass, trainer.name) + " " + trainer.name])

    writer.writerow(["Pokémon"]+[""]*6)
    writer.writerow([""] + [

        ResolvePokemonToCSV(mon, ResolveItemToCSV(mon.item), mon.shinylock)
        for mon in trainer.party
        ])
    
    rows = [
        ("Level", [
            get_or_dash([mon.level for mon in trainer.party], i) if i < trainer.nummons else ""
            for i in range(len(trainer.party))
        ]),
        ("DV", [
            get_or_dash([mon.dv for mon in trainer.party], i) if i < trainer.nummons else ""
            for i in range(len(trainer.party))
        ]),
        ("Ability Slot", [
            get_or_dash([mon.abilityslot for mon in trainer.party], i) if i < trainer.nummons else ""
            for i in range(len(trainer.party))
        ]),
        ("Held Item", [
            get_or_dash([ResolveItemToCSV(mon.item) for mon in trainer.party], i) if i < trainer.nummons else ""
            for i in range(len(trainer.party))
        ]),
        ("Ability", [
            get_or_dash([ResolveAbilityToCSV(mon.ability) for mon in trainer.party], i) if i < trainer.nummons else ""
            for i in range(len(trainer.party))
        ]),
        ("Nature", [
            get_or_dash([ResolveNatureToCSV(mon.nature) for mon in trainer.party], i) if i < trainer.nummons else ""
            for i in range(len(trainer.party))
        ]),
        ("IVs", [
            get_or_dash([",".join(str(ev) for ev in mon.setevs) for mon in trainer.party], i) if i < trainer.nummons else ""
            for i in range(len(trainer.party))
        ]),
        ("EVs", [
            get_or_dash([",".join(str(ev) for ev in mon.setevs) for mon in trainer.party], i) if i < trainer.nummons else ""
            for i in range(len(trainer.party))
        ]),
        ("Status", [
            get_or_dash([ResolveStatusToCSV(mon.status) for mon in trainer.party], i) if i < trainer.nummons else ""
            for i in range(len(trainer.party))
        ]),
        ("Stats", [
            get_or_dash([",".join(str(stat) for stat in mon.stats) for mon in trainer.party], i) if i < trainer.nummons else ""
            for i in range(len(trainer.party))
        ]),
        ("Ball Type", [
            get_or_dash([ResolveItemToCSV(mon.ball) for mon in trainer.party], i) if i < trainer.nummons else ""
            for i in range(len(trainer.party))
        ]),
        ("Ball Seal", [
            get_or_dash([mon.ballseal for mon in trainer.party], i) if i < trainer.nummons else ""
            for i in range(len(trainer.party))
        ])
        # ("Nickname", [
        #     get_or_dash([mon.ballseal for mon in trainer.party], i) if i < trainer.nummons else ""
        #     for i in range(len(trainer.party))
        # ]),
    ]

    for label, values in rows:
        if label in labelsFlags and labelsFlags[label] not in trainer.trainermontype:
            continue

        if label in labelsFlagsExclude.keys() and labelsFlagsExclude[label] in trainer.trainermontype:
            continue

        if label in labelsAdditionalFlags:
            if not any(labelsAdditionalFlags[label] in mon.additionalFlags for mon in trainer.party[:trainer.nummons]):
                continue

        if label == "IVs" or label == "EVs" and Config.PRINT_IVS_EVS == False:
            continue

        if label == "Ball Seal" and all(v == "0" or v == "" for v in values):
            continue


        writer.writerow([label] + values)

    if "TRAINER_DATA_TYPE_MOVES" in trainer.trainermontype:
        # Move 0
        writer.writerow(["Moves"] + [
            (ResolveMoveToCSV(mon.move[0]) +
            (f" - {mon.ppcounts[0]}" if "TRAINER_DATA_EXTRA_TYPE_PP_COUNTS" in mon.additionalFlags and mon.move[0] != "MOVE_NONE" else ""))
            if idx < trainer.nummons and len(mon.move) > 0 else ""
            for idx, mon in enumerate(trainer.party)
        ])

        # Moves 1 to 3
        for move_idx in range(1, 4):
            writer.writerow([""] + [
                (ResolveMoveToCSV(mon.move[move_idx]) +
                (f" - {mon.ppcounts[move_idx]}" if "TRAINER_DATA_EXTRA_TYPE_PP_COUNTS" in mon.additionalFlags and mon.move[move_idx] != "MOVE_NONE" else ""))
                if idx < trainer.nummons and len(mon.move) > move_idx else ""
                for idx, mon in enumerate(trainer.party)
            ])



    return output.getvalue()

def get_or_dash(attr_list: List, index: int):
    if index >= len(attr_list):
        return "-"
    v = attr_list[index]
    if isinstance(v, str) and not v:
        return "-"
    if isinstance(v, int) and v == 0:
        return "-"
    return v