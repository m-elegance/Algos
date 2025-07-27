from collections import deque

n = int(input())
graph = []
dist = [None] * n

for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)

edges = [[] for _ in range(n)]

for i in range(n):
    for j in range(i + 1):
        if graph[i][j] == 1:
            edges[i].append(j)
            edges[j].append(i)


start, finish = map(int, input().split())
start -= 1
finish -= 1

dist[start] = 0
queue = deque([start])
while queue:
    cur_v = queue.popleft()
    for i in edges[cur_v]:
        if dist[i] is None:
            dist[i] = dist[cur_v] + 1
            queue.append(i)

if dist[finish] is None:
    print(-1)
else:
    print(dist[finish])
