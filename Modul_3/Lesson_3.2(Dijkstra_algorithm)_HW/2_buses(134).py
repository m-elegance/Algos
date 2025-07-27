import heapq as hq
from math import inf


def dj(s, edges, dist):
    dist[s] = 0
    heap = []
    time = 0
    hq.heappush(heap, [dist[s], s])
    while heap:
        begin = hq.heappop(heap)
        v = begin[1]
        for i in range(len(edges[v])):
            u = edges[v][i][0]
            if dist[v] > edges[v][i][1][0]:
                continue
            
            w = edges[v][i][1][1] - dist[v]
            if dist[u] > dist[v] + w:
                dist[u] = dist[v] + w
                hq.heappush(heap, [dist[u], u])


n = int(input())
s, f = map(int, input().split())
s -= 1
f -= 1

edges = [[] for _ in range(n)]
r = int(input())
for i in range(r):
    u, t1, v, t2 = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append([v, [t1, t2]])

dist = [inf] * n

dj(s, edges, dist)
if dist[f] == inf:
    print(-1)
else:
    print(dist[f])
