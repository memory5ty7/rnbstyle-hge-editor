from trainer import TrainerData, TrainerMon
from typing import List
from resolve import ResolveMove, ResolveAbility, ResolveItem, ResolveBall, ResolveNature, ResolveStatus, ResolveTypes, ResolveNickname, ResolveTrainerClass
from header_parser import defines

def print_data(data: List[TrainerData], output_file: str):
    with open(output_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for trainer in data:
        if trainer is None or trainer.name == "" or trainer.id == 0:
            continue

        trainer_id_line = f"trainerdata {trainer.id},"
        start_idx = end_idx = None

        # Locate existing trainer block
        for i, line in enumerate(lines):
            if line.strip().startswith(trainer_id_line):
                start_idx = i
            if start_idx is not None and line.strip().startswith("endparty"):
                end_idx = i
                break

        # Generate replacement block
        new_block = []

        new_block.append(f"trainerdata {trainer.id}, \"{trainer.name}\"\n")

        if len(trainer.trainermontype) == 0:
            trainer.trainermontype.add("TRAINER_DATA_TYPE_NOTHING")
        new_block.append(f"    trainermontype {' | '.join(trainer.trainermontype)} | 0\n")

        trainerclass = ResolveTrainerClass(trainer.trainerclass, trainer.name)
        new_block.append(f"    trainerclass {trainerclass}\n")
        new_block.append(f"    nummons {trainer.nummons}\n")

        items = trainer.items if hasattr(trainer, "items") else []
        while len(items) < 4:
            items.append("ITEM_NONE")
        for item in items[:4]:
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
            if mon.pokemon[1] != 0:
                new_block.append(f"        monwithform SPECIES_{mon.pokemon[0].upper()}, {mon.pokemon[1]}\n")
            else:
                new_block.append(f"        pokemon SPECIES_{mon.pokemon[0].upper()}\n")

            if "TRAINER_DATA_TYPE_ITEMS" in trainer.trainermontype:
                item = ResolveItem(mon.item)
                new_block.append(f"        item {item}\n")
            if "TRAINER_DATA_TYPE_MOVES" in trainer.trainermontype:
                for move in mon.move:
                    move = ResolveMove(move)
                    new_block.append(f"        move {move}\n")
            if "TRAINER_DATA_TYPE_ABILITY" in trainer.trainermontype:
                ability = ResolveAbility(mon.ability)
                new_block.append(f"        ability {ability}\n")
            if "TRAINER_DATA_TYPE_BALL" in trainer.trainermontype:
                ball = ResolveItem(mon.ball)
                new_block.append(f"        ball {ball}\n")
            if "TRAINER_DATA_TYPE_IV_EV_SET" in trainer.trainermontype:
                ivs = mon.setivs() if callable(mon.setivs) else mon.setivs
                new_block.append(f"        setivs {', '.join(map(str, ivs))}\n")
                evs = mon.setevs() if callable(mon.setevs) else mon.setevs
                new_block.append(f"        setevs {', '.join(map(str, evs))}\n")
            if "TRAINER_DATA_TYPE_NATURE_SET" in trainer.trainermontype:
                nature = ResolveNature(mon.nature)
                new_block.append(f"        nature {nature}\n")
            if "TRAINER_DATA_TYPE_SHINY_LOCK" in trainer.trainermontype:
                shinylock = mon.shinylock
                new_block.append(f"        shinylock {int(mon.shinylock)}\n")
            if "TRAINER_DATA_TYPE_ADDITIONAL_FLAGS" in trainer.trainermontype:
                if mon.additionalFlags:
                    flags_str = ' | '.join(tag.strip('[]') for tag in mon.additionalFlags)
                else:
                    flags_str = '0'
                new_block.append(f"        additionalflags {flags_str}\n")

            if "TRAINER_DATA_EXTRA_TYPE_STATUS" in mon.additionalFlags:
                status = hex(ResolveStatus(mon.status))
                new_block.append(f"        status {status}\n")
            if "TRAINER_DATA_EXTRA_TYPE_HP" in mon.additionalFlags:
                new_block.append(f"        stathp {mon.stats[0]}\n")
                new_block.append(f"        statatk {mon.stats[1]}\n")
                new_block.append(f"        statdef {mon.stats[2]}\n")
                new_block.append(f"        statspeed {mon.stats[3]}\n")
                new_block.append(f"        statspatk {mon.stats[4]}\n")
                new_block.append(f"        statspdef {mon.stats[5]}\n")
            if "TRAINER_DATA_EXTRA_TYPE_TYPES" in mon.additionalFlags:
                types = ResolveTypes(mon.types)
                new_block.append(f"        types {types[0]}, {types[1]}\n")
            if "TRAINER_DATA_EXTRA_TYPE_PP_COUNTS" in mon.additionalFlags:
                ppcounts = mon.ppcounts() if callable(mon.ppcounts) else mon.ppcounts
                new_block.append(f"        ppcounts {', '.join(map(str, ppcounts))}\n")
            if "TRAINER_DATA_EXTRA_TYPE_NICKNAME" in mon.additionalFlags:
                nickname = ResolveNickname(mon.nickname)
                new_block.append(f"        nickname {nickname}\n")

            new_block.append(f"        ballseal {mon.ballseal}\n\n")

        new_block.append("    endparty\n")

        # Replace existing block or append if not found
        if start_idx is not None and end_idx is not None:
            lines[start_idx:end_idx + 1] = new_block
        else:
            lines.extend(["\n"] + new_block)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)
