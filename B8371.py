N = int(input())

listAnswer = input()
listStudent = input()

count = 0

for n in range(N):
    if listAnswer[n] != listStudent[n]:
        count += 1

print(count)
