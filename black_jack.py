from classes.deck import Deck
from classes.player import Player
from classes.hand import Hand
from classes.chips import Chips

playing = True
player1 = Player("Player 1")

player_chips =Chips()
print("You have",player1.chips,"chips")

while True:
    print(' ───────────────────────')
    print('┃ WELCOME TO BLACKJACK! ┃')
    print(' ───────────────────────')
    
    
    # Cria e embaralha o baralho, distribui duas cartas para cada jogador
    values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10, "Ace":11}
    deck = Deck(values)
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal_one())
    player_hand.add_card(deck.deal_one())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_one())
    dealer_hand.add_card(deck.deal_one())
    
    # Pede a aposta do jogador
    player_chips.take_bet()
    
    # Mostra as cartas (mas mantém uma carta do dealer oculta)
    player_hand.show_some()
    
    while playing:
        choice = player1.hit_or_stand(deck)
        if choice == 'stand':
            playing = False
        
        # Se a mão do jogador exceder 21, o jogador perde
        if player_hand.value > 21:
            player_chips.player_busts()
            break
        # Mostra as cartas (mas mantém uma carta do dealer oculta)
        player_hand.show_some()
    
    # Se o jogador não estourar, joga a mão do dealer até atingir 17
    if player_hand.value <= 21:
        while dealer_hand.value < player_hand.value:
            dealer_hand.hit(deck)
            
        # Mostra todas as cartas
        player_hand.show_all()
        
        # Executa diferentes cenários de vitória
        if dealer_hand.value > 21:
            player_chips.dealer_busts()
        elif dealer_hand.value > player_hand.value:
            player_chips.dealer_wins()
        elif dealer_hand.value < player_hand.value:
            player_chips.player_wins()
        else:
            player_chips.push()
            
    # Informa ao jogador o total de fichas
    print("\n Player total chips are at: {}".format(player_chips.total))
    
    # Pergunta se deseja jogar novamente
    if not player_chips.play_again():
        print("\n Thank's for playing BLACKJACK!")
        break
