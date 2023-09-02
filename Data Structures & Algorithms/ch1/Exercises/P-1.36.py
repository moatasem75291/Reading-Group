"""
Write a Python program that inputs a list of words, separated by whitespace,
and outputs how many times each word appears in the list. You
need not worry about efficiency at this point, however, as this topic is
something that will be addressed later in this book.
"""
#  1st solution without removing punctuation
word_list = input("Enter a list of words separated by whitespace: ").split()

word_count = {}
for word in word_list:
    word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f"'{word}': {count} times")


#  2nd solution with removing punctuation

word_list = input("Enter a list of words separated by whitespace: ").split()
word_count = {}

for word in word_list:
    word = word.strip(".,!?()[]{}")
    word = word.lower()

    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print(f"'{word}': {count} times")
