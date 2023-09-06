"""
Question 1.31
Write a Python program that can “make change.” Your program should
take two numbers as input, one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to design your program so that it returns as
few bills and coins as possible.

Denominations 100, 50, 20, 10, 5, 1, 0.25, 0.1, 0.05, 0.01 
$100 Bill: A one-hundred-dollar bill, often referred to simply as a "hundred,"
$50 Bill: A fifty-dollar bill, known as a "fifty,"
$20 Bill: A twenty-dollar bill, referred to as a "twenty,"
$10 Bill: A ten-dollar bill, called a "ten,"
$5 Bill: A five-dollar bill, known as a "five,"
$1 Bill: A one-dollar bill, often referred to as a "one" or simply a "dollar,"
25 Cents (Quarter): A quarter is a coin worth 25 cents
10 Cents (Dime): A dime is a coin worth 10 cents.
5 Cents (Nickel): A nickel is a coin worth 5 cents.
1 Cent (Penny): A penny is the smallest denomination of U.S. currency, worth 1 cent.
"""

monetary_amount_charged, monetary_amount_given = int(
    input("Enter monetary amount charged: ")
), int(input("Enter monetary amount given: "))


def make_change(monetary_amount_charged, monetary_amount_given):
    change = monetary_amount_charged - monetary_amount_given
    denominations = {
        "100-dollar bills": 100,
        "50-dollar bills": 50,
        "20-dollar bills": 20,
        "10-dollar bills": 10,
        "5-dollar bills": 5,
        "1-dollar bills": 1,
        "quarters": 0.25,
        "dimes": 0.1,
        "nickels": 0.05,
        "pennies": 0.01,
    }
    change_dict = {}
    for denomination_name, denomination_value in denominations.items():
        count = int(change / denomination_value)
        if count > 0:
            change_dict[denomination_name] = count
        count -= count * denomination_value
    return change_dict


for denomination_name, count in make_change(
    monetary_amount_charged, monetary_amount_given
).items():
    print(f"Give back {count} {denomination_name}")
