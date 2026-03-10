MAX = 1000001
p = []
prime = [1]*MAX
for i in range(2,MAX):
    if prime[i]:
        p.append(i)
        if i < int(MAX**0.5+1):
            k = 2
            while i*k<MAX:
                prime[i*k] = 0
                k += 1

s = set(p)
for t in range(int(input())):
    n = int(input())
    ans = 0
    for i in p:
        if n-i in s:
            ans += 1
            if i == n-i:
                ans += 1
    print(ans//2)