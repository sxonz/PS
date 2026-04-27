from math import *
n,k = map(int,input().split())
MOD = int(1e9)+7
print(comb(n,k)*(1<<k-1)%MOD)