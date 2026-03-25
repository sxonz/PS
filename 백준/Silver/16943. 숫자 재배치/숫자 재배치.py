a,b = input().split()
b = int(b)
cnt = [0]*10
ans = []
for i in a:
    cnt[int(i)] += 1
n = len(a)
def back(x,cur):
    if cur == n and int(x) < b:
        ans.append(x)
    for i in range(10):
        if cnt[i]:
            if i == 0 and cur == 0:
                continue
            cnt[i] -= 1
            back(x+str(i),cur+1)
            cnt[i] += 1
back('',0)
if ans:
    print(ans[-1])
else:
    print(-1)