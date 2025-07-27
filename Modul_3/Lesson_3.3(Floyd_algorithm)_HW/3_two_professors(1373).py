from math import inf

n, m = map(int, input().split())

graph = [[inf] * n for _ in range(n)]
for i in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u][v] = w
    graph[v][u] = w

for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


ans = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] != inf:
            ans = max(ans, graph[i][j])


print(ans)
