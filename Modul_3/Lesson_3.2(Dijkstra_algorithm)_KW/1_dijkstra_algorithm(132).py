from collections import *
def dj(s, dist, edges):
    dist[s] = 0
    queue = deque([[dist[s], s]])
    while queue:
        curr_v = queue[0][1]
        curr_dist = queue[0][0]
        for i in range(len(queue)):
            if curr_dist > queue[i][0]:
                curr_dist = queue[i][0]
                queue[0][0], queue[i][0] = queue[i][0], queue[0][0]
        queue.popleft()
        for i in range(len(edges[curr_v])):
            u = edges[curr_v][i][0]
            w = edges[curr_v][i][1]
            if dist[u] > dist[curr_v] + w:
                dist[u] = dist[curr_v] + w
                queue.append([dist[u], u])
        

n, s, f = map(int, input().split())
s -= 1
f -= 1

edges = [[] for i in range(n)]

for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        if a[j] != -1:
            edges[i].append([j, a[j]])

INF = 10 ** 9
dist = [INF] * n
dj(s, dist, edges)
if dist[f] == INF:
    print(-1)
else:
    print(dist[f])



