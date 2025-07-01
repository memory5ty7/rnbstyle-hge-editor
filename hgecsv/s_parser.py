from common.trainer import TrainerData, TrainerMon
from typing import List

def parse_s(rows):

    trainers = []
    current = None
    monIdx = 0
    moveIdx = 0
    itemIdx = 0
    
    pokemonEditing = False

    for i, row in enumerate(rows):
        parts = row.strip().split(maxsplit=1)

        if len(parts) > 1:
            key = parts[0]
            value = parts[1]

            match key:
                case "trainerdata":
                    current = TrainerData()
                    current.party = [TrainerMon() for _ in range(6)]
                    itemIdx = 0
                    pokemonEditing = False

                    parts = [part.strip() for part in value.split(',', 1)]
                    current.id = parts[0]
                    current.name = parts[1].replace('"','')
                case "trainermontype":
                    current.trainermontype = set(v.strip() for v in value.split('|'))
                case "trainerclass":
                    current.trainerclass = value
                case "nummons":
                    current.nummons = int(value)
                case "aiflags":
                    current.aiflags = set(v.strip() for v in value.split('|'))
                case "battletype":
                    current.battletype = value

                case "item":
                    if pokemonEditing:
                        current.party[monIdx].item = value
                    else:
                        current.item[itemIdx] = value
                        itemIdx += 1

                case "party":
                    monIdx = 0
                    pokemonEditing = True
                case "ivs":
                    current.party[monIdx].dv = value
                    moveIdx = 0
                case "abilityslot":
                    current.party[monIdx].abilityslot = value
                case "level":
                    current.party[monIdx].level = value
                case "pokemon":
                    current.party[monIdx].pokemon = (value, 0)
                case "monwithform":
                    parts = [part.strip() for part in value.split(',', 1)]
                    species = parts[0]
                    form = parts[1]
                    current.party[monIdx].pokemon = (species, form)
                case "item":
                    current.party[monIdx].item = value
                    itemcount += 1
                case "move":
                    current.party[monIdx].move[moveIdx] = value
                    moveIdx += 1
                case "ability":
                    current.party[monIdx].ability = value
                case "ball":
                    current.party[monIdx].ball = value
                case "setivs":
                    ivs = [int(x.strip()) for x in value.split(',')]
                    current.party[monIdx].setivs = ivs
                case "setevs":
                    evs = [int(x.strip()) for x in value.split(',')]
                    current.party[monIdx].setevs = evs
                case "nature":
                    current.party[monIdx].nature = value
                case "shinylock":
                    current.party[monIdx].shinylock = bool(int(value))
                case "additionalflags":
                    current.party[monIdx].additionalFlags = set(v.strip() for v in value.split('|'))
                case "status":
                    current.party[monIdx].status = value
                case "stathp":
                    current.party[monIdx].stats[0] = value
                case "statatk":
                    current.party[monIdx].stats[1] = value
                case "statdef":
                    current.party[monIdx].stats[2] = value
                case "statspeed":
                    current.party[monIdx].stats[3] = value
                case "statspatk":
                    current.party[monIdx].stats[4] = value
                case "statspdef":
                    current.party[monIdx].stats[5] = value
                case "ppcounts":
                    ppcounts = [int(x.strip()) for x in value.split(',')]
                    current.party[monIdx].ppcounts = ppcounts
                case "nickname":
                    key, rest = value.split(' ', 1)

                    parts = [p.strip() for p in rest.split(',')]

                    chars = []
                    for part in parts:
                        if part == "_endstr":
                            break

                    clean_char = part.strip('_')
                    chars.append(clean_char)

                    result_string = "".join(chars)

                    current.party[monIdx].nickname = result_string
                case "ballseal":
                    current.party[monIdx].ballseal = value
                    monIdx += 1
        elif parts == ['endparty']:
            trainers.append(current)
            monIdx = 0
            moveIdx = 0
            itemIdx = 0
            

    return trainers