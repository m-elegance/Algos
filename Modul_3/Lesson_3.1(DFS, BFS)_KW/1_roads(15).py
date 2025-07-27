N = 100
graph = [[0] * N for i in range(N)]

n = int(input())

for i in range(n):
    graph[i] = list(map(int, input().split()))

cnt = 0

for i in range(n):
    for j in range(i + 1, n):
        if graph[i][j] == 1:
            cnt += 1

print(cnt)
