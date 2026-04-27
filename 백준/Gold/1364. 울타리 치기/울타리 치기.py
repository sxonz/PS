n = int(input())
tmp = 1
r = [1,1,1,1,2,1]
for i in range(n-1):
    if i%6==0 and i:
        r = [j+1 for j in r]
    tmp += r[i%6]
print(tmp)