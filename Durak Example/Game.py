from typing import Literal
from pydantic import BaseModel
from Hand import Hand
from Round import Round
from Card import Card

from random import shuffle

class Game(BaseModel):
    hand1: Hand
    hand2: Hand
    trump: Literal["Hearts", "Spades", "Diamonds", "Clubs"]
    rounds: list[Round]

    def __init__(self):
        self._deck: list[Card] = [Card(suit=s, rank=r) 
                                  for s in ["Hearts", "Spades", "Diamonds", "Clubs"]
                                  for r in ["6", "7", "8", "9", "10", "J", "Q", "K", "A"]]
        
        shuffle(self._deck)
        
        

        