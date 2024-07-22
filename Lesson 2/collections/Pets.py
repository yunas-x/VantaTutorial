from typing import MutableSequence

from ..enums.Gender import Gender
from ..Pet import Pet

class Pets():

    def __init__(self, pets: MutableSequence[Pet]) -> None:
        self._pets = pets

    def as_list(self):
        return list(self._pets)
    
    def add(self, pet: Pet):
        self._pets.append(pet)

    def remove(self, pet: Pet):
        self._pets.remove(pet)
        
    def dominating_gender(self) -> Gender:
        gender_mask = [1 if p.Gender == Gender.Male else -1 for p in self._pets]
        if sum(gender_mask) > 0:
            return Gender.Male
        elif sum(gender_mask) < 0:
            return Gender.Female
        else:
            return Gender.Neither

    def average_age(self) -> int:
        return round(sum([p.Age for p in self._pets]) / len(self._pets), 2)
    
    def __str__(self) -> str:
        return "\n".join([str(p) for p in self._pets])