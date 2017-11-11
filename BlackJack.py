class Player(object):

    def __init__(self,bankroll,player_score,dealer_score):
        self.bankroll = bankroll
        self.player_score = player_score
        self.dealer_score = dealer_score

    def get_bankroll(self):
        print self.bankroll
        return self.bankroll

    def bet_money(self,bet):
        self.bankroll -= (int(bet))
        return self.bankroll

    def add_money(self,winings):
        self.bankroll += winings
        return self.bankroll

    def player_move(self):
        move = raw_input("Hit or Stand?")
        return move

    def add_score_player(self,card):
        value = card[:1]

        if value == 'A':
            self.player_score += 1

        if value == '2':
            self.player_score += 2

        if value == '3':
            self.player_score += 3

        if value == '4':
            self.player_score += 4

        if value == '5':
            self.player_score += 5

        if value == '6':
            self.player_score += 6

        if value == '7':
            self.player_score += 7

        if value == '8':
            self.player_score += 8

        if value == '9':
            self.player_score += 9

        if value == '1':
            self.player_score += 10

        if value == 'J':
            self.player_score += 11

        if value == 'Q':
            self.player_score += 12

        if value == 'K':
            self.player_score += 13

        return self.player_score

    def add_score_dealer(self,card):
        value = card[:1]

        if value == 'A':
            self.dealer_score += 1

        if value == '2':
            self.dealer_score += 2

        if value == '3':
            self.dealer_score += 3

        if value == '4':
            self.dealer_score += 4

        if value == '5':
            self.dealer_score += 5

        if value == '6':
            self.dealer_score += 6

        if value == '7':
            self.dealer_score += 7

        if value == '8':
            self.dealer_score += 8

        if value == '9':
            self.dealer_score += 9

        if value == '1':
            self.dealer_score += 10

        if value == 'J':
            self.dealer_score += 11

        if value == 'Q':
            self.dealer_score += 12

        if value == 'K':
            self.dealer_score += 13

        return self.dealer_score

import random


class Deck (object):
    suit = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    usedCards = []


    def draw_card(self):
        self.SUIT = random.choice((Deck.suit))
        self.VALUE = random.choice(Deck.faces)
        self.CARD = self.VALUE + '-' + self.SUIT

        if any(self.CARD in item for item in Deck.usedCards):
            return draw_card

        else:
            Deck.usedCards.append(self.CARD)

        print self.CARD


import random

d = Deck() #TODO put into one class
p = Player(100,0,0)

print '---Starting Game---'
print 'Your card is:',
d.draw_card()
player_score = p.add_score_player(d.CARD)
print "The dealer's card is: ",
d.draw_card()
dealer_score = p.add_score_dealer(d.CARD)

print '\nYour Score:',player_score
print "Dealer's score",dealer_score

while player_score < 21:
    move = p.player_move()

    if move == 'Hit':
        if p.get_bankroll() == 100:
            print '\nCurrent funds:',
            p.get_bankroll()
            bet = raw_input('How much will you bet?')
            p.bet_money(bet)
        print '----------------------------------------------------------'
        print 'You drew: ',
        d.draw_card()
        player_score = p.add_score_player(d.CARD)

        print '\nYour Score:',player_score
        print "Dealer's score",dealer_score

    #Dealer's turn
    if dealer_score < 8:
        #Dealer will hit
        print '----------------------------------------------------------'
        print "The dealer's card is: ",
        d.draw_card()
        dealer_score = p.add_score_dealer(d.CARD)

        print '\nYour Score:',player_score
        print "Dealer's score",dealer_score
    elif dealer_score < 16:
        dealer_choice = random.choice([True, False])
        if dealer_choice == True:
            #Dealer will hit
            print "The dealer's card is: ",
            d.draw_card()
            dealer_score = p.add_score_dealer(d.CARD)

            print '\nYour Score:',player_score
            print "Dealer's score",dealer_score

        else:
            #dealer passes
            print 'The dealer stands'
    elif dealer_score > 16:
        #dealer passes
        print 'The dealer stands'




if player_score > 21:
    print 'Ha! You busted!'    
