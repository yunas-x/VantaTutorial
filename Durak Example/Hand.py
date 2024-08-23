from pydantic import BaseModel
from Card import Card

class Hand(BaseModel):
    #player_id: int # 0 or 1
    cards: list[Card]