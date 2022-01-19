def solution(num):
    result = 1
    if num > 0:
        result = num * solution(num - 1)
    return result


N = int(input())
print(solution(N))
