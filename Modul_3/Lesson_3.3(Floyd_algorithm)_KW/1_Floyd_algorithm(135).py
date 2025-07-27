n = int(input())

dist = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])    

for i in range(n):
    for j in range(n):
        print(dist[i][j], end = ' ') 
    print() 

  








