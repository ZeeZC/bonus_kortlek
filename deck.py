#deck.py
#NOTE: Kör programmet i andra filen, deck-test.py!

import random

#Klass för kort
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value}{self.suit}"

    def __repr__(self):
        return str(self)


#Klass för hela kortleken
class Deck:
    def __init__(self):
        self._original_suits = ["♠", "♥", "♣", "♦"]
        self._original_values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        self.reset()

    #Funktion för att bygga upp en ny kortlek
    def reset(self):
        self.cards = [Card(suit, value) for suit in self._original_suits for value in self._original_values]
        self.shuffle()

    #Funktion för att visa alla kort
    def show_all(self):
        for card in self.cards:
            print(card)

    #Funktion för att dra ett kort
    def draw(self):
        if len(self.cards) == 0:
            print("Kortleken är tom! Du måste resetta.")
            return None
        return self.cards.pop(0)

    #Funktion för att blanda kortleken
    def shuffle(self):
        random.shuffle(self.cards)
