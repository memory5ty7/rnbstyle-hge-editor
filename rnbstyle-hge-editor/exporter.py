from trainer import TrainerData, TrainerMon
from typing import List

def format_nickname(nickname: str) -> str:
    nickname_parts = []

    for char in nickname:
        if char.isupper():
            nickname_parts.append(f"_{char}")
        elif char.islower():
            nickname_parts.append(f"_{char}_")
        else:
            raise ValueError(f"Unsupported character in nickname: {char}")

    # Pad to 12 fields (nickname + _endstr + 0 padding)
    nickname_parts.append("_endstr")
    while len(nickname_parts) < 12:
        nickname_parts.append("0")

    return "nickname " + ", ".join(nickname_parts)    

def print_data(data : List[TrainerData], output_file):
    with open(output_file, 'a+') as f:
        for trainer in data:

            if trainer is None:
                continue
            if trainer.name == "":
                continue

            f.write(f"\n\ntrainerdata 0, \"{trainer.name}\"\n")
            f.write(f"    trainermontype {(" | ".join(trainer.trainermontype))}\n")
            f.write(f"    trainerclass {trainer.trainerclass}\n")
            f.write(f"    nummons {trainer.nummons}\n")

            # Write up to 4 items (pad if needed)
            items = trainer.items if hasattr(trainer, "items") else []
            while len(items) < 4:
                items.append("ITEM_NONE")
            for item in items[:4]:
                f.write(f"    item {item}\n")

            f.write(f"    aiflags {(" | ".join(trainer.aiflags) + " | 0")}\n")

            f.write(f"    battletype {"DOUBLE_BATTLE" if trainer.battletype else "SINGLE_BATTLE"}\n")
            f.write("    endentry\n\n")

            # Party
            f.write(f"    party {trainer.id}\n")
            for idx, mon in enumerate(trainer.party):
                # Mandatory fields
                f.write(f"        // mon {idx}\n")
                f.write(f"        ivs {mon.dv}\n")
                f.write(f"        abilityslot {mon.abilityslot}\n")
                f.write(f"        level {mon.level}\n")
                if (mon.pokemon[1] != 0):
                    f.write(f"        monwithform {"SPECIES_"+mon.pokemon[0].upper()}, {mon.pokemon[1]}\n")
                else:
                    f.write(f"        pokemon {"SPECIES_"+mon.pokemon[0].upper()}\n")

                # Trainermontype Fields
                if "TRAINER_DATA_TYPE_ITEMS" in trainer.trainermontype:
                    f.write(f"        item {"ITEM_"+mon.item.upper().replace(' ','_')}\n")
                if "TRAINER_DATA_TYPE_MOVES" in trainer.trainermontype:
                    for move in mon.move:
                        f.write(f"        move {"MOVE_"+move.upper().replace(' ', '_')}\n")
                if "TRAINER_DATA_TYPE_ABILITY" in trainer.trainermontype:
                    f.write(f"        ability {"ABILITY_"+mon.ability.upper()}\n")
                if "TRAINER_DATA_TYPE_BALL" in trainer.trainermontype:
                    f.write(f"        ball {"BALL_"+mon.ball.upper()}\n")
                if "TRAINER_DATA_TYPE_IV_EV_SET" in trainer.trainermontype:
                    f.write(f"        setivs {', '.join(map(str, mon.setivs()))}\n")
                    f.write(f"        setevs {', '.join(map(str, mon.setevs()))}\n")
                if "TRAINER_DATA_TYPE_NATURE" in trainer.trainermontype:
                    f.write(f"        nature {"NATURE_"+mon.nature.upper()}\n")

                # Additional Flags Fields
                if "TRAINER_DATA_EXTRA_TYPE_STATUS" in mon.additionalFlags:
                    f.write(f"        status {"STATUS_"+mon.status.upper()}\n")
                if "TRAINER_DATA_EXTRA_TYPE_HP" in mon.additionalFlags:
                    f.write(f"        stats {', '.join(map(str, mon.stats))}\n")
                if "TRAINER_DATA_EXTRA_TYPE_TYPES" in mon.additionalFlags:
                    f.write(f"        types {"TYPE_"+mon.types[0].upper()}, {"TYPE_"+mon.types[1].upper()}\n")
                if "TRAINER_DATA_EXTRA_TYPE_PP" in mon.additionalFlags:
                    f.write(f"        ppcounts {', '.join(map(str, mon.ppcounts))}\n")
                if "TRAINER_DATA_EXTRA_TYPE_NICKNAME" in trainer.trainermontype:
                    f.write(f"        nickname \"{format_nickname(mon.nickname)}\"\n")

                # Ball Seal at the end
                f.write(f"        ballseal {mon.ballseal}\n\n")

            f.write("    endparty\n")