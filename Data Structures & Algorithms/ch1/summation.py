import collections


def summation(values):
    # check if Iterable or not.
    if not isinstance(values, collections.Iterable):
        raise TypeError("Your parameter is not Iterable.")
    total = 0
    for v in values:
        # check for each element if is number or not.
        if not isinstance(int(v), (int, float)):
            raise TypeError(f"elements, must be numbers.")
        total += int(v)
    return total