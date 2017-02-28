#!/usr/bin/python

import random
import scrapy

playing = False

class Player(object):

    def __init__(self,initial_amount=100):
        self.amount = initial_amount

    def check_money(self):
        return self.amount

    def add_money(self,amount):
        self.amount += amount

    def subtract_money(self,amount):
        self.amount -= amount


class Dealer(object):

    def __init__(self):
        print ("Dealer")


class Deck(object):


    suits = ('H','D','C','S')
    ranking = ('A','2','3','4','5','6','7','8','9','J','K','Q')
    card_val = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'J':10,'K':10,'Q':10}

    def __init__(self):
        print ("Deck")


    def shuffle_deck(self):
        print ("Deck Shuffle")

    def random_card(self):
        print ("Sharing Random suit: "+ random.choice(self.suits )+random.choice(self.ranking))
        

class Hand():
    def __init__(self):
        print ("Hand")

def check_winner(player,deck):
    print ("Winner")


def myblackjack_game():

    while (True):
        try:
            money = int(raw_input("Please enter the money for the player1::"))
        except:
            print ("Please enter numeric value")
            continue
        else:
            print ("Player1 will play with initial money:",money)
            break

    player1 = Player(money);
    print ("The current money I have is: {}"  .format(player1.check_money()))

    dec = Deck()

    dec.random_card()




def main():
    myblackjack_game()


if __name__ == "__main__":
    main()
