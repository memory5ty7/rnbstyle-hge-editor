from typing import List
from common.trainer import TrainerData, TrainerMon
from common.resolve import ResolveMove, ResolveAbility, ResolveItem, ResolveNature, ResolveStatus, ResolveNickname, ResolveTrainerClass
from csvhge.validity_checker import CheckTrainerValidity

def print_data(data: List[TrainerData], output_file: str):
    with open(output_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for trainer in data:
        if trainer is None or trainer.name == "" or trainer.id == 0:
            continue

        trainer_id_line = f"trainerdata {trainer.id},"
        start_idx = end_idx = None

        new_block = []

        new_block.append(f"trainerdata {trainer.id}, \"{trainer.name}\"\n")

        if len(trainer.trainermontype) == 0:
            trainer.trainermontype.add("TRAINER_DATA_TYPE_NOTHING")
        new_block.append(f"    trainermontype {' | '.join(trainer.trainermontype)} | 0\n")

        trainer.trainerclass = ResolveTrainerClass(trainer.trainerclass, trainer.name)
        new_block.append(f"    trainerclass {trainer.trainerclass}\n")
        new_block.append(f"    nummons {trainer.nummons}\n")

        for item in trainer.item:
            new_block.append(f"    item {item}\n")

        new_block.append(f"    aiflags {' | '.join(trainer.aiflags)} | 0\n")
        new_block.append(f"    battletype {'DOUBLE_BATTLE' if trainer.battletype else 'SINGLE_BATTLE'}\n")
        new_block.append(f"    endentry\n\n")

        new_block.append(f"    party {trainer.id}\n")
        for idx, mon in enumerate(trainer.party):
            new_block.append(f"        // mon {idx}\n")
            new_block.append(f"        ivs {mon.dv}\n")
            new_block.append(f"        abilityslot {mon.abilityslot}\n")
            new_block.append(f"        level {mon.level}\n")
            mon.pokemon = ("SPECIES_"+mon.pokemon[0].replace(' ','_').upper(),mon.pokemon[1])
            if mon.pokemon[1] != 0:         
                new_block.append(f"        monwithform {mon.pokemon[0]}, {mon.pokemon[1]}\n")
            else:
                new_block.append(f"        pokemon {mon.pokemon[0]}\n")

            if "TRAINER_DATA_TYPE_ITEMS" in trainer.trainermontype:
                mon.item = ResolveItem(mon.item)
                new_block.append(f"        item {mon.item}\n")
            if "TRAINER_DATA_TYPE_MOVES" in trainer.trainermontype:
                for move_idx in range(4):
                    mon.move[move_idx] = ResolveMove(mon.move[move_idx])
                    new_block.append(f"        move {mon.move[move_idx]}\n")
            if "TRAINER_DATA_TYPE_ABILITY" in trainer.trainermontype:
                mon.ability = ResolveAbility(mon.ability)
                new_block.append(f"        ability {mon.ability}\n")
            if "TRAINER_DATA_TYPE_BALL" in trainer.trainermontype:
                mon.ball = ResolveItem(mon.ball)
                new_block.append(f"        ball {mon.ball}\n")
            if "TRAINER_DATA_TYPE_IV_EV_SET" in trainer.trainermontype:
                mon.ivs = mon.setivs() if callable(mon.setivs) else mon.setivs
                new_block.append(f"        setivs {', '.join(map(str, mon.ivs))}\n")
                mon.evs = mon.setevs() if callable(mon.setevs) else mon.setevs
                new_block.append(f"        setevs {', '.join(map(str, mon.evs))}\n")
            if "TRAINER_DATA_TYPE_NATURE_SET" in trainer.trainermontype:
                mon.nature = ResolveNature(mon.nature)
                new_block.append(f"        nature {mon.nature}\n")
            if "TRAINER_DATA_TYPE_SHINY_LOCK" in trainer.trainermontype:
                new_block.append(f"        shinylock {int(mon.shinylock)}\n")
            if "TRAINER_DATA_TYPE_ADDITIONAL_FLAGS" in trainer.trainermontype:
                if mon.additionalFlags:
                    flags_str = ' | '.join(tag.strip('[]') for tag in mon.additionalFlags)
                else:
                    flags_str = '0'
                new_block.append(f"        additionalflags {flags_str}\n")

            if "TRAINER_DATA_EXTRA_TYPE_STATUS" in mon.additionalFlags:
                mon.status = hex(ResolveStatus(mon.status))
                new_block.append(f"        status {mon.status}\n")
            if "TRAINER_DATA_EXTRA_TYPE_HP" in mon.additionalFlags:
                new_block.append(f"        stathp {mon.stats[0]}\n")
                new_block.append(f"        statatk {mon.stats[1]}\n")
                new_block.append(f"        statdef {mon.stats[2]}\n")
                new_block.append(f"        statspeed {mon.stats[3]}\n")
                new_block.append(f"        statspatk {mon.stats[4]}\n")
                new_block.append(f"        statspdef {mon.stats[5]}\n")
            # if "TRAINER_DATA_EXTRA_TYPE_TYPES" in mon.additionalFlags:
            #     mon.types = ResolveTypes(mon.types)
            #     new_block.append(f"        types {mon.types[0]}, {mon.types[1]}\n")
            if "TRAINER_DATA_EXTRA_TYPE_PP_COUNTS" in mon.additionalFlags:
                ppcounts = mon.ppcounts() if callable(mon.ppcounts) else mon.ppcounts
                new_block.append(f"        ppcounts {', '.join(map(str, ppcounts))}\n")
            if "TRAINER_DATA_EXTRA_TYPE_NICKNAME" in mon.additionalFlags:
                mon.nickname = ResolveNickname(mon.nickname)
                new_block.append(f"        nickname {mon.nickname}\n")

            new_block.append(f"        ballseal {mon.ballseal}\n\n")
        
        new_block.append("    endparty\n")


        if CheckTrainerValidity(trainer):

            # Locate existing trainer block
            for i, line in enumerate(lines):
                if line.strip().startswith(trainer_id_line):
                    start_idx = i
                if start_idx is not None and line.strip().startswith("endparty"):
                    end_idx = i
                    break

            # Replace existing block or append if not found
            if start_idx is not None and end_idx is not None:
                lines[start_idx:end_idx + 1] = new_block
            else:
                lines.extend(["\n"] + new_block)
            #print(f"Inserted trainer : {trainer.name} with ID {trainer.id}")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)



