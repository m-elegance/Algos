import heapq as hq
from math import inf

n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]

for i in range(m):
    u, v, t, c = map(int, input().split())

    edges[v].append([u, t, c])
    edges[u].append([v, t, c])


def dj(edges, dist, mid):
    dist[1] = 0
    heap = []
    hq.heappush(heap, [0, 1])
    while heap:
        begin = hq.heappop(heap)
        v = begin[1]
        cur_t = begin[0]
        if dist[v] < cur_t:
            continue
        # for i in range(len(edges[v])):
        #     u = edges[v][i][0]
        #     t = edges[v][i][1]
        #     c = edges[v][i][2]
        for u, t, c in edges[v]:

            if dist[u] > dist[v] + t and c >= mid:
                dist[u] = dist[v] + t
                hq.heappush(heap, [dist[u], u])
    
    return dist[-1] <= 1440


l = 0
r = 10000000
ans = 0
while l <= r:
    mid = (l + r) // 2
    dist = [10**9 for _ in range(n + 1)]
    if dj(edges, dist, 3000000 + mid * 100):
        l = mid + 1
        ans = max(ans, mid)
    else:
        r = mid - 1
print(ans)


