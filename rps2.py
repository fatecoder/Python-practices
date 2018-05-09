#!/bin/python

from random import choice

options = ["rock", "paper", "scissors"]

play = { options[0]:"scissors",
         options[2]:"paper",
         options[1]:"rock" }

player1 = choice(options)
player2 = choice(options)

print "\nPlayer 1: %s " %player1 + " - Player 2: %s" %player2

def evaluate(player1, player2) :
    if player1 == player2 :
        return "DRAW!!!"
    elif play[player1] == player2 :
        return "Player 1 WINS!!!"
    else :
        return "Player 2 WINS!!!"

print "\n	%s" %evaluate(player1, player2)
