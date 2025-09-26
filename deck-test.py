#deck-test.py
#Kör programmet i denna fil!
from deck import Deck

#Meny för kortleken
def meny():
    deck = Deck()  #Startar med en blandad kortlek

    while True:
        print("\n--- MENY ---")
        print("1. Dra ett kort")
        print("2. Resetta kortleken")
        print("3. Kort & Antal kvar")
        print("4. Avsluta")

        val = input("Välj ett alternativ (1-4): ")

        if val == "1":
            kort = deck.draw() #Kallar draw metoden och drar ett kort
            if kort:
                print(f"Du drog: {kort}")
                print(f"Antal kort kvar: {len(deck.cards)}")
            
        elif val == "2":
            deck.reset() #Kallar reset metoden för att återställa leken
            print("Kortleken har blivit resettad och blandad.")
        
        elif val == "3":
            print(f"Antal kort kvar i leken: {len(deck.cards)}")
            print("Korten som finns kvar:")
            for kort in deck.cards: #Visar nuvarande kort kvar
                print(kort, end=" ")
            print()
        
        elif val == "4":
            print("Avslutar programmet.")
            break
        else:
            print("Fel val, försök igen.")

if __name__ == "__main__":
    meny()
