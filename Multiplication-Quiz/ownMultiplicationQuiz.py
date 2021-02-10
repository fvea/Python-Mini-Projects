#! python3
# ownMultiplicationQuiz.py
#      - A simple timed multiplication quiz using Regex and w/o Pyinputplus.

# LOGIC:
#       1. Set 10 item question.
#       2. Loop through 10 item question.
#       3. Generate two numbers to multiply.
#       4. Get the current time, or time before the question is posted.
#       5. Set initial tries to 0.
#       6. Get the answer from the user.
#       7. If the answer is wrong, increment tries.
#       8. Get current time, or time after the user answered the question correctly.
#       9. If the time taken didn't exceed the allowed time and
#           the user didn't reached max tries, increment total score by 1.
#       10. Proceed to next question.


import re
import random, time


numberOfQuestions = 10
correctAnswer = 0
timeAllowed = 8
maxTries = 3
for questionNum in range(numberOfQuestions):
    # Generate two random numbers to multiply.
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    # Correct answer is handled by answerREGEX
    answerREGEX = re.compile(r'^%s$' % (num1 * num2))

    # Question portion:
    tries = 0
    correct = False
    beforeTIME = time.time()
    while not correct and tries < maxTries:
        print('Q#%s: %s x %s = ' % (questionNum+1, num1, num2))
        answer = input()
        if answerREGEX.search(answer):     # if the answer matched the answerREGEX, then its correct.
            correct = True
        else:
            tries += 1
            print('Incorrect!')
    afterTIME = time.time()

    if (afterTIME-beforeTIME) < timeAllowed and tries < maxTries:
        print('Correct!')
        correctAnswer += 1
    else:
        if (afterTIME-beforeTIME) >= timeAllowed:
            print('Out of time!')
        elif tries == maxTries:
            print('Out of tries!')
    time.sleep(1)                           # Pause for 1-second before the next question.

print('Total Score: %s/%s' % (correctAnswer, numberOfQuestions))



    




