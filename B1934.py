import math

T = int(input())


def solution(x, y):
    return x * y // math.gcd(x, y)


for t in range(T):
    A, B = map(int, input().split())
    print(solution(A, B))
