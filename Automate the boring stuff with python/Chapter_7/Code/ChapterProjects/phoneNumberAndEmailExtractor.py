#! python3
# phoneNumberAndEmailExtractor.py - Finds phone numbers and email addresses on the clipboard.

"""
Say you have the boring task of finding every phone number and email address in a long web page or document.
If you manually scroll through the page, you might end up searching for a long time.
But if you had a program that could search the text in your clipboard for phone numbers and email addresses,
you could simply press CTRL-A to select all the text, press CTRL-C to copy it to the clipboard,
and then run your program.
It could replace the text on the clipboard with just the phone numbers and email addresses it finds.

- The phone number and email address extractor will need to do the following:
    - Use the pyperclip module to copy and paste strings.
    - Create two regexes, one for matching phone numbers and the other for matching email addresses.
    - Find all matches, not just the first match, of both regexes.
    - Neatly format the matched strings into a single string to paste.


"""

import pyperclip, re


# STEP 1: Create regex for matching phone numbers.
phoneRegex = re.compile(
    r"""(
    (\d{3} | \(\d{3}\))?               # area code
    (\.|\-|\s)?                        # separator
    (\d{3})                            # first 3 digit
    (\.|\-|\s)?                        # separator
    (\d{4})                            # last 4 digit
    (\s*(ext|x|ext.)\s*(\d{2,5}))?     # extension

)""",
    re.VERBOSE,
)


# STEP 2: Create regex for matching email addresses.
emailRegex = re.compile(
    r"""(
    [a-zA-Z0-9._%+-]+      # user name
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something

)""",
    re.VERBOSE,
)


# STEP 3: Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    phoneName = "-".join([groups[1], groups[3], groups[5]])
    if groups[8] != "":
        phoneName += " x" + groups[8]
    matches.append(phoneName)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# STEP 4: Join the Matches into a string for the clipboard.
if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied to clipboard:")
    print("\n".join(matches))
else:
    print("No phone numbers or email addresses found.")


"""
Test cases:
    - Test Case 1: Valid Phone Number and Email
        - Input: "John Doe's phone number is (555) 123-4567 and his email is john.doe@example.com."
        - Expected Output:
            - Phone Number: (555) 123-4567
            - Email Address: john.doe@example.com

    - Test Case 2: Multiple Phone Numbers and Emails
        - Input: "Contact us at (555) 123-4567 or (555) 987-6543. Email support@example.com or info@example.org."
        - Expected Output:
            - Phone Numbers: (555) 123-4567, (555) 987-6543
            - Email Addresses: support@example.com, info@example.org

    - Test Case 3: No Phone Numbers or Emails
        - Input: "This is a random text without any phone numbers or email addresses."
        - Expected Output: No phone numbers or email addresses found.

    - Test Case 4: Email without Phone Number
        - Input: "Please contact us via email at contact@example.com."
        - Expected Output:
            - Email Address: contact@example.com
            - No phone number found.

    - Test Case 5: Phone Number without Email
        - Input: "Call us at (123) 456-7890 for assistance."
        - Expected Output:
            - Phone Number: (123) 456-7890
            - No email address found.

    - Test Case 6: Clipboard with Mixed Content
        - Input: "John Doe's phone number is (555) 123-4567 and his email is john.doe@example.com. Contact support at support@example.org."
        - Expected Output:
            - Phone Number: (555) 123-4567
            - Email Addresses: john.doe@example.com, support@example.org

    - Test Case 7: Phone Number and Email in Different Formats
        - Input: "Phone: 123-456-7890, Email: contact_me@example.org"
        - Expected Output:
            - Phone Number: 123-456-7890
            - Email Address: contact_me@example.org

    - Test Case 8: Special Characters in Email
        - Input: "Contact us at user.name123@example-domain.com for assistance."
        - Expected Output:
            - Email Address: user.name123@example-domain.com
            - No phone number found.

"""
