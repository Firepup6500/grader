import firepup650 as fp

fp.replitCursor = fp.bcolors.REPLIT + "> " + fp.bcolors.RESET

answerKey = []
answer = "0"
answerCount = 0

fp.clear()

while not False:
    answer = fp.replitInput(
        f"Please input the answer to question #{answerCount + 1}, empty answer to submit answer key"
    ).upper()
    if not answer:
        break
    answerCount += 1
    answerKey.append(answer)

fp.clear()

while 1:
    right = 0
    try:
        for i in range(answerCount):
            answer = fp.replitInput(
                f"Please input the student's answer to question {i + 1}. ^C at any time to show results immediately."
            ).upper()
            if answer == answerKey[i]:
                right += 1
                print("    That is correct")
            else:
                print("    That is incorrect")
    except KeyboardInterrupt:
        pass
    print(
        f"\nThe student got {right}/{answerCount} correct, which is approximately {round((right/answerCount) * 100, 2)}%.\n"
    )
