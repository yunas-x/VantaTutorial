from pydantic import BaseModel
from typing import Literal

court_cards_rank_value_map = {
    "J": 2,
    "Q": 3,
    "K": 4,
    "A": 11
}

class Card(BaseModel):
    suit: Literal["Hearts", "Spades", "Diamonds", "Clubs"]
    rank: Literal["6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    @property
    def rank_value(self):
        if self.rank in court_cards_rank_value_map:
            return court_cards_rank_value_map[self.rank]
        return int(self.rank)
