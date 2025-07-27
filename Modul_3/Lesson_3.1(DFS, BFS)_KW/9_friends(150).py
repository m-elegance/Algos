n, s = map(int, input().split())

using = [False] * n
ans = 0

def dfs(v, using, edges):
    global ans 
    ans += 1
    using[v] = True
    for i in edges[v]:
        if using[i] == False:
            dfs(i, using, edges)


graph = []
for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)

edges = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            edges[i].append(j)

dfs(s - 1, using, edges)
print(ans - 1)
