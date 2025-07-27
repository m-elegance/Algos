#in leetcode:  
# 1480, 2574, 1732, 2848, 1991, 1893, 1829, 1442, 1314


# 2848 <- использовался подход с подотрезками и +1, -1 на flag_arr


# представлен код для задачи 1314 (here неправильный, на литкоде правильный)
# представлен алгоритм нахождения префиксной суммы для матрицы
mat = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
n = len(mat)
m = len(mat[0])

prefix_sum = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    for j in range(m):
        #i, j
        prefix_sum[i][j] = mat[i][j]
        if i - 1 >= 0:
            prefix_sum[i][j] += prefix_sum[i - 1][j]
        if j - 1 >= 0:
            prefix_sum[i][j] += prefix_sum[i][j - 1]
        if i - 1 >= 0 and j - 1 >= 0:
            prefix_sum[i][j] -= prefix_sum[i - 1][j - 1]

ans = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    for j in range(m):
        ans[i][j] += prefix_sum[min(n - 1, i + k)][min(m - 1, j + k)]
        ans[i][j] += prefix_sum[max(0, i - k - 1)][max(0, j - k - 1)]
        ans[i][j] -= prefix_sum[min(i + k, n - 1)][max(0, j - k - 1)]
        ans[i][j] -= prefix_sum[max(i - k - 1, 0)][min(m - 1, j + 1)]

print(ans)