#! python
# dateDetection.py - Detects dates in the DD/MM/YYYY format

"""
Write a regular expression that can detect dates in the DD/MM/YYYY format.
Assume that the days range from 01 to 31, the months range from 01 to 12,
and the years range from 1000 to 2999. Note that if the day or month is a single digit,
it’ll have a leading zero.

The regular expression doesn’t have to detect correct days for each month or for leap years;
it will accept nonexistent dates like 31/02/2020 or 31/04/2021.

Then store these strings into variables named day, month, and year,
and write additional code that can detect if it is a valid date. April, June, September,
and November have 30 days, February has 28 days, and the rest of the months have 31 days.
February has 29 days in leap years.
Leap years are every year evenly divisible by 4, except for years that are evenly divisible by 100,
unless the year is also evenly divisible by 400.
Note how this calculation makes it impossible to make a reasonably simple regular expression that can detect a valid date.

"""
import re


def detect_date_format(text):
    """
    Detects dates in the DD/MM/YYYY format using a regular expression.
    Args:
        text: A string that may contain dates.
    Returns:
        A list of strings representing dates in the DD/MM/YYYY format.
    """
    date_regex = re.compile(
        r"""
        (\d{2})/  # Day
        (\d{2})/  # Month
        (\d{4})   # Year
    """,
        re.VERBOSE,
    )
    return date_regex.findall(text)


def is_valid_date(day, month, year):
    """
    Checks if the given day, month, and year form a valid date.
    Args:
        day: An integer representing the day.
        month: An integer representing the month.
        year: An integer representing the year.
    Returns:
        True if the date is valid, False otherwise.
    """
    days_in_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    # Adjust days in February for leap years
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month[2] = 29

    return month in days_in_month and 1 <= day <= days_in_month[month]


def validate_dates_in_text(text):
    """
    Validates dates in the DD/MM/YYYY format within a given text.
    Args:
        text: A string that may contain dates.
    Returns:
        A dictionary where keys are detected dates, and values are True if the date is valid, False otherwise.
    """
    dates = detect_date_format(text)
    result = {}

    for date_str in dates:
        day, month, year = map(int, date_str)
        result[date_str] = is_valid_date(day, month, year)

    return result


text_case_1 = "Today is a valid date: 25/02/2024."
print(validate_dates_in_text(text_case_1))  # {'25/02/2024': True}

text_case_2 = "This is an invalid date: 32/02/2024."
print(validate_dates_in_text(text_case_2))  # {'32/02/2024': False}

text_case_3 = "Another invalid date: 25/13/2024."
print(validate_dates_in_text(text_case_3))  # {'25/13/2024': False}

text_case_5 = "Dates in the text: 25/02/2024, 32/02/2024, 31/04/2021."
print(
    validate_dates_in_text(text_case_5)
)  # {'25/02/2024': True, '32/02/2024': False, '31/04/2021': False}

text_case_6 = "Leap year date: 29/02/2024."
print(validate_dates_in_text(text_case_6))  # {'29/02/2024': True}

text_case_7 = "Single digit date: 05/06/2022."
print(validate_dates_in_text(text_case_7))  # {'05/06/2022': True}

text_case_8 = "Invalid date format: 2024/02/25."
print(validate_dates_in_text(text_case_8))  # {}

text_case_9 = "Valid date with leading zeros: 01/05/2023."
print(validate_dates_in_text(text_case_9))  # {'01/05/2023': True}

text_case_10 = ""
print(validate_dates_in_text(text_case_10))  # {}
