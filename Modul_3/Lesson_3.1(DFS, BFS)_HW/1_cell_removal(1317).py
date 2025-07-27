def is_board(v, u):
    return 0 <= v < n and 0 <= u < m

def dfs(v, u, used):
    used[v][u] = True
    for i in range(4):
        new_u = u + dx[i]
        new_v = v + dy[i]
        if (is_board(new_v, new_u)):
            if graph[new_v][new_u] == 1 and used[new_v][new_u] == False:
                dfs(new_v, new_u, used)



n, m = map(int, input().split())
used = [[False] * m for _ in range(n)]
graph = [[] * m for _ in range(n)]
for i in range(n):
    a = list(input())
    for j in range(m):
        if a[j] == "#":
            graph[i].append(1)
        else:
            graph[i].append(0)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and used[i][j] == False:
            dfs(i, j, used)
            cnt += 1


print(cnt)



