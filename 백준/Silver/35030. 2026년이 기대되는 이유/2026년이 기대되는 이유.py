import sys
input = sys.stdin.readline

prime = set()
MAX = 100001
p = [0]*MAX
for i in range(2,MAX):
    if not p[i]:
        prime.add(i)
        k = 2
        while i*k<MAX:
            p[i*k] = 1
            k += 1

num = set()
for i in range(1,MAX):
    if i+1 not in prime:
        continue
    i = str(i)
    for k in range(1,len(i)):
        if (int(i[:k])*int(i[k:]))+1 not in prime:
            break
    else:
        num.add(int(i))

psum = [0]*MAX
for i in range(1,MAX):
    psum[i] = psum[i-1]
    if i in num:
        psum[i] += 1

for t in range(int(input())):
    print(psum[int(input())])