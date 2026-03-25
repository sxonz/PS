n = int(input())
r = 1
MOD = 45678
for i in range(n):
    r = (r+i*3+4)%MOD
print(r)