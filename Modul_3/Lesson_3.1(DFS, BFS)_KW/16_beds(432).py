from collections import deque

def is_border(i, j):
    return 0 <= i < n and 0 <= j < m

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

grid = [[None] * m for _ in range(n)]


cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '#' and grid[i][j] is None:
            queue = deque([[i, j]])
            grid[i][j] = 1
            while queue:
                curr_i, curr_j = queue.popleft()
                for k in range(4):
                    new_i, new_j = curr_i + dx[k], curr_j + dy[k]
                    if not is_border(new_i, new_j):
                        continue
                    else:
                        if grid[new_i][new_j] is None and graph[new_i][new_j] == '#':
                            grid[new_i][new_j] = 1
                            queue.append([new_i, new_j])
            cnt += 1

print(cnt)
                        








