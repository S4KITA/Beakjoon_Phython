N, K = map(int, input())
listBackpack = []

for n in range(N):
    W, V = map(int, input().split())
    listBackpack.append([W, V])

for k in range(K):
    listValue = []
