N = 100
graph = [[0] * N for _ in range(N)]

def read():
    global n, m
    n, m = map(int, input().split())
    for i in range(m):
        v, u = map(int, input().split())
        v -= 1
        u -= 1
        graph[v][u] = graph[u][v] = 1

def sol():
    for i in range(n):
        for j in range(i + 1, n):
            
            if graph[i][j] == 0:
                print("NO")
                return
    print("YES")

if __name__ == "__main__":
    read()
    sol()

# for i in range(m):
#     temp = []
#     x, y = map(int, input().split())
#     if x > y:
#         x, y = y, x
#     temp.append(x)
#     temp.append(y)
#     if temp not in edges:
#         edges.append(temp)


# if len(edges) == n * (n - 1) // 2:
#     print("YES")
# else:
#     print("NO")
