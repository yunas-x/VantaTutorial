from dataclasses import dataclass
from typing import Literal, Self

@dataclass
class Cell:
    coord_x: int
    coord_y: int
    player_id: Literal[0, 1, 2] # 0 - пусто, 1 - красный, 2 - черный
    #is_occupied: bool

    def reacheable_from(self, other: Self):
        # Тут переписать для двух цветов
        return (not self.is_occupied and (other.coord_x + 1 == self.coord_x)) # для другого цвета смотрим other.coord_x - 1