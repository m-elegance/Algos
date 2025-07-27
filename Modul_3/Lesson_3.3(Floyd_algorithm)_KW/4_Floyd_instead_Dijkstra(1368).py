from math import inf

n, s, f = map(int, input().split())
s -= 1
f -= 1
graph = []
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        if a[j] == -1:
            a[j] = inf
    graph.append(a)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
if graph[s][f] == inf:
    print(-1)
else:
    print(graph[s][f])
