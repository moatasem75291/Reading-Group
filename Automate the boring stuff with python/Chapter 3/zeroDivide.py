# def spam(divideBy):
#     return 42 / divideBy
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        return "Error: Invalid argument"


print(spam(10))
print(spam(7))
print(spam(0))
print(spam(1))
