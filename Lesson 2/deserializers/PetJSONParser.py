from datetime import date
from ..enums.Gender import Gender
from ..enums.Species import Species
from ..Pet import Pet
from .protocols.Parser import Parser

class PetJSONParser(Parser):

    gender_mapper = {
        "male": Gender.Male,
        "female": Gender.Female
    }

    species_mapper = {
        "cat": Species.Cat,
        "dog": Species.Dog,
        "monkey": Species.Monkey,
        "rat": Species.Rat,
        "unknown": Species.Unknown
    }

    def parse(self, value: dict):
        name = value["name"]
        gender = self.gender_mapper[value["gender"]] # можно убрать словарь на самом деле
        species = self.species_mapper[value.get("species", "unknown")] # можно убрать словарь на самом деле
        day, month, year = tuple(map(int, value["birthDate"].split(".")))
        birthDate = date(year, month, day)
        return Pet(name=name, gender=gender, species=species, birthDate=birthDate)