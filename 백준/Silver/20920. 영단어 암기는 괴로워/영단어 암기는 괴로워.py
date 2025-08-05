n,m = map(int,input().split())
d = [tmp for i in range(n) if len(tmp:=input()) >= m]
cnt = dict()
for i in d:
    if i not in cnt:
        cnt[i] = 0
    cnt[i] += 1
r = list(set(d))
r.sort(key=lambda x:(-cnt[x],-len(x),x))
print(*r,sep='\n')