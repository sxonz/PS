def solution(n):
    sum = 0
    sum2 = 1
    f = []
    for i in range(n):
        f.append(sum2)
        temp = sum
        sum = sum2
        sum2 += temp
    return f[n-1] % 1234567