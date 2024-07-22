from datetime import date
from .enums.Gender import Gender
from .enums.Species import Species
from .LivingBeing import LivingBeing

class Pet(LivingBeing):

    def __init__(self, name: str, birthDate: date, gender: Gender, species: Species = Species.Unknown) -> None:
        super().__init__(name, birthDate, gender)
        self._species = species

    @property
    def Species(self):
        return str(self._species)
    
    def __str__(self) -> str:
        return f"{self.Species} {self.Gender} called {self.Name} of age {self.Age}"
    
    def specify_species(self, species: Species):
        if self._species == Species.Unknown:
            self._species = species
        else:
            raise ValueError("Species already set")