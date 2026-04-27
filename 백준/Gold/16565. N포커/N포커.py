from itertools import combinations
import math

n = int(input())
res = 0
for i in range(1,n//4+1):
    t,t2 = 52-(4*i),n-(4*i)
    if i %2 != 0:
        res += math.comb(t,t2)*math.comb(13,i)
    else:
        res -= math.comb(t,t2)*math.comb(13,i)


print(res%10007)
