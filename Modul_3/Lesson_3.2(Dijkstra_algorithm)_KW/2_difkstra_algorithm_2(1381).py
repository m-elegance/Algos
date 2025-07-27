import heapq as hq


def dj(s, dist, edges, road):
    dist[s] = 0
    heap = []
    hq.heappush(heap, [dist[s], s])  #O(1) добавление элемента в heap
    while heap:
        begin = hq.heappop(heap)     #O(log n) 
        v = begin[1]
        for i in range(len(edges[v])):
            w = edges[v][i][0]
            u = edges[v][i][1]
            if dist[u] > dist[v] + w:
                dist[u] = dist[v] + w
                road[u] = v
                hq.heappush(heap, [dist[u], u])


n, s, f = map(int, input().split())
s -= 1
f -= 1
INF = 10**9
edges = [[] for _ in range(n)]
dist = [INF] * n
road = [-1] * n

for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        if a[j] != -1:
            edges[i].append([a[j], j])

dj(s, dist, edges, road)

ans = []
vertex = f
while vertex != -1:
    ans.append(vertex + 1)
    vertex = road[vertex]

ans = ans[::-1]
if dist[f] == INF:
    print(-1)
else:
    print(*ans)
