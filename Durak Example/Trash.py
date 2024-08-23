from Hand import Hand
from Card import Card
from random import shuffle

the_hand: Hand = Hand(cards=[])
the_deck: list[Card] = [Card(suit=s, rank=r) 
                                  for s in ["Hearts", "Spades", "Diamonds", "Clubs"]
                                  for r in ["6", "7", "8", "9", "10", "J", "Q", "K", "A"]]

shuffle(the_deck)