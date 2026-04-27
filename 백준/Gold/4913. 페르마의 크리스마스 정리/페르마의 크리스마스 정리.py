import sys
input = sys.stdin.readline

MAX = 1000001
prime = [1]*MAX
prime[0] = prime[1] = 0
for i in range(2,MAX-1):
    if prime[i]:
        k = 2
        while i*k<MAX:
            prime[i*k] = 0
            k += 1
square = [0]*MAX
for i in range(1,1000):
    for j in range(i,1000):
        if i*i+j*j < MAX:
            square[i*i+j*j] = 1

psum = [(0,0) for i in range(MAX)]
for i in range(1,MAX):
    psum[i] = (psum[i-1][0]+prime[i],psum[i-1][1]+prime[i]*square[i])
while True:
    a,b = map(int,input().split())
    if (a,b) == (-1,-1):
        break
    s = psum[max(a-1,0)]
    e = psum[max(b,0)]
    print(a,b,e[0]-s[0],e[1]-s[1])