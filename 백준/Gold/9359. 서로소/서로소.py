from itertools import combinations
import sys
input = sys.stdin.readline

def phi(n):
    result = [] 
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            result.append(i)
            while n % i == 0:
                n //= i
    if n > 1:
        result.append(n)
    return result

testcase = int(input())
for case in range(1, testcase+1):
    A, B, N = map(int, input().split())
    x, resa, resb = phi(N), A-1, B
    for i in range(1, len(x)+1): 
        for comb in combinations(x,i):
            m = 1
            for j in comb:
                m *= j
            if i%2 != 0:
                resa -= (A-1)//m
                resb -= B//m
            else:
                resa += (A-1)//m
                resb += B//m
    print('Case #{0}: {1}'.format(case,resb-resa))