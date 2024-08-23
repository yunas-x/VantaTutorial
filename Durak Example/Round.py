from pydantic import BaseModel
from Pair import Pair

class Round(BaseModel):
    attacking_player_id: int
    pairs: list[Pair]
    