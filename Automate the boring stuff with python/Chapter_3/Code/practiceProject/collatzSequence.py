import sys


def collatz(number):
    checkNumber = "even" if number % 2 == 0 else "odd"
    if checkNumber == "even":
        return number // 2
    else:
        return 3 * number + 1


def start():
    print("Enter a number: ")


start()
while True:
    try:
        number = int(input())
        result = collatz(number)
        print(result)
    except ValueError:
        print("Invalid value, please try again")
        start()
    except KeyboardInterrupt:
        sys.exit(1)
