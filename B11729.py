def solution(n, front, rear):
    if n == 1:
        print(front, rear)
        return
    solution(n - 1, front, 6 - front - rear)
    print(front, rear)
    solution(n - 1, 6 - front - rear, rear)


n = int(input())
print(2 ** n - 1)
solution(n, 1, 3)
