from collections import deque
from math import inf

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dist = [[inf] * m for _ in range(n)]

queue = deque([])

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


def is_board(i, j):
    return 0 <= i < n and 0 <= j < m


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])
            dist[i][j] = 0


while queue:
    i_1, j_1 = queue.popleft()
    for k in range(4):
        i_2 = i_1 + di[k]
        j_2 = j_1 + dj[k]
        if is_board(i_2, j_2):
            if dist[i_2][j_2] > dist[i_1][j_1] + 1:
                dist[i_2][j_2] = dist[i_1][j_1] + 1
                queue.append([i_2, j_2])


for i in range(n):
    for j in range(m):
        print(dist[i][j], end=" ")
    print()
