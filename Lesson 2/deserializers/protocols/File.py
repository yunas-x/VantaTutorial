from typing import Protocol

class File(Protocol):
    def load_file(self) -> object:
        ...