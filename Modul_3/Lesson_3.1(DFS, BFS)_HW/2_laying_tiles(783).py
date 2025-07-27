def is_board(i, j):
    return 0 <= i < n and 0 <= j < n


def dtf(i, j, using):
    using[i][j] = True
    for k in range(4):
        new_i = i + dy[k]
        new_j = j + dx[k]
        if is_board(new_i, new_j) and using[new_i][new_j] == False:
            if graph[new_i][new_j] != graph[i][j]:
                dtf(new_i, new_j, using)


n = 8
using = [[False] * n for _ in range(n)]
graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    s = input()
    a = []
    for j in range(n):
        if s[j] == "W":
            a.append(0)
        else:
            a.append(1)
    graph.append(a)

cnt = 0
for i in range(n):
    for j in range(n):
        if using[i][j] == False:
            dtf(i, j, using)
            cnt += 1

print(cnt)
