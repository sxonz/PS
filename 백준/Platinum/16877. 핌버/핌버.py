n = int(input())
d = list(map(int,input().split()))
p = 3000000

fib = set([1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309])
g = [0,1,2]
for i in range(3,p+1):
    mex = set()
    for j in fib:
        if i >= j:
            mex.add(g[i-j])
        else:
            break
    for k in range(19):
        if k not in mex:
            g.append(k)
            break
res = 0
for i in d:
    res ^= g[i]
res = 'koosaga' if res else 'cubelover'
print(res)