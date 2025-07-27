N = 100
graph = [[0] * N for _ in range(N)]

n = int(input())
for i in range(n):
    graph[i] = list(map(int, input().split()))


flag = "NO"

for i in range(n):
    for j in range(i + 1, n):
        if graph[i][j] != graph[j][i]:
            flag = "YES"


for i in range(n):
    if graph[i][i] == 1:
        flag = "NO"

print(flag)
