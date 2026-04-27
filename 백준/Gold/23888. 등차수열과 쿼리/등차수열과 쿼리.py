def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)
a, d = map(int, input().split())
res = a if d == 0 else gcd(a, d)
for q in range(int(input())):
    t, l, r = map(int, input().split())
    if t == 1:
        n = r - l + 1
        start_value = a + (l - 1) * d
        ans = n * (2 * start_value + (n - 1) * d) // 2
        print(ans)
    else:
        if l == r:
            print(a + (l - 1) * d)
        else:
            print(res)