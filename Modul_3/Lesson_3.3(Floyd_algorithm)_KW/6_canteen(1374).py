from math import inf

n, m = map(int, input().split())
graph = [[inf] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u][v] = w
    graph[v][u] = w

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = inf
for i in range(n):
    temp = max(graph[i])
    if ans > temp:
        ans = temp
        ind = i        

print(ind + 1)

