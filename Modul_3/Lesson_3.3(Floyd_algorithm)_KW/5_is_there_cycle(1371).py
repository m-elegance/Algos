
def dfs(v, c):
    global flag
    color[v] = c
    for i in edges[v]:
        if color[i] is None:
            dfs(i, c)
        elif color[i] == c: 
            flag = True
    color[v] = 2




n = int(input())
flag = False
graph = [list(map(int, input().split())) for _ in range(n)]
color = [None] * n

edges = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            edges[i].append(j)


for i in range(n):
    if color[i] is None:
        dfs(i, 1)

if flag:
    print("Yes")
else:
    print("No")





