import random
import time



def create_deck():
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    faces = ['A', 'K', 'Q', 'J', 10, 9 , 8, 7, 6, 5, 4, 3, 2]

    deck = []
    for suit in suits:
        for face in faces:
            deck.append(str(face)+' of '+suit)
            
    random.shuffle(deck)
    
    return deck


def get_card_value(card):
    if card[0] == 'A':
        card_value = 1
    elif card[0] == 'K':
        card_value = 10
    elif card[0] == 'Q':
        card_value = 10
    elif card[0] == 'J':
        card_value = 10
    else:
        try:
            card_value = int(card[0:2])
        except:
            card_value = int(card[0])
        
    return card_value
    
def draw_card(deck):
    card = deck.pop()
    return card
    
def start_game():
    start = input('Start Game? (y/n): ')
    print ("")
    if start == 'y':
        play_game()
    else:
        exit()
          
def play_game():
    deck = create_deck()
    wallet = 100
    play_again = 'y'
    
    while play_again == 'y':
        print ('Wallet: ', wallet)
        bet = int(input('Enter bet: '))
        print (len(deck))
        if len(deck) < 12:
            deck = create_deck()
            print ("Shuffling Cards...")
            print ("")
            
            
        dc1 = draw_card(deck)
        dc2 = draw_card(deck)
        dc1v = get_card_value(dc1)
        dc2v = get_card_value(dc2)
        dtotal = dc1v + dc2v
        
        c1 = draw_card(deck)
        c2 = draw_card(deck)
        c1v = get_card_value(c1)
        c2v = get_card_value(c2)
        total = c1v + c2v
        
        print ("Dealer Card 1: ", dc1)
        #print ("Dealer Card 2: ", dc2)
        #print ("Dealer Total: ", dtotal)
        print ("")
        
        print ("Card 1: ", c1)
        
        print ("Card 2: ", c2)
        print ("Player Total: ", total)
        print ("")

        
        draw_again = input("Draw again? (y/n): ")
        print ("")
        
        bust = 'n'
        while draw_again == 'y':
            new_card = draw_card(deck)
            nvc = get_card_value(new_card)
            total = total + nvc
            print ("New Player Card: ", new_card)
            print ("New Player Total: ", total)
            print ("")
            if total > 21:
                draw_again = 'n'
                bust = 'y'
            elif total == 21:
                draw_again = 'n'
            else:
                draw_again = input("Draw again? (y/n): ")
                print("")
                
        if bust == 'n' and total != 'y':       
            while dtotal < 16:
                print ("Dealer Card 2: ", dc1)
                
                print ("Dealer Card 2: ", dc2)
                
                print ("Dealer Total: ", dtotal)
                
                new_dc = draw_card(deck)
                dcv = get_card_value(new_dc)
                dtotal = dtotal + dcv
                
                print ("Dealer New Card: ", new_dc)
                print ("Dealer Total: ", dtotal)
                print("")
                print ("")
                
                if dtotal > 21:
                    print ('Dealer Busts!')
                    print ('You Win!')

        if total ==21:
            print ('21 !!!')
            wallet = wallet + bet * 1.5
            print ('You win ', bet*1.5)
            print ('New Wallet Amount: ', wallet)
        if dtotal == total:
            print ("Player Total: ", total)
            print ("Dealer Total: ", dtotal)
            print ('PUSH!')
            print (wallet)
        elif dtotal > total and dtotal <= 21:
            print ("Player Total: ", total)
            print ("Dealer Total: ", dtotal)
            
            print ('Dealer Wins!')
            wallet = wallet - bet
            print ('YouL Lose', bet)
            print ('New Wallet Amount: ', wallet)
        elif total > 21:
            
            print ('BUST!')
            print ('YOU LOSE!', bet)
            wallet = wallet - bet
            print ('New Wallet Amount: ', wallet)
        else:
            print ("Player Total: ", total)
            print ("Dealer Total: ", dtotal)
            
            print ('You Win!', bet)
            wallet = wallet + bet
            print ('New Wallet Amount: ', wallet)
                
        print ("")
        play_again = input('Play Again? (y/n): ')
        print ("")
        
        
start_game()