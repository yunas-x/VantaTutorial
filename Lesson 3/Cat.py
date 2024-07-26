from enum import StrEnum, auto

class CatSpecies(StrEnum):
    Russian = auto()
    Siamese = auto()
    Sphinx = auto()
    British = auto()

class Cat:

    def __init__(self, 
                 name: str, 
                 age: int, 
                 owner_id: int,
                 species: CatSpecies) -> None:
        
        self.name = name
        self.age = age
        self.owner_id = owner_id
        self.species = species