num = int(input())
result = 0

for i in range(1, num + 1):
    if i <= 99:
        result += 1
    else:
        mList = list(map(int, str(i)))
        if mList[0] - mList[1] == mList[1] - mList[2]:
            result += 1

print(result)
