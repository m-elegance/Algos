n, m = map(int, input().split())
edges = [[] for _ in range(n)]
color = [0] * n
flag = False

def dfs(v, c):
    global flag
    color[v] = c
    for i in edges[v]:
        if color[i] == 0:
            if c == 1:
                new_color = 2
            else:
                new_color = 1
            dfs(i, new_color)
        else:
            if color[i] == color[v]:
                flag = True


for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

for i in range(n):
    if color[i] == 0:
        dfs(i, 1)

if flag:
    print("NO")
else:
    print("YES")