N = int(input())
scoreA, scoreB = 100, 100
for n in range(N):
    A, B = map(int, input().split())
    if A > B:
        scoreB -= A
    elif A < B:
        scoreA -= B
    else:
        pass

print(scoreA)
print(scoreB)
