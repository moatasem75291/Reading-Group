"""
Question 1.32
Write a Python program that can simulate a simple calculator, using the
console as the exclusive input and output device. That is, each input to the
calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
can be done on a separate line. After each such input, you should output
to the Python console what would be displayed on your calculator.
"""
while True:
    try:
        number_one = int(input("Enter the 1st number: "))
        number_two = int(input("Enter the 2n number: "))
        operator = input("Enter the operator: ")

        if operator == "+":
            print(number_one + number_two)
        elif operator == "-":
            print(number_one - number_two)
        elif operator == "*":
            print(number_one * number_two)
        elif operator == "/" and number_two != 0:
            print(number_one / number_two)
        else:
            print("Invalid operator or division by zero")
        if input("Do you want to continue? (y/n): ") == "n":
            break
    except:
        raise ValueError("Invalid input")
