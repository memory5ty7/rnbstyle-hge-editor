import re
import os
import csv
from common.resolve import ResolvePokemon, ResolveItemForm, ResolvePPCount, ResolveHiddenPower
from common.trainer import TrainerData, TrainerMon
from config import Config

def list_csv_files(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".csv")]

def read_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as f:
        return list(csv.reader(f))
    
def parse_csv(rows, debug=False):

    trainers = []

    for i, row in enumerate(rows):
        if not row or len(row) < 2:
            continue
        key = row[0]

        if debug:
            print(row)

        if key.startswith("Name - "):          
            # Handle False Double Battles (two single trainers fought together)
            if (" / ") in key:
                trainer1, trainer2 = HandleFalseDouble(key, row, rows, i)
                trainers.append(trainer1)
                trainers.append(trainer2)
                continue

            trainers.append(HandleSingleTrainer(key, row, rows, i))

    return trainers

def HandleSingleTrainer(key, row, rows, i):
    nummons = min(6, sum(1 for cell in rows[i + 2][1:] if cell != ''))

    current = HandleTrainer(key, 1, rows, i, nummons)

    current.id = key.rsplit(" ", 1)[1]
    if not current.id.isdigit():
        current.id = 0

    tags = re.findall(r'\[.*?]', row[1])
    if "[Double]" in tags:
        current.battletype = True

    cleaned_str = re.sub(r'\s*\[.*?\]\s*$', '', row[1])
    words = cleaned_str.split()

    # Handle Double Battle Classes (Twins, etc.)
    if ' & ' in cleaned_str:
        name_words = 3
    else:
        name_words = 1

    current.name = ' '.join(words[-name_words:])
    current.trainerclass = ' '.join(words[:-name_words])

    return current

def HandleFalseDouble(key, row, rows, i):

    nummons1 = min(3, sum(1 for cell in rows[i + 2][1:3] if cell != ''))
    nummons2 = min(3, sum(1 for cell in rows[i + 2][4:6] if cell != ''))

    trainer1 = HandleTrainer(key, 1, rows, i, nummons1)
    trainer2 = HandleTrainer(key, 4, rows, i, nummons2)

    trainer1.battletype = False
    trainer2.battletype = False

    # id
    trainer1.id = key.rsplit("Name - ")[1].split(" / ")[0]
    trainer2.id = key.rsplit("Name - ")[1].split(" / ")[1]
    # tags
    name1 = re.sub(r'\s*\[.*?\]\s*$', '', row[1])
    name2 = re.sub(r'\s*\[.*?\]\s*$', '', row[1])
    name1 = name1.split(" & ")[0]
    name2 = name2.split(" & ")[1]
    # trainerclass and name
    trainer1.trainerclass = name1.rsplit(" ", 1)[0]
    trainer1.name = name1.rsplit(" ", 1)[1]
    trainer2.trainerclass = name2.rsplit(" ", 1)[0]
    trainer2.name = name2.rsplit(" ", 1)[1]

    #print(trainer1.id, trainer1.trainerclass, trainer1.name)
    #print(trainer2.id, trainer2.trainerclass, trainer2.name)

    return trainer1,trainer2

def HandleTrainer(key, start, rows, i, nummons):
    current = TrainerData()

    current.nummons = nummons
    current.party = [TrainerMon() for _ in range(nummons)]

    if (Config.USE_IV_EV == True):
        current.trainermontype.add("TRAINER_DATA_TYPE_IV_EV_SET")  

    i = i + 1

    while i < len(rows) and not rows[i][0].startswith("Name - "):
        key = rows[i][0]

        match key:
            case "DV":
                for j, cell in enumerate(rows[i][start:start + current.nummons]):
                    current.party[j].dv = cell
            case "Ability Slot":
                for j, cell in enumerate(rows[i][start:start + current.nummons]):
                    current.party[j].abilityslot = cell
            case "Level":
                for j, cell in enumerate(rows[i][start:start + current.nummons]):
                    current.party[j].level = cell
            case "Pokémon":
                if i + 1 >= len(rows):
                    break
                next_row = rows[i + 1]
                for j, cell in enumerate(next_row[start:start + current.nummons]):
                    if j >= current.nummons:
                        i += 1
                        continue
                    if cell != '':
                        if cell.endswith('*'):
                            cell = cell[:-1]
                            current.party[j].shinylock = True
                            current.trainermontype.add("TRAINER_DATA_TYPE_SHINY_LOCK")
                        current.party[j].pokemon = ResolvePokemon(cell)
            case "Held Item":
                for j, cell in enumerate(rows[i][start:start + current.nummons]):
                    if cell != "-" and cell != "":
                        current.party[j].item = cell
                        current.party[j].pokemon, current.party[j].item = ResolveItemForm(current.party[j].pokemon, current.party[j].item)
                current.trainermontype.add("TRAINER_DATA_TYPE_ITEMS")
            case "Moves":
                for k in range(4):
                    if i + k >= len(rows):
                        break
                    move_row = rows[i + k]
                    for j, cell in enumerate(move_row[start:start + current.nummons]):
                        if cell != "-" and cell != "":
                            current.party[j].move[k], current.party[j].setivs, current.trainermontype = ResolveHiddenPower(cell, current.party[j].setivs, current.trainermontype)
                            current.party[j].move[k], current.party[j].ppcounts[k] = ResolvePPCount(cell)
                            if current.party[j].ppcounts[k] != 0:
                                current.party[j].additionalFlags.append("TRAINER_DATA_EXTRA_TYPE_PP_COUNTS")
                                current.trainermontype.add("TRAINER_DATA_TYPE_ADDITIONAL_FLAGS")
                current.trainermontype.add("TRAINER_DATA_TYPE_MOVES")
            case "Ability":
                for j, cell in enumerate(rows[i][start:start + current.nummons]):
                    if "/" in cell:
                        cell = cell.split("/")[0].strip()
                    current.party[j].ability = cell
                current.trainermontype.add("TRAINER_DATA_TYPE_ABILITY")
            case "Ball Type":
                for j, cell in enumerate(rows[i][start:start + current.nummons]):
                    current.party[j].ball = cell
                current.trainermontype.add("TRAINER_DATA_TYPE_BALL")
            case "IVs":
                #if "," in cell:
                #    for j, cell in enumerate(rows[i][start:start + current.nummons]):
                #        current.party[j].setivs = [int(x.strip()) for x in cell.split(',')]
                #else:
                for j, cell in enumerate(rows[i][start:start + current.nummons]):
                    current.party[j].setivs = [cell] * 6
            case "EVs":
                for j, cell in enumerate(rows[i][start:start + current.nummons]):
                    current.party[j].setivs = [int(x) for x in cell.split(',')]
                current.trainermontype.add("TRAINER_DATA_TYPE_IV_EV_SET")
            case "Nature":
                for j, cell in enumerate(rows[i][start:start + current.nummons]):
                    current.party[j].nature = cell
                current.trainermontype.add("TRAINER_DATA_TYPE_NATURE_SET")
            case "Status":
                for j, cell in enumerate(rows[i][start:start + current.nummons]):
                    if cell != "-" and cell != "":
                        current.party[j].status = cell
                        current.party[j].additionalFlags.append("TRAINER_DATA_EXTRA_TYPE_STATUS")
                    current.trainermontype.add("TRAINER_DATA_TYPE_ADDITIONAL_FLAGS")
            case "Stats":
                for j, cell in enumerate(rows[i][start:start + current.nummons]):
                    if cell != '-' and cell != "":
                        current.party[j].stats = [int(x) for x in cell.split(',')]
                        current.party[j].additionalFlags.append("TRAINER_DATA_EXTRA_TYPE_HP")
                        current.party[j].additionalFlags.append("TRAINER_DATA_EXTRA_TYPE_ATK")
                        current.party[j].additionalFlags.append("TRAINER_DATA_EXTRA_TYPE_DEF")
                        current.party[j].additionalFlags.append("TRAINER_DATA_EXTRA_TYPE_SPEED")
                        current.party[j].additionalFlags.append("TRAINER_DATA_EXTRA_TYPE_SP_ATK")
                        current.party[j].additionalFlags.append("TRAINER_DATA_EXTRA_TYPE_SP_DEF")
                    current.trainermontype.add("TRAINER_DATA_TYPE_ADDITIONAL_FLAGS")
            # case "Types":
            #     for j, cell in enumerate(row[start:start + current.nummons]):
            #         if cell != "-":
            #             if ',' in cell:
            #                 current.party[j].types = cell.split(', ')
            #             else:
            #                 current.party[j].types = [cell, cell]
            #             current.party[j].additionalFlags.append("TRAINER_DATA_EXTRA_TYPE_TYPES")
            #         current.trainermontype.add("TRAINER_DATA_TYPE_ADDITIONAL_FLAGS")
            case "Nickname":
                for j, cell in enumerate(rows[i][start:start + current.nummons]):
                    if cell != "-" and cell != "":
                        current.party[j].nickname = cell
                        current.party[j].additionalFlags.append("TRAINER_DATA_EXTRA_TYPE_NICKNAME")
                    current.trainermontype.add("TRAINER_DATA_TYPE_ADDITIONAL_FLAGS")
            case "Ball Seal":
                for j, cell in enumerate(rows[i][start:start + current.nummons]):
                    if cell != "-" and cell != "":
                        current.party[j].ballseal = cell
            # case "Shiny":
            case "":
                i += 1
                continue
            case _:
                print(f"Unknown Key in Row {i} : {key}")

        i += 1


    return current