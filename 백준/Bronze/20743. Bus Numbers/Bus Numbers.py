n=int(input())
d,r,s={},{},range(1,74)
for i in s:
    for j in s[i:]:
        t=i**3+j**3
        if t in d:r[-t]=1
        d[t]=1
d=[-i for i in sorted(r) if -i<=n]+['none']
print(d[0])
