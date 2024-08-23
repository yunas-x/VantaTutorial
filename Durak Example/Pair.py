from pydantic import BaseModel
from typing import Literal, Optional
from Card import Card

class Pair(BaseModel):
    attacking_card: Card
    defending_card: Optional[Card]

    def defend(self, defending_card: Card, trump: Literal["Hearts", "Spades", "Diamonds", "Clubs"]):
        if defending_card.suit == self.attacking_card.suit and defending_card.rank_value > self.attacking_card.rank_value:
            self.defending_card = defending_card
        elif defending_card.suit == trump and self.attacking_card.suit != trump:
            self.defending_card = defending_card

    @property
    def is_defended(self):
        return self.defending_card != None