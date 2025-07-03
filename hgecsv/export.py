import csv
import io
from typing import List
from common.trainer import TrainerData, TrainerMon
from common.resolve import ResolvePokemonToCSV, ResolveItemToCSV, ResolveAbilityToCSV, ResolveNatureToCSV, ResolveStatusToCSV, ResolveMoveToCSV, ResolveTrainerClassToCSV
from config import Config
from .mon_parser import mons
from common.header_parser import trainerClassDefines, speciesDefines, natureDefines
from common.c_parser import trainerGenders

current_row = 0

def print_data(data: List[TrainerData], output_file: str):
    for trainer in data:
        output_file.write(trainerdata_to_csv(trainer))

labelReplaceValues = {
    "DV" : (Config.PRINT_IVS, "IVs"),
    "Ability Slot" : (Config.PRINT_ABILITY, "Ability")
}

flagDependentValues = {
    "IVs" : "TRAINER_DATA_TYPE_IV_EV_SET",
    "Ability" : "TRAINER_DATA_TYPE_ABILITY",
}

replacedValues = {
    "DV": "TRAINER_DATA_TYPE_IV_EV_SET",
    "Ability Slot" : "TRAINER_DATA_TYPE_ABILITY"
}

def trainerdata_to_csv(trainer: TrainerData) -> str:
    global current_row

    output = io.StringIO()
    writer = csv.writer(output)

    if trainer.battletype == "DOUBLE_BATTLE":
        writer.writerow(["Name - " + str(trainer.id), ResolveTrainerClassToCSV(trainer.trainerclass, trainer.name) + " " + trainer.name+" [Double]"])
    else:
        writer.writerow(["Name - " + str(trainer.id), ResolveTrainerClassToCSV(trainer.trainerclass, trainer.name) + " " + trainer.name])
    current_row += 1

    writer.writerow(
        ["Pokémon"] + 
        getMonFormula(current_row + 2, [i + 2 for i in range(6)]) + 
        getTrainerFormula(current_row, 2)
    )
    writer.writerow([""] + [

        ResolvePokemonToCSV(mon, ResolveItemToCSV(mon.item), mon.shinylock)
        for mon in trainer.party
        ])
    current_row += 2

    rows = [
        ("Level", [
            get_or_dash([mon.level for mon in trainer.party], i) if i < trainer.nummons else ""
            for i in range(len(trainer.party))
        ]),
        ("Ability Slot", [
            (
                (ResolveAbilityToCSV(mons[mon.pokemon[0]].abilities[int(int(mon.abilityslot) / 32) % 2])) if Config.PRINT_ABILITY else mon.abilityslot
            ) if i < trainer.nummons else ""
            for i in range(len(trainer.party))
            for mon in [trainer.party[i]]
        ]),
        ("Ability", [
            get_or_dash([ResolveAbilityToCSV(mon.ability) for mon in trainer.party], i) if i < trainer.nummons else ""
            for i in range(len(trainer.party))
        ]),
        ("Held Item", [
            get_or_dash([ResolveItemToCSV(mon.item) for mon in trainer.party], i) if i < trainer.nummons else ""
            for i in range(len(trainer.party))
        ]),
        ("Nature", [
            (
                ResolveNatureToCSV(mon.nature) if ("TRAINER_DATA_TYPE_NATURE_SET" in trainer.trainermontype) else ResolveNatureToCSV(calcMonNature(trainer, mon))
            ) if i < trainer.nummons else ""
            for i in range(len(trainer.party))
            for mon in [trainer.party[i]]
        ]),
        ("DV", [
            (
            (str(int(int(mon.dv) * 31 / 255))) if Config.PRINT_IVS else mon.dv
            ) if i < trainer.nummons else ""
            for i in range(len(trainer.party))
            for mon in [trainer.party[i]]
        ]),
        ("IVs", [
            get_or_dash([",".join(str(ev) for ev in mon.setevs) for mon in trainer.party], i) if i < trainer.nummons else ""
            for i in range(len(trainer.party))
        ]),
        ("EVs", [
            get_or_dash([",".join(str(ev) for ev in mon.setevs) for mon in trainer.party], i) if i < trainer.nummons else ""
            for i in range(len(trainer.party))
        ]),
        ("Stats", [
            get_or_dash([",".join(str(stat) for stat in mon.stats) for mon in trainer.party], i) if i < trainer.nummons else ""
            for i in range(len(trainer.party))
        ]),
        ("Status", [
            get_or_dash([ResolveStatusToCSV(mon.status) for mon in trainer.party], i) if i < trainer.nummons else ""
            for i in range(len(trainer.party))
        ]),
        ("Ball Type", [
            get_or_dash([ResolveItemToCSV(mon.ball) for mon in trainer.party], i) if i < trainer.nummons else ""
            for i in range(len(trainer.party))
        ]),
        ("Ball Seal", [
            get_or_dash([mon.ballseal for mon in trainer.party], i) if i < trainer.nummons else ""
            for i in range(len(trainer.party))
        ]),
        ("Nickname", [
            get_or_dash([mon.nickname for mon in trainer.party], i) if i < trainer.nummons else ""
            for i in range(len(trainer.party))
        ]),
    ]

    for label, values in rows:
        if label in replacedValues and replacedValues[label] in trainer.trainermontype:
            continue

        if label in flagDependentValues and flagDependentValues[label] not in trainer.trainermontype:
            continue

        if label in labelReplaceValues and labelReplaceValues[label][0]:
            label = labelReplaceValues[label][1]

        if label in Config.ROWS_TO_PRINT.keys() and Config.ROWS_TO_PRINT[label] == False:
           continue

        writer.writerow([label] + values)
        current_row += 1

    if "TRAINER_DATA_TYPE_MOVES" in trainer.trainermontype:
        # Move 0
        writer.writerow(["Moves"] + [
            (ResolveMoveToCSV(mon.move[0]) +
            (f" - {mon.ppcounts[0]}" if "TRAINER_DATA_EXTRA_TYPE_PP_COUNTS" in mon.additionalFlags and mon.move[0] != "MOVE_NONE" else ""))
            if idx < trainer.nummons and len(mon.move) > 0 else ""
            for idx, mon in enumerate(trainer.party)
        ])
        current_row += 1

        # Moves 1 to 3
        for move_idx in range(1, 4):
            writer.writerow([""] + [
                (ResolveMoveToCSV(mon.move[move_idx]) +
                (f" - {mon.ppcounts[move_idx]}" if "TRAINER_DATA_EXTRA_TYPE_PP_COUNTS" in mon.additionalFlags and mon.move[move_idx] != "MOVE_NONE" else ""))
                if idx < trainer.nummons and len(mon.move) > move_idx else ""
                for idx, mon in enumerate(trainer.party)
            ])
            current_row += 1
    else:
        for move_idx in range(4):
            writer.writerow(
                ["Moves" if move_idx == 0 else ""] + [
                    (
                        (
                            lambda moves, idx=move_idx, mon=mon: (
                                ResolveMoveToCSV(moves[idx][0]) +
                                (
                                    f" - {mon.ppcounts[idx]}"
                                    if "TRAINER_DATA_EXTRA_TYPE_PP_COUNTS" in mon.additionalFlags and moves[idx][0] != "MOVE_NONE"
                                    else ""
                                )
                            ) if idx < len(moves) else ""
                        )(get_last_moves(mon.pokemon[0], mon.level, mons), move_idx)
                    ) if idx < trainer.nummons else ""
                    for idx, mon in enumerate(trainer.party)
                ]
            )
            current_row += 1



    return output.getvalue()

def get_last_moves(species: str, level: int, mons_dict: dict, n_moves: int = 4):
    mon = mons_dict.get(species)
    if not mon:
        return []

    filtered_moves = [move for move in mon.learnset if move[1] <= int(level)]
    filtered_moves.sort(key=lambda m: m[1], reverse=True)

    return filtered_moves[:n_moves]


def get_or_dash(attr_list: List, index: int):
    if index >= len(attr_list):
        return "-"
    v = attr_list[index]
    if isinstance(v, str) and not v:
        return "-"
    if isinstance(v, int) and v == 0:
        return "-"
    return v

def int_to_letter(n: int) -> str:
    result = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        result = chr(65 + remainder) + result
    return result

def getMonFormula(row, cols):
    formulas = []
    for col in cols:
        cell = int_to_letter(col) + str(row)
        formula = (
            f'\'=SIERREUR(SI(DROITE({cell};1)=\"\";'
            f'INDEX(\'Pokémon\'!$C:$C; EQUIV(VRAI; INDEX(MINUSCULE(\'Pokémon\'!$A:$A)=MINUSCULE(GAUCHE({cell};NBCAR({cell})-1)); 0); 0));'
            f'INDEX(\'Pokémon\'!$B:$B; EQUIV(VRAI; INDEX(MINUSCULE(\'Pokémon\'!$A:$A)=MINUSCULE({cell}); 0); 0)));'
            f'SI(ESTTEXTE({cell}); \'Pokémon\'!$B$2; \"\"))'
        )
        formulas.append(formula)
    return formulas

def getTrainerFormula(row, col):
    cell = int_to_letter(col) + str(row)
    formula = (f'\'=LET(cleanStr; REGEXREPLACE(${cell}; \" ?\\[[^\\]]*\\]\"; \"\");mots; SPLIT(cleanStr; \" \");nbMots; NBVAL(mots);contientEt; ESTNUM(CHERCHE(\" & \"; cleanStr));classPart; SI(contientEt;INDEX(mots; 1);SI(nbMots > 1;GAUCHE(cleanStr;TROUVE(\"☃\";SUBSTITUE(cleanStr; \" \"; \"☃\"; nbMots - 1)) - 1);\"\"));lastPart; SI(contientEt;SI(nbMots >= 3;INDEX(mots; nbMots-2) & \" \" & INDEX(mots; nbMots-1) & \" \" & INDEX(mots; nbMots);cleanStr);SI(nbMots > 1;DROITE(cleanStr;NBCAR(cleanStr) - TROUVE(\"☃\";SUBSTITUE(cleanStr; \" \"; \"☃\"; nbMots - 1)));cleanStr));resultat1; RECHERCHEX(SUPPRESPACE(classPart); Trainers!$B:$B; Trainers!$C:$C; \"\");resultat2; RECHERCHEX(SUPPRESPACE(classPart); Trainers!$B:$B; Trainers!$C:$C; Trainers!$C$2);resultat3; RECHERCHEX(SUPPRESPACE(lastPart); Trainers!$B:$B; Trainers!$C:$C; Trainers!$C$2);SI(resultat1 <> \"\"; resultat2; resultat3))')
    return [formula]

def calcMonNature(trainer, mon):
    global trainerClassDefines
    global speciesDefines
    global trainerGenders
    global natureDefines

    trid = int(trainer.id)
    trclass = int(trainerClassDefines.index(trainer.trainerclass))
    trclassmale = not (trainerGenders[trainer.trainerclass] == "TRAINER_FEMALE")
    pokeid = int(speciesDefines.index(mon.pokemon[0]))
    level = int(mon.level)
    dv = int(mon.dv)

    return natureDefines[generate_pid(trid,trclass,trclassmale,pokeid,level,dv)%100%25]

def generate_pid(trid, trclass, trclassmale, pokeid, level, dv):

    rnd = trid + pokeid + level + dv
    set_random(rnd)
    
    while trclass > 0:
        rnd = random_num()
        trclass -= 1
        
    rnd = (rnd >> 16) & 0xffff
    rnd *= 256
    rnd += 136 if trclassmale else 120

    return int(rnd)

seed = 0

def set_random(new_seed):
    global seed
    seed = new_seed

def random_num():
    global seed
    result = 0x41c64e6d * seed + 0x6073
    seed = result & 0xffffffff
    return result