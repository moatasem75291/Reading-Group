#! Python
# multiplicationQuiz.py - A multiplication quiz program.

import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):

    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = f"# {questionNumber}: {num1} x {num2} = "

    try:
        pyip.inputStr(
            prompt,
            allowRegexes=["^%s$" % (num1 * num2)],
            blockRegexes=[(".*", "Incorrect!")],
            timeout=8,
            limit=3,
        )
    except pyip.TimeoutException:
        print("Out of time!")
    except pyip.RetryLimitException:
        print("Out of tries!")
    else:
        print("Correct!")
        correctAnswers += 1

    time.sleep(1)
    print("\n\n--- Quiz Results ---")
    print(f"{correctAnswers} / {numberOfQuestions} correct\n")

print(f"\nYou got {correctAnswers} / {numberOfQuestions} correct!")
