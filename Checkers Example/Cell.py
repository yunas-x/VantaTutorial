from dataclasses import dataclass
from typing import Self

@dataclass
class Cell:
    coord_x: int
    coord_y: int
    is_occupied: bool

    def reacheable_from(self, other: Self):
        return (not self.is_occupied and (other.coord_x + 1 == self.coord_x or other.coord_x - 1 == self.coord_x))