class Config:
    # Directories and file paths
    INPUT_DIR = "csv"
    ROOT_DIR = "../hg-engine/"
    DATA_DIR = "armips/data/"

    # hg-engine directories
    TRAINER_DIR = ROOT_DIR + DATA_DIR + "trainers/"
    MONDATA_FILE = ROOT_DIR + DATA_DIR + "mondata.s"
    LEARNSETS_FILE = ROOT_DIR + DATA_DIR + "levelupdata.s"
    OUTPUT_FILE = TRAINER_DIR + "trainers.s"

    # If set to True, a copy of trainers.s will be created before priting the trainers
    CREATE_BACKUP = True
    BACKUP_FILE = TRAINER_DIR + "trainers_backup.s"

    INCLUDE_DIR = ROOT_DIR + "include/"
    CONSTANTS_DIR = INCLUDE_DIR + "constants/"
    ABILITY_HEADER = CONSTANTS_DIR + "ability.h"
    ITEM_HEADER = CONSTANTS_DIR + "item.h"    
    MOVE_HEADER = CONSTANTS_DIR + "moves.h"    
    SPECIES_HEADER = CONSTANTS_DIR + "species.h"
    TRAINERCLASS_HEADER = CONSTANTS_DIR + "trainerclass.h"
    BATTLE_HEADER = INCLUDE_DIR + "battle.h"
    POKEMON_HEADER = INCLUDE_DIR + "pokemon.h"

    
    # Trainer Configuration

    # Default Trainer AI Flags
    DEFAULT_AI_FLAGS = ["F_PRIORITIZE_SUPER_EFFECTIVE", "F_EVALUATE_ATTACKS", "F_EXPERT_ATTACKS"]

    # Default Trainer Items
    DEFAULT_ITEMS = ["ITEM_NONE", "ITEM_NONE", "ITEM_NONE", "ITEM_NONE"]


    # Pokémon Configuration

    # Default DV Value if there is no "DV" row
    DEFAULT_DV = 255

    # Use custom IV/EV values instead of DV even if there are no "IV" or "EV" rows
    USE_IV_EV = True
    DEFAULT_IVS = [31, 31, 31, 31, 31, 31] # HP, ATK, DEF, SPD, SPATK, SPDEF
    DEFAULT_EVS = [0, 0, 0, 0, 0, 0]       # HP, ATK, DEF, SPD, SPATK, SPDEF

    # Default Ball if there is no "Ball" row
    DEFAULT_BALL = "ITEM_POKE_BALL"


    # hgecsv Configuration
    DEFAULT_INPUT_FILE = TRAINER_DIR + "trainers.s"
    DEFAULT_OUTPUT_FILE = "trainers.csv"

    # Which rows to print if the corresponding row is present
    ROWS_TO_PRINT = {
        "DV" : True,
        "Ability Slot" : True,
        "Level" : True,
        "Pokémon" : True,
        "Held Item" : True,
        "Moves" : True,
        "Ability" : True,
        "Ball Type" : True,
        "IVs" : True,
        "EVs" : True,
        "Nature" : True,
        "Status" : True,
        "Stats" : True,
        "Nickname" : True,
        "Ball Seal" : True,
    }

    # Print Ability instead of Ability Slot
    PRINT_ABILITY_ABILITY_SLOT = True

    # Print IVs instead of DVs
    PRINT_IV_DV = True

    # Print Moves when the moves are the default level-up ones
    PRINT_MOVES_DEFAULT = True

    # Print Nature even if there is no "Nature" row
    PRINT_NATURE_DEFAULT = True
    