N = 100

n, m = map(int, input().split())

edges = [[] for i in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)


print(n)
for i in range(len(edges)):
    print(len(edges[i]), end=' ')
    edges[i].sort()
    for j in edges[i]:
        print(j + 1, end = ' ')
    print()


