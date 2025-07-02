from common.pokemon import Pokemon
from typing import Dict

mons = {}


def parse_mons(mondata_file, learnsets_file):
    global mons

    with open(mondata_file, 'r', encoding="utf-8") as infile:
        rows = infile.read().splitlines()

        current_species = "SPECIES_NONE"

        for i, row in enumerate(rows):
            parts = row.strip().split(maxsplit=1)   

            if len(parts) > 1:
                key = parts[0]
                value = parts[1]

                match key:
                    case "mondata":
                        current_species = value.split(",")[0].strip()
                        if current_species not in mons:
                            mons[current_species] = Pokemon(species=current_species)
                            mons[current_species].species = current_species
                            mons[current_species].learnset =[('MOVE_NONE', 0), ('MOVE_NONE', 0), ('MOVE_NONE', 0), ('MOVE_NONE', 0)]
                    case "abilities":
                        if current_species not in mons:
                            mons[current_species] = Pokemon(species=current_species)
                        mons[current_species].abilities = [x.strip() for x in value.split(",")]

                if len(value) == 1:
                    current_species = value
                    

    with open(learnsets_file, 'r', encoding="utf-8") as infile:
        rows = infile.read().splitlines()

        current_species = "SPECIES_NONE"

        for i, row in enumerate(rows):
            parts = row.strip().split(maxsplit=1)

            if len(parts) > 1:
                key = parts[0]
                value = parts[1]

                move_parts = value.strip().split(',')

                if len(move_parts) == 2:
                    move = move_parts[0]
                    level = int(move_parts[1])

                    mons[current_species].learnset.append((move, level))
                elif len(move_parts) == 1 and move_parts[0].startswith("SPECIES_"):
                    current_species = move_parts[0]