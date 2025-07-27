n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] != -1 and graph[k][j] != -1:
                if graph[i][j] == -1:
                    graph[i][j] = graph[i][k] + graph[k][j]
                else:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])    
                     
ans = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] != -1:
            ans = max(ans, graph[i][j])
print(ans) 





