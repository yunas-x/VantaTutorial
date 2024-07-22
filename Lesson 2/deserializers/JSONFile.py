import json
from typing import override

from .protocols.File import File

class JSONFile(File):

    def __init__(self, path) -> None:
        self._path = path

    @property
    def Path(self):
        return self._path
    
    @override
    def load_file(self) -> object:
        with open(self._path, "r") as fp:
            file = json.load(fp)

        return file