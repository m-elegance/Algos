N = 100
graph = [[0] * N for _ in range(N)]


n = int(input())
for i in range(n):
    graph[i] = list(map(int, input().split()))

ans = []
for i in range(n):
    cnt = 0
    for j in range(n):
        cnt += graph[i][j]
    ans.append(cnt)

flag = "YES"
for i in range(1, n):
    if ans[i] != ans[i - 1]:
        flag = "NO"

print(flag)
