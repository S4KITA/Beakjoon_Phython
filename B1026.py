import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort()

temp = 0

for i in range(0, N):
    temp += A[i] * B[N - i - 1]

print(temp)
