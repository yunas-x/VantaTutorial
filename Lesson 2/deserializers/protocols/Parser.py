from typing import Any, Protocol

class Parser(Protocol):

    def parse(self, value) -> Any:
        ...