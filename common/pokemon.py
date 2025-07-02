from dataclasses import dataclass, field
from typing import List

@dataclass
class Pokemon:
    species : str = "SPECIES_NONE"
    abilities: tuple[str, str] = ("ABILITY_NONE","ABILITY_NONE")
    learnset: List[tuple[str, int]] = field(default_factory=list)