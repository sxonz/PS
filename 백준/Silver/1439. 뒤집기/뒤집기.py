n=input()
ans = int(1e12)
for k in [0,1]:
    tmp = 0
    for i in n.split(str(k)):
        if str(k^1) in i:
            tmp += 1
    ans = min(ans,tmp)
print(ans)