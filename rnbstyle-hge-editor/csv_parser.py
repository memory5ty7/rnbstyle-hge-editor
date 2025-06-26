from resolve import ResolvePokemon
import re
from trainer import TrainerData, TrainerMon
from typing import List
from config import Config

def parse_csv(rows):
    headers = rows[0]

    trainers = []
    current = None

    for i, row in enumerate(rows):
        if not row or len(row) < 2:
            continue
        key = row[0].strip()
        value = row[1:7]

        match key:
            case "Name":
                trainers.append(current)
                current = TrainerData()

                if (Config.DEFAULT_IV_EV_CONFIG == True):
                    current.trainermontype.append("TRAINER_DATA_TYPE_IV_EV_SET")

                current.id = 0
                current.name = re.sub(r"^.*?\b(\w+)\s*(?:\[.*\])?$", r"\1", row[1])
            case "DV":
                for j, cell in enumerate(row[1:]):
                    current.party[j].dv = cell
            case "Ability Slot":
                for j, cell in enumerate(row[1:]):
                    current.party[j].abilityslot = cell
            case "Level":
                for j, cell in enumerate(row[1:]):
                    current.party[j].level = cell
            case "Pokémon":
                if i + 1 >= len(rows):
                    break
                next_row = rows[i + 1]
                for j, cell in enumerate(next_row[1:]):
                    current.party.append(TrainerMon())
                    current.party[j].pokemon = ResolvePokemon(cell)
                    current.nummons += 1
            case "Held Item":
                for j, cell in enumerate(row[1:]):
                    current.party[j].item = cell
                current.trainermontype.append("TRAINER_DATA_TYPE_ITEMS")
            case "Moves":
                for k in range(4):
                    if i + k >= len(rows):
                        break
                    move_row = rows[i + k]
                    for j, cell in enumerate(move_row[1:]):
                        current.party[j].move[k] = cell
                current.trainermontype.append("TRAINER_DATA_TYPE_MOVES")
            case "Ability":
                for j, cell in enumerate(row[1:]):
                    current.party[j].ability = cell
                current.trainermontype.append("TRAINER_DATA_TYPE_ABILITY")
            case "Ball Type":
                for j, cell in enumerate(row[1:]):
                    current.party[j].ball = cell
                current.trainermontype.append("TRAINER_DATA_TYPE_BALL")
            case "IVs":
                for j, cell in enumerate(row[1:]):
                    current.party[j].setivs = [int(x) for x in cell.split(',')]
                current.trainermontype.append("TRAINER_DATA_TYPE_IV_EV_SET")
            case "EVs":
                for j, cell in enumerate(row[1:]):
                    current.party[j].setivs = [int(x) for x in cell.split(',')]
                current.trainermontype.append("TRAINER_DATA_TYPE_IV_EV_SET")
            case "Nature":
                for j, cell in enumerate(row[1:]):
                    current.party[j].nature = cell
                current.trainermontype.append("TRAINER_DATA_TYPE_NATURE_SET")
            case "Status":
                for j, cell in enumerate(row[1:]):
                    current.party[j].status = cell
                    current.party[j].additionalFlags.append("TRAINER_DATA_EXTRA_TYPE_STATUS")
            case "Stats":
                for j, cell in enumerate(row[1:]):
                    current.party[j].stats = [int(x) for x in cell.split(',')]
                    current.party[j].additionalFlags.append("TRAINER_DATA_EXTRA_TYPE_HP")
                    current.party[j].additionalFlags.append("TRAINER_DATA_EXTRA_TYPE_ATK")
                    current.party[j].additionalFlags.append("TRAINER_DATA_EXTRA_TYPE_DEF")
                    current.party[j].additionalFlags.append("TRAINER_DATA_EXTRA_TYPE_SPEED")
                    current.party[j].additionalFlags.append("TRAINER_DATA_EXTRA_TYPE_SP_ATK")
                    current.party[j].additionalFlags.append("TRAINER_DATA_EXTRA_TYPE_SP_DEF")
            case "Types":
                for j, cell in enumerate(row[1:]):
                    types = [int(x) for x in cell.split(',')]
                    current.party[j].types = (types[0], types[1] if len(types) > 1 else 0)
                    current.trainermontype.append("TRAINER_DATA_EXTRA_TYPE_TYPES")
            case "PP":
                for j, cell in enumerate(row[1:]):
                    current.party[j].ppcounts = [int(x) for x in cell.split(',')]
                    current.trainermontype.append("TRAINER_DATA_EXTRA_TYPE_PP")
            case "Nickname":
                for j, cell in enumerate(row[1:]):
                    current.party[j].nickname = cell
                    current.trainermontype.append("TRAINER_DATA_EXTRA_TYPE_NICKNAME")
            case "Ball Seal":
                for j, cell in enumerate(row[1:]):
                    current.party[j].ballseal = cell
            # case "Shiny":
            case "":
                continue
            case _:
                print(f"Unknown Key in Row {i} : {key}")

    return trainers

