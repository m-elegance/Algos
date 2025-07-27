def dfs(v, used, edges):
    used[v] = 1
    for i in edges[v]:
        if used[i] == 0:
            dfs(i, used, edges)

n, k = map(int, input().split())
k -= 1


used = [0] * n
edges = [[] for _ in range(n)]

while True:
    temp = list(map(int, input().split()))
    if len(temp) == 1:
        break

    v = temp[0] - 1
    u = temp[1] - 1
    
    edges[v].append(u)

dfs(k, used, edges)

if min(used) == 0:
    print("No")
else:
    print("Yes")
