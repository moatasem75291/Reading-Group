"""
Write a function that takes a list value as an argument
and returns a strings with all items separeted by a comma
and a space, with and inserted before the last item. 
"""


def join_list(lst):
    """
    The lst empty.
    The lst contains only one item.
    The lst contains several items.
    """
    if len(lst) == 0:
        return " "
    elif len(lst) == 1:
        return lst[0]
    else:
        items = ""
        for item in lst:
            if item == lst[-1]:
                items += "and " + item
            else:
                items += item + ", "
        return items


spam = []
print(f"The lst is empty: {join_list(spam)}")
spam = ["apples"]
print(f"The lst contains only one item: {join_list(spam)}")
spam = ["apples", "bananas", "tofu", "cats"]
print(f"The lst contains several items: {join_list(spam)}")
