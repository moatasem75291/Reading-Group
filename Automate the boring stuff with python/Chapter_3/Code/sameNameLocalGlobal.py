def spam():
    global eggs
    eggs = "sapm"


def bacon():
    eggs = "bacon"


def ham():
    print(eggs)


eggs = 324
spam()
print(eggs)
