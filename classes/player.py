class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
        self.chips =100
    
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self, new_cards):
        if type(new_cards) == list:
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards and {self.chips} chips.'
    def hit_or_stand(self, deck):
        while True:
            choice = input("Would you like to hit or stand? Enter 'h' or 's': ")
            if choice.lower() == 'h':
                self.add_cards(deck.deal_one())
                return 'hit'
            elif choice.lower() == 's':
                print("Player stands. Dealer is playing.")
                return 'stand'
            else:
                print("Please enter 'h' or 's' only.")