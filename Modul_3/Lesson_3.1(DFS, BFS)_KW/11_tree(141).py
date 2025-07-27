ans = 0


def dfs(v, using, edges):
    global ans
    using[v] = 1
    for i in edges[v]:
        ans += 1
        if using[i] == 0:
            dfs(i, using, edges)


n = int(input())
graph = []
for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)

edges = [[] for _ in range(n)]
using = [0] * n

for i in range(n):
    for j in range(i + 1, n):
        if graph[i][j] == 1:
            edges[i].append(j)
            edges[j].append(i)


dfs(0, using, edges)

if min(using) == 1 and ans // 2 == n - 1:
    print("YES")
else:
    print("NO")
