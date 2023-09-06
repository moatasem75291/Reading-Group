"""
The birthday paradox says that the probability that two people in a room
will have the same birthday is more than half, provided n, the number of
people in the room, is more than 23. This property is not really a paradox,
but many people find it surprising. Design a Python program that can test
this paradox by a series of experiments on randomly generated birthdays,
which test this paradox for n = 5,10,15,20, . . . ,100.
"""
import random


def has_shared_birthday(birthdays):
    return len(birthdays) != len(set(birthdays))


def birthday_experiment(n, total_experiments):
    shared_birthday_count = 0
    for _ in range(total_experiments):
        birthdays = [random.randint(1, 365) for _ in range(n)]
        if has_shared_birthday(birthdays):
            shared_birthday_count += 1
    return shared_birthday_count / total_experiments


def main():
    total_experiments = 10000
    for n in range(5, 101, 5):
        probability = birthday_experiment(n, total_experiments)
        print(f"For n = {n}, Probability of shared birthday: {probability:.4f}")


if __name__ == "__main__":
    main()
