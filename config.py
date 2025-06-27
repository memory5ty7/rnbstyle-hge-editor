class Config:
    # Directories and file paths
    INPUT_DIR = "csv"
    ROOT_DIR = "../hg-engine/"

    # hg-engine directories
    OUTPUT_FILE = ROOT_DIR + "armips/data/trainers/trainers.s"
    INCLUDE_DIR = ROOT_DIR + "include/"
    CONSTANTS_DIR = INCLUDE_DIR + "constants/"
    ABILITY_HEADER = CONSTANTS_DIR + "ability.h"
    ITEM_HEADER = CONSTANTS_DIR + "item.h"    
    MOVE_HEADER = CONSTANTS_DIR + "moves.h"    
    SPECIES_HEADER = CONSTANTS_DIR + "species.h"
    TRAINERCLASS_HEADER = CONSTANTS_DIR + "trainerclass.h"
    BATTLE_HEADER = INCLUDE_DIR + "battle.h"
    
    # Configuration of the Tool

    # Default DV Value if there is no "DV" row (IVs are calculated using the formula IVs = DV / 255 * 31; IVs are 0 by default)
    DEFAULT_DV = 255

    # Use custom IV/EV values instead of DV even if there are no "IV" or "EV" rows
    USE_IV_EV = True
    DEFAULT_IVS = [31, 31, 31, 31, 31, 31] # HP, ATK, DEF, SPD, SPATK, SPDEF
    DEFAULT_EVS = [0, 0, 0, 0, 0, 0]       # HP, ATK, DEF, SPD, SPATK, SPDEF

    # Default AI flags for Trainers
    DEFAULT_AI_FLAGS = ["F_PRIORITIZE_SUPER_EFFECTIVE", "F_EVALUATE_ATTACKS", "F_EXPERT_ATTACKS"]

    # Default Ball if there is no "Ball" row
    DEFAULT_BALL = "POKE_BALL"