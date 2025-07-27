N = 100

edges = [[] for i in range(N)]

n, m = map(int, input().split())

for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

for i in range(n):
    print(len(edges[i]), end=' ')
    


