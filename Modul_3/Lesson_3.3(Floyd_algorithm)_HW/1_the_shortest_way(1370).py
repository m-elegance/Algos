from math import inf
n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = inf
flag = 0

for i in range(n):
    if (graph[i][i] < 0):
        flag = -1 
    for j in range(n):
        if i != j:
            ans = min(ans, graph[i][j])

if flag == -1 or ans == inf:
    print(flag)
else:
    print(ans)