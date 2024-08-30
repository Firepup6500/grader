import firepup650 as fp

keys = {"Create new assignment": False}

try:
    from assignments import keys
except:
    with open("assignments.py", "w") as file:
        file.write(f"keys = {keys}")

fp.replitCursor = fp.bcolors.REPLIT + "> " + fp.bcolors.RESET

answerKey = []
answer = "0"
answerCount = 0
key = False
validAnswers = []

if len(keys) > 1:
    key = fp.menu(keys, "Please select an assignment to grade")
fp.clear()
if key:
    answerKey = key["key"]
    answerCount = len(key["key"])
    validAnswers = key["valid"]
else:
    while not False:
        answer = fp.replitInput(
            f"Please input the answer to question #{answerCount + 1}, empty answer to submit answer key"
        ).upper()
        if not answer:
            break
        if len(answer) > 1:
            multi = fp.replitInput("Is this multiple answers? (Y|n)")
            if multi.upper() != "N":
                for i in range(len(answer)):
                    answerCount += 1
                    answerKey.append(answer[i])
                continue
        answerCount += 1
        answerKey.append(answer)
    name = fp.replitInput("Please enter the name of this assignment")
    validAnswers = list(
        fp.replitInput("Please enter the valid answers to this assignment").upper()
    )
    keys[name] = {"key": answerKey, "valid": validAnswers}
    with open("assignments.py", "w") as file:
        file.write(f"keys = {keys}")

fp.clear()

tDigits = 1
tmp = answerCount
while tmp > 10:
    tmp = tmp / 10
    tDigits += 1

while 1:
    right = 0
    try:
        queue = []
        for i in range(answerCount):
            answer = ""
            if not queue:
                answer = fp.replitInput(
                    f"Please input the student's answer to question {i + 1}. ^C at any time to show results immediately."
                ).upper()
            else:
                answer = queue.pop(0)
            if len(answer) > 1:
                multi = fp.replitInput("Is this multiple answers? (Y|n)")
                if multi.upper() != "N":
                    queue = list(answer)
                    answer = queue.pop(0)
            aDigits = 0
            tmp = i + 1
            while tmp > 10:
                aDigits += 1
                tmp = tmp / 10
            digits = tDigits - aDigits
            space = " " * digits
            if answer == answerKey[i]:
                right += 1
                print(f"++    Answer {space}{i + 1} is correct")
            elif answer in validAnswers:
                print(f"--    Answer {space}{i + 1} is incorrect")
            else:
                print(f"??    Answer {space}{i + 1} is N/A")
    except KeyboardInterrupt:
        pass
    print(
        f"\nThe student got {right}/{answerCount} correct, which is approximately {round((right/answerCount) * 100, 2)}%.\n"
    )
