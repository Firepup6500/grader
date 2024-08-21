import firepup650 as fp

fp.replitCursor = fp.bcolors.REPLIT + "> " + fp.bcolors.RESET

answerKey = []
answer = "0"
answerCount = 0

fp.clear()

while not False:
    answer = fp.replitInput(
        f"Please input the answer to question #{answerCount + 1}, empty answer to submit answer key"
    )
    if not answer:
        break
    answerCount += 1
    answerKey.append(answer)

fp.clear()

while 1:
    right = 0
    for i in range(answerCount):
        answer = fp.replitInput(
            f"Please input the student's answer to question {i + 1}."
        )
        if answer == answerKey[i]:
            right += 1
            print("    That is correct")
        else:
            print("    That is incorrect")
    print(
        f"\nThe student got {right}/{answerCount} correct, with approximately an {round((right/answerCount) * 100, 2)}%.\n"
    )
