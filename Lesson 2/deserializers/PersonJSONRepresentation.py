from .protocols.Parser import Parser

from ..Person import Person
from .JSONFile import JSONFile

class PersonJSONRepresentation():

    def __init__(self, file: JSONFile) -> None:
        self._file = file

    def person(self, person_parser: Parser) -> Person:
        json = self._file.load_file()
        return person_parser.parse(json)