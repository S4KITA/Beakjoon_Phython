def solution(num):
    if num <= 1:
        return num
    return solution(num - 1) + solution(num - 2)

N = int(input())
print(solution(N))