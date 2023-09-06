"""
Write a Python program that simulates a handheld calculator. Your program
should process input from the Python console representing buttons
that are “pushed,” and then output the contents of the screen after each operation
is performed. Minimally, your calculator should be able to process
the basic arithmetic operations and a reset/clear operation
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiplay(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    else:
        return a / b


# calculator status
current_input = ""
current_operation = None
result = 0

while True:
    print(f"Screen: {current_input if current_input else result}")

    user_input = input(
        "Enter a number or operator (+, -, *, /, =, C to clear, Q to quit): "
    ).strip()  # Get user input
    if user_input.lower() == "q":
        break
    elif user_input.lower() == "c":  # clear command
        current_input = ""
        current_operation = None
    elif user_input.isdigit() or (
        user_input[0] == "-" and user_input[1:].isdigit()
    ):  # numeric input
        current_input += user_input
    elif user_input == ".":  # decimal point
        if "." not in current_input:
            current_input += user_input
    elif user_input in ["+", "-", "*", "/"]:  # operator
        if current_operation:  # if there is an operation in progress
            result = current_operation(result, float(current_input))
        else:
            result = float(current_input)
        current_input = ""
        if user_input == "+":
            current_operation = add
        elif user_input == "-":
            current_operation = subtract
        elif user_input == "*":
            current_operation = multiplay
        elif user_input == "/":
            current_operation = divide
    elif user_input == "=":  # equals
        if current_operation:
            result = current_operation(result, float(current_input))
            current_input = ""
            current_operation = None


print(f"Final Result: {result}")  # final result and exit
