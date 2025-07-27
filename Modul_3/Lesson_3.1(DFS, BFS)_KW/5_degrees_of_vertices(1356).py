N = 100
graph = [[0] * N for _ in range(N)]

n = int(input())
for i in range(n):
    graph[i] = list(map(int, input().split()))


ans = [0] * n
for i in range(n):
    for j in range(n):
        ans[i] += graph[i][j]

print(*ans)





