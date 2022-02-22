import sys
import collections

N = int(sys.stdin.readline())
listN = list(sys.stdin.readline().split())

M = int(sys.stdin.readline())
listM = list(sys.stdin.readline().split())

listCount = collections.Counter(listN)

for i in range(len(listM)):
    if listM[i] in listCount:
        print(listCount[listM[i]], end=' ')
    else:
        print(0, end=' ')
