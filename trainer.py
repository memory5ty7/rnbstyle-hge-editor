from dataclasses import dataclass, field
from typing import List, Tuple, Set
from config import Config

@dataclass
class TrainerMon:
    dv: int = Config.DEFAULT_DV
    abilityslot: int = 0
    level: int = 0
    pokemon: tuple[str, int] = ("SPECIES_NONE",0)
    item: str = "ITEM_NONE"
    move: List[str] = field(default_factory=lambda: ["MOVE_NONE", "MOVE_NONE", "MOVE_NONE", "MOVE_NONE"])
    ability: str = "ABILITY_NONE"
    ball: str = Config.DEFAULT_BALL
    setivs: List[int] = field(default_factory=lambda: Config.DEFAULT_IVS.copy)
    setevs: List[int] = field(default_factory=lambda: Config.DEFAULT_EVS.copy)
    nature: str = "NATURE_HARDY"
    shinylock: bool = False
    # Additional flags
    additionalFlags: List[str] = field(default_factory=list)
    status: int = 0x0
    stats: List[int] = field(default_factory=lambda: [0, 0, 0, 0, 0, 0])
    # types: Tuple[str, str] = ("TYPE_NORMAL", "TYPE_NORMAL")
    ppcounts: List[int] = field(default_factory=lambda: [0, 0, 0, 0])
    nickname: str = ""
    ballseal: int = 0

@dataclass
class TrainerData:
    id: int = 0
    name: str = ""
    trainermontype: Set[str] = field(default_factory=set)
    trainerclass: str = "Ethan"
    nummons: int = 0
    item: List[str] = field(default_factory=lambda: Config.DEFAULT_ITEMS.copy())
    aiflags: Set[str] = field(default_factory=lambda: Config.DEFAULT_AI_FLAGS.copy())
    battletype: bool = False
    party: List[TrainerMon] = field(default_factory=list)