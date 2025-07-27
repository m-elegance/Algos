from random import *


def solution(arr):
    n = len(arr)
    prefix_sum = [0] * n
    suffix_sum = [0] * n

    prefix_sum[0] = arr[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]

    suffix_sum[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + arr[i]

    ans = []

    for i in range(n):
        left_sum = right_sum = 0
        if i - 1 >= 0:
            left_sum = prefix_sum[i - 1]
        if i + 1 < n:
            right_sum = suffix_sum[i + 1]
        ans.append(abs(left_sum - right_sum))

    print(arr)
    print(prefix_sum, suffix_sum)
    print(ans)





def main():
    n = 5
    arr = [randint(0, 10) for i in range(n)]
    solution(arr)

    


if __name__ == '__main__':
    main()
