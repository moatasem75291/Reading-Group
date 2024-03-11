#! Python
# sandwitchMaker.py - A simple program to ask the user for their sandwitch preferences.

import pyinputplus as pyip
import time


def sandwitchMaker():
    print("Welcome to the the Sandwitch maker.")
    print("Please enter your sandwitch preferences from this menu.")

    print(" Sandwitch maker ".center(50, "#"))
    prompt = "Bread Type: \n"
    breadType = pyip.inputMenu(["wheat", "white", "sourdough"], prompt=prompt)

    prompt = "Protein Type: \n"
    proteinType = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"], prompt=prompt)

    prompt = "Do you want cheese on your sandwitch?(yes/no)\n"
    withCheese = pyip.inputYesNo(prompt=prompt)

    if withCheese == "yes":

        prompt = "Cheese Type: \n"
        cheeseType = pyip.inputMenu(["cheddar", "swiss", "mozzarella"], prompt=prompt)
    else:
        cheeseType = ""

    print("Please wait while we prepare your sandwitch.")
    time.sleep(2)
    print(
        "\nYour {} sandwitch with {} and {} cheese is ready.".format(
            breadType, proteinType, cheeseType
        )
    )


sandwitchMaker()
