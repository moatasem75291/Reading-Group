"""A common punishment for school children is to write out a sentence multiple
times. Write a Python stand-alone program that will write out the
following sentence one hundred times: “I will never spam my friends
again.” Your program should number each of the sentences and it should
make eight different random-looking typos."""

# solution 1

import random

sentence = "I will never spam my friends again."
for i in range(100):
    print(
        f"{i + 1}. {sentence[:random.randint(0, len(sentence ) // 2 - 1)]}{sentence[random.randint(0, len(sentence ) // 2 - 1):]}"
    )

#  solution 2
import random

sentence = "I will never spam my friends again."
repetitions = 100

with open("punishment_sentences.txt", "w") as file:
    for i in range(1, repetitions + 1):
        # Get 8 random indices in the sentence
        typo_indices = random.sample(range(len(sentence)), 8)
        sentence_with_typos = list(sentence)

        for index in typo_indices:
            replacement = chr(random.randint(33, 126))
            sentence_with_typos[index] = replacement

        sentence_numbered = f"{i}. {''.join(sentence_with_typos)}\n"
        file.write(sentence_numbered)

print("Sentences generated and saved to 'punishment_sentences.txt'.")
