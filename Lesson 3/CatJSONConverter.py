from JSONConverter import JSONConverter
from Cat import Cat

import json

class CatJSONConverter(JSONConverter):

    def __init__(self, value: Cat) -> None:
        self.value = value

    def convert(self) -> str:
        return json.dumps(self.value.__dict__, indent=2)
    
## Мы можем друго сделать преобразователь