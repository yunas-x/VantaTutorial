from Card import Card

cards = [Card(suit="Hearts", rank="6"), Card(suit="Hearts", rank="8"), Card(suit="Hearts", rank="J"),
         Card(suit="Spades", rank="6"), Card(suit="Spades", rank="8"), Card(suit="Spades", rank="9")]

class Hand:

    def __init__(self) -> None:
        self.ind = 1

    @property
    def score(self):
        return sum(card.rank_value for card in cards[:self.ind])
    
    def add_card(self):
        self.ind += 1

    @property
    def cards(self):
        return cards[:self.ind].copy()
    
    @property
    def is_game_on(self):
        return self.score < 21
    
    @property
    def is_game_lost(self):
        return self.score > 21
    
    @property
    def is_game_won(self):
        return self.score == 21
    

the_hand: Hand = None