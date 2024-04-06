class Hand:
    def __init__(self):
        self.cards = []  # começa com uma lista vazia de cartas
        self.value = 0   # valor total das cartas na mão
        self.aces = 0    # acompanha o número de ases na mão
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        # se o valor da mão for > 21 e ainda houver ases, ajuste o valor do ás para 1
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
    
    def show_some(self):
        print("\n Dealer's Hand: ")
        print("First card hidden!")
        print("\n Player's Hand: ", *self.cards, sep='\n')

    def show_all(self):
        print("\n Dealer's Hand: ", *self.cards, sep='\n')
    def hit(self, deck):
        new_card = deck.deal_one()
        self.add_card(new_card)