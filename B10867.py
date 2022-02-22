N = int(input())
mList = list(map(int, input().split()))

for i in sorted(list(set(mList))):
    print(i, end=' ')
