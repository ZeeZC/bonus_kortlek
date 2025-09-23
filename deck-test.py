#skapa en kortlek med hjälp av objektorienterad programmering - använd klasser. Läs mer på classroom - uppgift4.
from deck import Deck, Card

#Skapar en ny kortlek
deck = Deck()

print("Antal kort i ny kortlek:", len(deck.cards))  # ska vara 52

#Testar show_all
print("\nVisar hela kortleken:")
deck.show_all()

#Testar shuffle metoden
print("\nBlandar kortleken...")
deck.shuffle()
deck.show_all()

#Testar draw metoden
print("\nDrar 5 kort:")
for _ in range(5):
    print("Drog:", deck.draw())

print("\nAntal kort kvar efter dragning:", len(deck.cards))
