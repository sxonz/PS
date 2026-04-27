m,a = map(int,input().split())
try:
    res = abs(pow(a, -1, m))
except:
    res = -1
print(m-a,res)