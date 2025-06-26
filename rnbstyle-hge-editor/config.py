class Config:
    INPUT_DIR = "csv"
    ROOT_DIR = "../"
    OUTPUT_FILE = ROOT_DIR + "armips/data/trainers/trainers.s"

    INCLUDE_DIR = ROOT_DIR + "include/"
    CONSTANTS_DIR = INCLUDE_DIR + "constants/"
    SPECIES_HEADER = INCLUDE_DIR + "species.h"
    MOVE_HEADER = INCLUDE_DIR + "moves.h"
    ITEM_HEADER = INCLUDE_DIR + "item.h"
    ABILITY_HEADER = INCLUDE_DIR + "ability.h"
    TRAINERCLASS_HEADER = INCLUDE_DIR + "trainerclass.h"

    DEFAULT_DV = 255

    DEFAULT_IV_EV_CONFIG = True
    DEFAULT_IVS = [31, 31, 31, 31, 31, 31] # HP, ATK, DEF, SPD, SPATK, SPDEF
    DEFAULT_EVS = [0, 0, 0, 0, 0, 0]       # HP, ATK, DEF, SPD, SPATK, SPDEF

    DEFAULT_AI_FLAGS = ["F_PRIORITIZE_SUPER_EFFECTIVE", "F_EVALUATE_ATTACKS", "F_EXPERT_ATTACKS"]
