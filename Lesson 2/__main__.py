from .deserializers.JSONFile import JSONFile
from .deserializers.PersonJSONParser import PersonJSONParser
from .deserializers.PetJSONParser import PetJSONParser
from .deserializers.PersonJSONRepresentation import PersonJSONRepresentation

import pathlib

def main():
    path = pathlib.Path("./OOP/example.json")
    file = JSONFile(path)
    person = PersonJSONRepresentation(file).person(PersonJSONParser(PetJSONParser()))

    print(person)
    print(person.Pets)
    print(person.Pets.average_age())
    print(person.Pets.dominating_gender())

if __name__ == "__main__":
    main()
