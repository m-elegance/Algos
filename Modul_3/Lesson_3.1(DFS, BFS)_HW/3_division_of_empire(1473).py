def dfs(v, used, edges):
    global ans
    ans.append(v + 1)
    used[v] = True
    for i in edges[v]:
        if used[i] == False:
            used[v] = True
            dfs(i, used, edges)
                

n, m = map(int, input().split())
edges = [[] for _ in range(n)]

for i in range(m):
    v, u = map(int, input().split())
    v -= 1
    u -= 1
    edges[v].append(u)
    edges[u].append(v)

k = int(input())
capitals = list(map(int,input().split()))
for i in range(k):
    capitals[i] -= 1



used = [False] * n
for i in capitals:
    used[i] = True
    
cnt = 0
for i in capitals:
    ans = []
    dfs(i, used, edges)
    print(len(ans))
    print(*ans)





