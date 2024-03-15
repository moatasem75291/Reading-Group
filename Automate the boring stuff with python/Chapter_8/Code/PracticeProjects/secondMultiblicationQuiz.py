#! Python
# secondMultiblicationQuiz.py - Without pyinputplus Module

import time, random

NUMBER_QUESTIONNS = 10
LIMIT = 3
TIME_FOR_ANSWER = 8
SCORE = 0

print(f"Answer the questions")
for i in range(NUMBER_QUESTIONNS):

    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    correct_answer = num1 * num2
    question = f"{num1} * {num2} = "

    for _ in range(LIMIT):

        try:
            time1 = time.time()
            answer = int(input(question))
            time2 = time.time()

            if time2 - time1 > TIME_FOR_ANSWER:
                print("Out of the time :(")
                break
            if answer != correct_answer:
                print("Incorrect answer:(")
            if answer == correct_answer:
                print("Correct answer :)")
                SCORE += 1
                time.sleep(1)
                break
        except ValueError:
            print("Invalid answer, expected integer.")

print(f"Your score is {SCORE} / {NUMBER_QUESTIONNS}")
if SCORE / NUMBER_QUESTIONNS > 0.70:
    print("Congratulations, You passed")
else:
    print("Sorry, you didn't pass")
