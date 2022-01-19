def solution(array):
    if len(array) <= 1:
        return array

    center = len(array) // 2
    front = solution(array[:center])
    rear = solution(array[center:])

    i, j, k = 0, 0, 0

    while i < len(front) and j < len(rear):
        if front[i] < rear[j]:
            array[k] = front[i]
            i += 1

        else:
            array[k] = rear[k]
            j += 1
        k += 1

    if i == len(front):
        while j < len(rear):
            array[k] = rear[j]
            j += 1
            k += 1
    elif j == len(rear):
        while i < len(front):
            array[k] = front[i]
            i += 1
            k += 1
    return array


N = int(input())
mList = []

for i in range(N):
    mList.append(int(input()))

mList = solution(mList)

for j in mList:
    print(j)
