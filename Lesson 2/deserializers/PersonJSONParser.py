from ..Person import Person
from ..collections.Pets import Pets
from .protocols.Parser import Parser
from ..enums.Gender import Gender
from datetime import date

class PersonJSONParser(Parser):
    
    gender_mapper = {
        "male": Gender.Male,
        "female": Gender.Female
    }
        
    def __init__(self, pet_parser: Parser) -> None:
        self._pet_parser = pet_parser

    def parse(self, value):
        name = value["name"]
        gender = self.gender_mapper[value["gender"]]
        day, month, year = tuple(map(int, value["birthDate"].split(".")))
        birthDate = date(year, month, day)
        pets = Pets([self._pet_parser.parse(p) for p in value["pets"]])
        return Person(name=name, gender=gender, birthDate=birthDate, pets=pets)
