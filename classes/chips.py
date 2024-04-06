class Chips:
    def __init__(self, total=100):
        self.total = total
        self.bet = 0
        
    def take_bet(self):
        while True:
            try:
                self.bet = int(input('How many chips would you like to bet? '))
            except:
                print("Sorry! Please provide an integer")
            else:
                if self.bet > self.total:
                    print("Sorry you do not have enought chips! You have: {}".format(self.total))
                else:
                    break
    
    def win_bet(self):
        self.total += self.bet
        
    def lose_bet(self):
        self.total -= self.bet
        
    def player_busts(self):
        print("\n BUST PLAYER")
        self.lose_bet()

    def player_wins(self):
        print("\n PLAYER WINS!")
        self.win_bet()

    def dealer_busts(self):
        print("\n PLAYER WINS! DEALER BUSTED!")
        self.win_bet()

    def dealer_wins(self):
        print("\n DEALER WINS!")
        self.lose_bet()
    
    def push(self):
        print("\n Dealer and Player tie! PUSH")
    
    def play_again(self):
        return input("Would you like to play another hand? (y/n) ").lower().startswith('y')
