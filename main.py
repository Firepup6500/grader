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
    if len(answer) > 1:
        multi = fp.replitInput("Is this multiple answers? (Y|n)")
        if multi.upper() != "N":
            for i in range(len(answer)):
                answerCount += 1
                answerKey.append(answer[i])
            continue
    answerCount += 1
    answerKey.append(answer)

fp.clear()

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
            if answer == answerKey[i]:
                right += 1
                print(f"    Answer {i + 1} is correct")
            else:
                print(f"    Answer {i + 1} is incorrect")
    except KeyboardInterrupt:
        pass
    print(
        f"\nThe student got {right}/{answerCount} correct, which is approximately {round((right/answerCount) * 100, 2)}%.\n"
    )
