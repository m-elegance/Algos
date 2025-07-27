from collections import deque

n = int(input())
dist = [[None] * (n + 1) for _ in range(n + 1)]

def is_board(x, y):
    return 1 <= x <= n and 1 <= y <= n

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

x_start, y_start = map(int, input().split())
x_end, y_end = map(int, input().split())


dist[x_start][y_start] = 0

queue = deque([[x_start, y_start]])
while queue:
    curr_x, curr_y = queue.popleft()
    for i in range(8):
        new_curr_x, new_curr_y = curr_x + dx[i] , curr_y + dy[i] 
        if not is_board(new_curr_x, new_curr_y):
            continue
        else:
            if dist[new_curr_x][new_curr_y] is None:
                dist[new_curr_x][new_curr_y] = dist[curr_x][curr_y] + 1
                queue.append([new_curr_x, new_curr_y])

print(dist[x_end][y_end])

