#! python3
# multiplicationQuiz.py 
#   - A timed multiplication quiz, implemented using Regexes and pyinputplus.

import pyinputplus as pyip
import random, time

numberOfQuestion = 10
correctAnswer = 0
for questionNum in range(numberOfQuestion):
    # Pick two random numbers:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = '#%s: %s x %s = ' % (questionNum, num1, num2)

    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handled by blockRegexes, with a custom message.
        pyip.inputStr(
            prompt, 
            allowRegexes=[r'^%s$' % (num1 * num2)], 
            blockRegexes=[(r'.*', 'Incorrect!')], 
            timeout=8, 
            limit=3
        )
    except pyip.TimeoutException:
        print('Out of Time!')
    except pyip.RetryLimitException:
        print('Out of Tries!')
    else:
        # This block runs if no exceptions were raised in the try block.
        correctAnswer += 1
        print('Correct!')
    time.sleep(1)               # Brief pause to let the user see the result.

print('Score: %s/%s' % (correctAnswer, numberOfQuestion))

