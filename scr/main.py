# ==========================================================
# Project: Rock Paper Scissors Game
# Description:
# A simple command-line Rock Paper Scissors game built with Python.
# The player competes against the computer and tries to win rounds.
#
# Features:
# - Player vs Computer gameplay
# - Random computer move selection
# - Input validation system
# - Score tracking for player and computer
# - Replay option after each round
# - Function-based program structure
#
# Language: Python
# ==========================================================


import random
import time


# Gets player's choice and checks if the input is valid
def playerOpSelector():
    while True:
        givenValue = input("choose between(Rock, Paper, Scissors): ")

        givenValue = givenValue.lower()

        # Allows both full names and short versions (r, p, s)
        if givenValue != "rock" and givenValue != "paper" and givenValue != "scissors" and givenValue != "r" and givenValue != "p" and givenValue != "s":
            print("Please enter a valid value.")
            continue

        break

    # Converts player's input into a standard format
    if givenValue == "rock" or givenValue == "r":
        return "rock"
    elif givenValue == "paper" or givenValue == "p":
        return "paper"
    elif givenValue == "scissors" or givenValue == "s":
        return "scissors"


# Randomly chooses the computer's move
def computerOpSelector():
    opRandomizer = random.randint(0, 2)

    if opRandomizer == 0:
        return "rock"
    elif opRandomizer == 1:
        return "paper"
    elif opRandomizer == 2:
        return "scissors"


# Displays the choices made by player and computer
def showSelectedOp(playerOp, computerOp):

    if playerOp == "rock" or playerOp == "r":
        print("You chose Rock")
    elif playerOp == "paper" or playerOp == "p":
        print("You chose Paper")
    elif playerOp == "scissors" or playerOp == "s":
        print("You chose Scissors")

    if computerOp == "rock":
        print("Computer chose Rock")
    elif computerOp == "paper":
        print("Computer chose Paper")
    elif computerOp == "scissors":
        print("Computer chose Scissors")


# Checks the result of the round and shows the winner
def showWinner(playerOp, computerOp):

    if playerOp == "rock" and computerOp == "rock":
        print("it's a tie.")
    elif playerOp == "rock" and computerOp == "paper":
        print("YOU LOST :(")
    elif playerOp == "rock" and computerOp == "scissors":
        print("YOU WON :)")
    elif playerOp == "paper" and computerOp == "rock":
        print("YOU WON :)")
    elif playerOp == "paper" and computerOp == "paper":
        print("it's a tie.")
    elif playerOp == "paper" and computerOp == "scissors":
        print("YOU LOST :(")
    elif playerOp == "scissors" and computerOp == "scissors":
        print("it's a tie.")
    elif playerOp == "scissors" and computerOp == "paper":
        print("YOU WON :)")
    elif playerOp == "scissors" and computerOp == "rock":
        print("YOU LOST :(")


# Asks the player if they want to continue the game
def continuationPermission():

    while True:
        givenValue = input("Do you wish to continue playing(y/n): ")

        givenValue = givenValue.lower()

        # Validates the continue/exit input
        if givenValue != "yes" and givenValue != "y" and givenValue != "n" and givenValue != "no":
            print("Please enter a valid value.")
            continue

        break

    if givenValue == "y" or givenValue == "yes":
        print("Restarting game")
        time.sleep(1)
        return True

    print("Thank you for playing :)\nClosing game.")
    time.sleep(1.2)

    return False


# Calculates player's score after each round
def playerRoundStats(playerPoints, computerPoints):

    if playerPoints == "rock" and computerPoints == "scissors":
        return 1
    elif playerPoints == "paper" and computerPoints == "rock":
        return 1
    elif playerPoints == "scissors" and computerPoints == "paper":
        return 1

    return 0


# Calculates computer's score after each round
def computerRoundStats(playerPoints, computerPoints):

    if playerPoints == "scissors" and computerPoints == "rock":
        return 1
    elif playerPoints == "rock" and computerPoints == "paper":
        return 1
    elif playerPoints == "paper" and computerPoints == "scissors":
        return 1

    return 0


# Shows current game score
def showRoundStats(playerPoints, computerPoints):
    print("PLAYER", playerPoints, '\t', "COMPUTER", computerPoints)


# Initial scores
playerPointCounter = 0
computerPointCounter = 0


# Main game loop
# Runs until the player chooses to exit
while True:

    # Select player and computer moves
    player = playerOpSelector()

    computer = computerOpSelector()


    # Display moves and decide winner
    showSelectedOp(player, computer)

    showWinner(player, computer)


    # Update scores
    playerPointCounter += playerRoundStats(player, computer)

    computerPointCounter += computerRoundStats(player, computer)


    # Display current score
    showRoundStats(playerPointCounter, computerPointCounter)


    # Continue playing or close the game
    if continuationPermission():
        continue

    break
