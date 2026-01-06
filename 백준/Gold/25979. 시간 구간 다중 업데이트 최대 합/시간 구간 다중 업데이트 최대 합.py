def parse(s):
    tmp = list(map(int,s.split(":")))
    return tmp[0]*3600+tmp[1]*60+tmp[2]

MAX = 86401
n = int(input())
d = [0]*MAX
for i in range(n-1):
    _,a,b = input().split()
    a,b = parse(a),parse(b)
    d[a] += 1
    d[b] -= 1

psum = [d[0]]
for i in d[1:]:
    psum.append(psum[-1]+i)

_,x = input().split()
x = parse(x)
cur = sum(psum[:x])
ans = cur
for i in range(x,MAX):
    cur -= psum[i-x]
    cur += psum[i]
    ans = max(cur,ans)

print(ans)