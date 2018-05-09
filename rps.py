#!/bin/python

from random import choice

options = ["rock", "paper", "scizors"]
player1 = choice(options)
player2 = choice(options)

print "\nPlayer 1: %s " %player1 + " - Player 2: %s " %player2

    #player1 wins rock - scizors
    #player1 wins scizors - paper
    #player1 wins paper - rock

def evaluate (player1, player2) :
    if player1 == player2 :
        return "DRAW!!!"
    elif player1 == "rock" and player2 == "scizors" or player1 == "scizors" and player2 == "paper" or player1 == "paper" and player2 == "rock" :
        return "Player 1 WINS!!!"
    else :
        return "Player 2 WINS!!!"

print "\n	%s" %evaluate(player1, player2)

