# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import math
import random

def name_to_number(name):
    if name == 'rock':
        number = 0
    elif name == 'Spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name == 'lizard':
        number = 3
    elif name == 'scissors':
        number = 4
    else:
        print('error')
    return number


def number_to_name(number):
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        print('error')
    return name


def rpsls(player_choice):

    # print a blank line to separate consecutive games
    print("\n")

    # print out the message for the player's choice
    print("Player chooses  %s" % (player_choice))

    # convert the player's choice to player_number using the function name_to_number()
    player_numb = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_numb = random.randrange(0,4)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_numb)

    # print out the message for computer's choice
    print("Computer chooses  %s" % (comp_choice))

    # compute difference of comp_number and player_number modulo five
    dif_player_comp = (comp_numb - player_numb) % 5
    # use if/elif/else to determine winner, print winner message
    if dif_player_comp == 1:
        winner = comp_choice
        print("Computer's choice %s Wins!" % (winner))
    elif dif_player_comp == 2:
        winner = comp_choice
        print("Computer's choice %s  Wins!" % (winner))
    elif dif_player_comp == 3:
        winner = player_choice
        print("Player's Choice  %s Wins!" % (winner))
    elif dif_player_comp == 4:
        winner = player_choice
        print("Player's Choice  %s Wins!" % (winner))
    elif comp_choice == player_choice:
        winner = player_choice
        print("Tie, both players picked %s! Try playing again." % (player_choice))
    else:
        print("Error, try again!")




# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")