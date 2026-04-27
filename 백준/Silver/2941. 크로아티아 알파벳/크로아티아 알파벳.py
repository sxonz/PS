s = input()
n = len(s)
n -= 2*s.count("dz=")
s = s.replace("dz=","x")
for i in ("c=","c-","d-","lj","nj","s=","z="):
    n -= s.count(i)
print(n)