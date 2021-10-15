inputA = int(input())

for i in range(inputA):
    mList = list(input())
    score = 0
    win_streak = 0
    for OX in mList:
        if OX == 'O':
            win_streak += 1
            score += win_streak
        else:
            win_streak = 0

    print(score)
