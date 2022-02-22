N, M = map(int, input().split())

mList = []
is_visited = [False] * N


def solution(depth, N, M):
    if depth == M:
        print(' '.join(map(str, mList)))
        return
    for i in range(len(is_visited)):
        if not is_visited[i]:
            is_visited[i] = True
            mList.append(i + 1)
            solution(depth + 1, N, M)
            is_visited[i] = False
            mList.pop()


solution(0, N, M)
