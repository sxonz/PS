def gcd(a, b):
    return b if not a%b else gcd(b,a%b)

ans = [0, 3]

for i in range(2, 1001):
    cur = sum(1 for j in range(1,i) if gcd(i,j) == 1)
    ans.append(ans[-1] + cur * 2)

for _ in range(int(input())):
    print(ans[int(input())])