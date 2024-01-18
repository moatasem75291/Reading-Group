# name = "mary"
# password = input("Enter password: ")
# if name == "mary":
#     print(f"Hello, {name.title()}!")
#     if password == "swordfish":
#         print("Access granted")
#     else:
#         print("wrong password")
#####################################################################################
# name = ""
# flag = ""
# while flag != "q":
#     print("Enter 'q' to Exit, anything to continue")
#     flag = input()
#     if flag == "q":
#         break
#     else:
#         print("Enter your name")
#         name = input()
# print(f"Thanks, {name.title()}!")
#####################################################################################
# # Guess Number
# import random

# secretNumber = random.randint(0, 20)
# print("I am thinking of a number between 1 and 20...")

# for guessesTaken in range(1, 7):
#     print("Take a guess")
#     guessedNumber = int(input())

#     if guessedNumber > secretNumber:
#         print("Your guess is too high")
#     elif guessedNumber < secretNumber:
#         print("Your guess is too low")
#     else:
#         break

# if guessedNumber == secretNumber:
#     print(f"Good job!, you guessed my number in {guessesTaken} gueses!")
# else:
#     print(f"Nope, the number i was thinking of was {secretNumber}.")
#####################################################################################
# # ROCK, PAPER, AND, SCISSORS
# import sys, random

# print("ROCK, PAPER, SCISSORS")


# Wins, Losses, Ties = 0, 0, 0
# while True:
#     print(f"{Wins} Wins, {Losses} Losses, {Ties} Ties")
#     while True:
#         print("Enter your move: (r)ock, (p)aper, (s)cissors, and (q)uit.")
#         playerMove = input()
#         if playerMove == "q":
#             sys.exit()
#         elif playerMove == "r" or playerMove == "s" or playerMove == "p":
#             break
#         else:
#             print("Type one of the following: r, p, s, q.")

#     # display what the player chose
#     if playerMove == "r":
#         print("ROCK Versus...")
#     elif playerMove == "p":
#         print("PAPER Versus...")
#     else:
#         print("SCISSOR Versus...")

#     # display what the computer chose
#     randomNumber = random.randint(1, 3)
#     if randomNumber == 1:
#         computerMove = "r"
#         print("ROCK")
#     elif randomNumber == 2:
#         computerMove = "s"
#         print("SCISSOR")
#     else:
#         computerMove = "p"
#         print("PAPER")
#     # display and record the win/loss/tie
#     if playerMove == computerMove:
#         print("It's a Tie!")
#         Ties += 1
#     elif playerMove == "r" and computerMove == "s":
#         print("You win!")
#         Wins += 1
#     elif playerMove == "r" and computerMove == "p":
#         print("You lose!")
#         Losses += 1
#     elif playerMove == "s" and computerMove == "r":
#         print("You lose!")
#         Losses += 1
#     elif playerMove == "s" and computerMove == "p":
#         print("You win!")
#         Wins += 1
#     elif playerMove == "p" and computerMove == "r":
#         print("You win!")
#         Wins += 1
#     elif playerMove == "p" and computerMove == "s":
#         print("You lose!")
#         Losses += 1
#####################################################################################
# EXERCISES
# # NUMBER 9
# spam = input("Enter 1 or 2 or anything...")
# if spam == "1":
#     print("Hello!")
# elif spam == "2":
#     print("Howdy")
# else:
#     print("Greetings!")
