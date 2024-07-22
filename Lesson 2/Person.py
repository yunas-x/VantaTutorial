from datetime import date

from .Pet import Pet
from .collections.Pets import Pets
from .enums.Gender import Gender
from .LivingBeing import LivingBeing


class Person(LivingBeing):

    def __init__(self, name: str, birthDate: date, gender: Gender, pets: Pets) -> None:
        super().__init__(name, birthDate, gender)
        self._pets = pets

    def adopt(self, pet: Pet):
        self._pets.add(pet)

    def leave(self, pet: Pet):
        self._pets.remove(pet)
    
    @property
    def Pets(self):
        return self._pets