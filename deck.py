import random

#Uppgift 1: Klass för kort
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value}{self.suit}"

    def __repr__(self):
        return str(self)


#Uppgift 1: Skapa klass för hela kortleken
class Deck:
    def __init__(self):
        suits = ["♠", "♥", "♣", "♦"] #Lista för korttyper
        values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"] #Lista för kort
        self.cards = [Card(suit, value) for suit in suits for value in values]

    #Uppgift 2: metod som visar alla kort
    def show_all(self):
        for card in self.cards:
            print(card)

    #Uppgift 3: metod som drar ett kort
    def draw(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop(0)   # drar från toppen

    #Uppgift 4: Överkurs: metod för att blanda kortleken
    def shuffle(self):
        random.shuffle(self.cards)


#Exempel på användning
if __name__ == "__main__":
    deck = Deck()
    print("Hela kortleken:")
    deck.show_all()

    print("\nBlandar...")
    deck.shuffle()
    deck.show_all()

    print("\nDrar ett kort:")
    print(deck.draw())

    print("\nAntal kort kvar:", len(deck.cards))
