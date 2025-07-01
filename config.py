class Config:
    # Directories and file paths
    INPUT_DIR = "csv"
    ROOT_DIR = "../hg-engine/"

    # hg-engine directories
    TRAINER_DIR = ROOT_DIR + "armips/data/trainers/"
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

    # print IVs/EVs (this includes automatically written IVs/EVs when USE_IV_EV is True)
    PRINT_IVS_EVS = False