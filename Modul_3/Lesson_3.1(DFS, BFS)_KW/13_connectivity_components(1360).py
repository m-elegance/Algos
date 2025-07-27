n, m = map(int, input().split())
using = [False] * n
edges = [[] for _ in range(n)]


def dfs(v, components):
    components.append(v + 1)
    using[v] = True
    for i in edges[v]:
        if using[i] == False:
            dfs(i, components)


for _ in range(m):
    v, u = map(int, input().split())
    v -= 1
    u -= 1
    edges[v].append(u)
    edges[u].append(v)

cnt = 0
ans = []
for i in range(n):
    if using[i] == False:
        components = []
        dfs(i, components)

        cnt += 1
        ans.append(components)

print(cnt)
for i in range(cnt):
    print(len(ans[i]))
    print(*ans[i])
