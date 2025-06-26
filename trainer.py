from dataclasses import dataclass, field
from typing import List, Tuple, Set
from config import Config

@dataclass
class TrainerMon:
    dv: int = Config.DEFAULT_DV
    abilityslot: int = 0
    level: int = 0
    pokemon: tuple[int, int] = (0,0)
    item: int = "None"
    move: List[int] = field(default_factory=lambda: [0, 0, 0, 0])
    ability: str = "None"
    ball: int = "Poke Ball"
    setivs: List[int] = field(default_factory=lambda: Config.DEFAULT_IVS.copy)
    setevs: List[int] = field(default_factory=lambda: Config.DEFAULT_EVS.copy)
    nature: str = "Hardy"
    shinylock: bool = False
    # Additional flags
    additionalFlags: List[str] = field(default_factory=list)
    status: str = "None"
    stats: List[int] = field(default_factory=lambda: [0, 0, 0, 0, 0, 0])
    types: Tuple[int, int] = (0, 0)
    ppcounts: List[int] = field(default_factory=lambda: [0, 0, 0, 0])
    nickname: str = ""
    ballseal: int = 0

@dataclass
class TrainerData:
    id: int = 0
    name: str = ""
    trainermontype: Set[str] = field(default_factory=list)
    trainerclass: int = 0
    nummons: int = 0
    item: List[int] = field(default_factory=lambda: [0]*4)
    aiflags: Set[str] = field(default_factory=lambda: Config.DEFAULT_AI_FLAGS.copy())
    battletype: bool = False
    party: List[TrainerMon] = field(default_factory=list)