import heapq as hq
from math import inf

def dj(s, edges, dist):
    dist[s] = 0
    heap = []
    hq.heappush(heap, [dist[s], s])
    while heap:
        begin = hq.heappop(heap)
        v = begin[1]
        for i in range(len(edges[v])):
            u = edges[v][i][0]
            w = edges[v][i][1]
            if dist[u] > dist[v] + w:
                dist[u] = dist[v] + w
                hq.heappush(heap, [dist[u], u])


n = int(input())
w = list(map(int, input().split()))
m = int(input())
edges = [[] for _ in range(n)]
dist = [inf] * n

for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append([v, w[u]])
    edges[v].append([u, w[v]])

dj(0, edges, dist)
if dist[n - 1] == inf:
    print(-1)
else:
    print(dist[n - 1])




