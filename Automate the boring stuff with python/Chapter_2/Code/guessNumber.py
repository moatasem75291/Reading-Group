# Guess Number
import random

secretNumber = random.randint(0, 20)
print("I am thinking of a number between 1 and 20...")

for guessesTaken in range(1, 7):
    print("Take a guess")
    guessedNumber = int(input())

    if guessedNumber > secretNumber:
        print("Your guess is too high")
    elif guessedNumber < secretNumber:
        print("Your guess is too low")
    else:
        break

if guessedNumber == secretNumber:
    print(f"Good job!, you guessed my number in {guessesTaken} gueses!")
else:
    print(f"Nope, the number i was thinking of was {secretNumber}.")
