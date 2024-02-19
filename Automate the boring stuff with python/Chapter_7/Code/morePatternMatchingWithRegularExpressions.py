# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
#      More Pattern Matching With Regular Expressions      #
#                Grouping with Parentheses                 #
#          Matching Multiple Groups with the Pipe          #
#        Optional Matching with the Question Mark          #
#            Matching Zero or More with the Star           #
#            Matching One or More with the Plus            #
#        Matching Specific Repetitions with Braces         #
# @#$^$^*&*(^&$%^#@#@%$#%$^%&*^*&)(&^&%$^@#%$#%^&*&^(&*%$^)#
import re

#                Grouping with Parentheses                 #

phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")

match = phoneNumRegex.search("My number is 415-555-4242.")
print(f"Match : {match}")
print(f"Matched Groups : {match.groups()}")
print(f"Matchs and returns the first Group : {match.group(1)}")
print(f"Matchs and returns the second Group : {match.group(2)}")

phoneNumRegex = re.compile(r"\((\d\d\d)\)-(\d\d\d-\d\d\d\d)")
match = phoneNumRegex.search("My number is (415)-555-4242.")
print(f"Match : {match}")
print(f"Matched Groups : {match.groups()}")
print(f"Matchs and returns the first Group : {match.group(1)}")
print(f"Matchs and returns the second Group : {match.group(2)}")

#          Matching Multiple Groups with the Pipe          #
heroRegex = re.compile(r"Batman|Tina Fey")
matches = heroRegex.search("Who's the best superhero? Batman! Who else? Tina Fey!")
print(f"Match : {matches.group()}")


superHeros = ["Superman", "Wonder Woman", "Batman"]
for heroe in superHeros:
    match = heroRegex.search(heroe)
    print(f"Match : {match.group()}") if match else print(f"No match for {heroe}.")


batRegex = re.compile(r"Bat(mobile|man|copter|bat)")
batMatch = batRegex.search("I saw Batman at the movie theater.")
print(f"Match : {batMatch.group()}")


#        Optional Matching with the Question Mark          #
batRegex = re.compile(r"Bat(wo)?man")
batMatch = batRegex.search("The Adventures of Batman")
print(f"Match : {batMatch.group()}")

batMatch = batRegex.search("The Adventures of Batwoman")
print(f"Match: {batMatch.group()}")

phoneRegex = re.compile(r"(\d\d\d-)?\d\d\d-\d\d\d\d")
phoneMatch = phoneRegex.search("My number is 415-555-4242")
print(f"Match : {phoneMatch.group()}")

phoneMatch = phoneRegex.search("My number is 555-4242")
print(f"Match : {phoneMatch.group()}")


#            Matching Zero or More with the Star           #
batRegex = re.compile(r"Bat(wo)*man")
mo1 = batRegex.search("The Adventures of Batman.")
print(f"Match: {mo1.group()}")

mo2 = batRegex.search("The Adventures of Batwoman.")
print(f"Match: {mo2.group()}")

mo3 = batRegex.search("The Adventures of Batwowowowowowoman.")
print(f"Match: {mo3.group()}")


#            Matching One or More with the Plus            #
batRegex = re.compile(r"Bat(wo)+man")
mo1 = batRegex.search("The Adventures of Batman.")
print(f"Match: {mo1}")  # None

mo2 = batRegex.search("The Adventures of Batwoman.")
print(f"Match: {mo2.group()}")

mo3 = batRegex.search("The Adventures of Batwowowowowowoman.")
print(f"Match: {mo3.group()}")


#        Matching Specific Repetitions with Braces         #
haRegex = re.compile(r"(Ha){3}")
mo1 = haRegex.search("HaHaHa")
print(f"Match: {mo1.group()}")

mo2 = haRegex.search("Ha")
print(f"Match: {mo2}")  # None
