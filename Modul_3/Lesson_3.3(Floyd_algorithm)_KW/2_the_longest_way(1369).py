n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = graph[0][0]
for i in range(n):
    for j in range(n):
        ans = max(ans, graph[i][j])

print(ans)