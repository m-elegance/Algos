from collections import deque


def is_board(i, j):
    return 0 <= i < n and 0 <= j < m


n, m = map(int, input().split())
graph = [[] for i in range(n)]
for i in range(n):
    s = input()
    for j in range(m):
        if s[j] == "*":
            graph[i].append(1)
        else:
            graph[i].append(0)


di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

used = [[False] * m for _ in range(n)]


def bfs(i, j, used, graph):
    stack = [[i, j]]
    while len(stack) > 0:
        i_1, j_1 = stack[0]
        stack.pop(0)
        for k in range(4):
            i_2 = i_1 + di[k]
            j_2 = j_1 + dj[k]
            if is_board(i_2, j_2) and used[i_2][j_2] == False and graph[i_2][j_2] == 1:
                used[i_2][j_2] = True
                stack.append([i_2, j_2])


cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and used[i][j] == False:
            bfs(i, j, used, graph)
            cnt += 1

print(cnt)
