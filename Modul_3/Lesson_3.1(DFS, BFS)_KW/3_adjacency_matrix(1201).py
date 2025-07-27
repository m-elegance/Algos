N = 100
graph = [[0] * N for i in range(N)]
n = int(input())

for i in range(n):
    graph[i] = list(map(int,input().split()))


cnt = 0
my_dict = {}

edges = [[] for i in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            edges[i].append(j)
            cnt += 1
       
print(n, cnt)
for i in range(len(edges)):
    if not edges[i] == False:
        for j in range(len(edges[i])):
            print(i + 1, edges[i][j] + 1)







