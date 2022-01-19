N = int(input())
mList = []

for n in range(N):
    age, name = map(str, input().split())
    age = int(age)
    mList.append((age, name))

mList.sort(key=lambda x: x[0])

for i in mList:
    print(i[0], i[1])
