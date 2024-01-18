# ROCK, PAPER, AND, SCISSORS
import sys, random

print("ROCK, PAPER, SCISSORS")


Wins, Losses, Ties = 0, 0, 0
while True:
    print(f"{Wins} Wins, {Losses} Losses, {Ties} Ties")
    while True:
        print("Enter your move: (r)ock, (p)aper, (s)cissors, and (q)uit.")
        playerMove = input()
        if playerMove == "q":
            sys.exit()
        elif playerMove == "r" or playerMove == "s" or playerMove == "p":
            break
        else:
            print("Type one of the following: r, p, s, q.")

    # display what the player chose
    if playerMove == "r":
        print("ROCK Versus...")
    elif playerMove == "p":
        print("PAPER Versus...")
    else:
        print("SCISSOR Versus...")

    # display what the computer chose
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = "r"
        print("ROCK")
    elif randomNumber == 2:
        computerMove = "s"
        print("SCISSOR")
    else:
        computerMove = "p"
        print("PAPER")
    # display and record the win/loss/tie
    if playerMove == computerMove:
        print("It's a Tie!")
        Ties += 1
    elif playerMove == "r" and computerMove == "s":
        print("You win!")
        Wins += 1
    elif playerMove == "r" and computerMove == "p":
        print("You lose!")
        Losses += 1
    elif playerMove == "s" and computerMove == "r":
        print("You lose!")
        Losses += 1
    elif playerMove == "s" and computerMove == "p":
        print("You win!")
        Wins += 1
    elif playerMove == "p" and computerMove == "r":
        print("You win!")
        Wins += 1
    elif playerMove == "p" and computerMove == "s":
        print("You lose!")
        Losses += 1
