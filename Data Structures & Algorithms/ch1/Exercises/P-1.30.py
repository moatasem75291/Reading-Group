#  My Solution
number = int(input("Enter a number greater than two: "))
if number <= 2:
    raise ValueError("Enter a number greater than two. ")


def processing(num):
    for i in range(num):
        num /= 2
        if num <= 2:
            return i+1


print(processing(number))


# GPT Solution
number = int(input("Enter a number greater than two: "))


def processing(num):
    if num <= 2:
        return "Input must be greater than 2"

    count = 0
    while num >= 2:
        num /= 2
        count += 1

    return count


result = processing(number)
print(result)

