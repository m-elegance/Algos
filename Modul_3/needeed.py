n, m = map(int, input().split())
edges = [[] for i in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

color = [None] * n
ans = []


def dfs(v, color, edges):
    color[v] = 1
    global ans
    for i in edges[v]:
        if color[i] == 1:
            continue
        if color[i] is None:
            dfs(i, color, edges)
            ans.append([v, i])


for i in range(n):
    if color[i] is None:
        dfs(i, color, edges)

ans = ans[::-1]
for arr in ans:
    print(arr[0] + 1, arr[1] + 1)
