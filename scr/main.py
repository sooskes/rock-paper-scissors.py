# ============================================================
# Rock Paper Scissors
#
# Description:
# A console-based Rock Paper Scissors game where the player
# competes against a randomly choosing computer opponent.
# The player can choose how many points are needed to win
# each match.
#
# Features:
# - Custom points needed to win
# - Input validation for the required points
# - Rock, Paper, Scissors input
# - Short commands: r, p, s
# - Random computer choices
# - Player and computer score tracking
# - Round winner detection
# - Match winner detection
# - Option to restart or close the game
# ============================================================

import random
import time
import os

def roundAmountSelector():
    while True:
        roundAmount = input("Points needed to win: ")
        # Check that the input contains only digits before converting it to an integer.
        if not roundAmount.isdigit():
            os.system("cls")
            print("Something went wrong, Please enter a numeric value.")
            continue

        roundAmount = int(roundAmount)

        if roundAmount < 1:
            os.system("cls")
            print("The round amount cannot be under 1 round!")
            continue
        elif roundAmount > 100:
            os.system("cls")
            print("The round amount cannot be over 100 rounds!")
            continue
        os.system("cls")
        return roundAmount

def playerOpSelector():
    while True:
        givenValue = input("choose between(Rock, Paper, Scissors): ")

        givenValue = givenValue.lower()

        # Allow both the full choice and its single-letter shortcut.
        if givenValue != "rock" and givenValue != "paper" and givenValue != "scissors" and givenValue != "r" and givenValue != "p" and givenValue != "s":
            os.system("cls")
            print("Please enter a valid value.")
            continue

        break

    os.system("cls")

    if givenValue == "rock" or givenValue == "r":
        return "rock"
    elif givenValue == "paper" or givenValue == "p":
        return "paper"
    elif givenValue == "scissors" or givenValue == "s":
        return "scissors"

def computerOpSelector():
    # Generate a random number that represents one of the three possible choices.
    opRandomizer = random.randint(0, 2)

    if opRandomizer == 0:
        return "rock"
    elif opRandomizer == 1:
        return "paper"
    elif opRandomizer == 2:
        return "scissors"

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

def showWinner(playerOp, computerOp):
    if playerOp == "rock" and computerOp == "rock":
        print("It's a tie.")
    elif playerOp == "rock" and computerOp == "paper":
        print("You lost the round.")
    elif playerOp == "rock" and computerOp == "scissors":
        print("You won the round.")
    elif playerOp == "paper" and computerOp == "rock":
        print("You won the round.")
    elif playerOp == "paper" and computerOp == "paper":
        print("It's a tie.")
    elif playerOp == "paper" and computerOp == "scissors":
        print("You lost the round.")
    elif playerOp == "scissors" and computerOp == "scissors":
        print("It's a tie.")
    elif playerOp == "scissors" and computerOp == "paper":
        print("You won the round.")
    elif playerOp == "scissors" and computerOp == "rock":
        print("You lost the round.")

def continuationPermission():
    while True:
        givenValue = input("Do you wish to continue playing(y/n): ")

        givenValue = givenValue.lower()

        if givenValue != "yes" and givenValue != "y" and givenValue != "n" and givenValue != "no":
            os.system("cls")
            print("Please enter a valid value.")

            continue

        break

    if givenValue == "y" or givenValue == "yes":
        os.system("cls")
        print("Restarting game")

        time.sleep(1)

        return True

    os.system("cls")
    print("Thank you for playing :)\nClosing game.")

    time.sleep(1.2)

    return False

def playerRoundStats(playerPoints, computerPoints):
    # Return one point only when the player wins the round.
    if playerPoints == "rock" and computerPoints == "scissors":
        return 1
    elif playerPoints == "paper" and computerPoints == "rock":
        return 1
    elif playerPoints == "scissors" and computerPoints == "paper":
        return 1

    return 0

def computerRoundStats(playerPoints, computerPoints):
    # Return one point only when the computer wins the round.
    if playerPoints == "scissors" and computerPoints == "rock":
        return 1
    elif playerPoints == "rock" and computerPoints == "paper":
        return 1
    elif playerPoints == "paper" and computerPoints == "scissors":
        return 1

    return 0

def showRoundStats(playerPoints, computerPoints, neededRounds):
    print("PLAYER", playerPoints, '\t', "COMPUTER", computerPoints)
    print("\tFirst to", neededRounds)

def endCheck(neededRounds, playerPoints, computerPoints):
    # Check whether either player has reached the required winning score.
    if playerPoints == neededRounds:
        print("\n\tYOU WON :)")
        return False
    elif computerPoints == neededRounds:
        print("\n\tYOU LOST :(")
        return False
    return True

while True:
    os.system("cls")
    playerPointCounter = 0
    computerPointCounter = 0

    roundAmount = roundAmountSelector()

    while endCheck(roundAmount, playerPointCounter, computerPointCounter):
        player = playerOpSelector()

        computer = computerOpSelector()

        showSelectedOp(player, computer)

        playerPointCounter += playerRoundStats(player, computer)

        computerPointCounter += computerRoundStats(player, computer)

        showWinner(player, computer)

        showRoundStats(playerPointCounter, computerPointCounter, roundAmount)
    if continuationPermission():
        continue

    break
