n = int(input())
d = sorted(map(int,input().split()))

dif = []
for i in range(len(d)-1):
    dif.append(d[i+1]-d[i])

res = dif[0] + dif[1]
for i in range(3,len(dif),2):
    res += dif[i]

tmp = res
for i in range(1,len(dif)-1,2):
    tmp = tmp - dif[i] + dif[i+1]
    res = min(res,tmp)
    
print(res)