# стресс тест

from random import randint


def best_solution(arr, querry):
    n = len(arr)
    prefix_sum = [0] * n
    prefix_sum[0] = arr[0]

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]

    ans = []

    for i in range(len(querry)):
        l, r = querry[i]
        sum_l_r = prefix_sum[r] 
        if l - 1 >= 0:
            sum_l_r -= prefix_sum[l - 1]
        ans.append(sum_l_r)

    return ans



def bad_solution(arr, querry):
    #O(m * n)
    ans = []

    for i in range(len(querry)):
        l, r = querry[i]
        sum_l_r = 0
        for j in range(l, r + 1):
            sum_l_r += arr[j]
        ans.append(sum_l_r)
    return ans

def check(arr, querry):
    if best_solution(arr, querry) != bad_solution(arr, querry):
        print('arr = ', arr)
        print('querry = ', querry)
        print('best_solution = ', best_solution(arr, querry))
        print('bad_solution = ', bad_solution(arr, querry))

        raise Exception ("wrong")

    #print('OK')

def main():
    n = 4
    m = 5
    arr = []
    for i in range(n):
        arr.append(randint(-5, 5))
    
    querry = []
    for i in range(m):
        l = randint(0, n - 1)
        r = randint(l, n - 1)   #l <= r
        querry.append([l, r])

    check(arr, querry)




if __name__ == "__main__":
    for i in range(100):
        main()
    print('OK')

