"""
Write a program to find out how often a streak of six
heads or a streak of six tails comes up in a randomly
generated list of heads and tails. Your program breaks
up the experiment into two parts: the first part generates
a list of randomly selected 'heads' and 'tails' values,
and the second part checks if there is a streak in it.
Put all of this code in a loop that repeats the experiment
10,000 times so we can find out what percentage of the coin
flips contains a streak of six heads or tails in a row.
As a hint, the function call random.randint(0, 1) will
return a 0 value 50% of the time and a 1 value the other
50% of the time.
"""
import random

numberOfStreaks = 0
streak = 0
coinFlips = []

# First part of the experiment - generate a list of heads/tails
for experimentNumber in range(10000):
    for flip in range(100):
        coinFlips.append(random.choice([0, 1]))  # Use random.choice for heads or tails
        # Checking for a streak (if one exists)
        if coinFlips[flip] == coinFlips[flip - 1]:
            streak += 1
        else:
            streak = 0
        if streak == 6:
            numberOfStreaks += 1
            streak = 0
    # print(coinFlips)
    coinFlips = []

print(f"Chance of streak: {((numberOfStreaks / 10000) * 100):0.2f}%")
