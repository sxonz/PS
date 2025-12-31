from itertools import permutations

MAX = 10000000
prime = [1]*MAX
prime[0] = prime[1] = 0
for i in range(2,MAX//2+1):
    if prime[i]:
        k = 2
        while i*k < MAX:
            prime[i*k] = 0
            k += 1

for c in range(int(input())):
    s = input()
    tmp = set()
    res = 0
    for k in range(1,len(s)+1):
        for i in permutations(s,k):
            i = int(''.join(i))
            if i in tmp:
                continue
            tmp.add(i)
            res += prime[i]
    print(res)