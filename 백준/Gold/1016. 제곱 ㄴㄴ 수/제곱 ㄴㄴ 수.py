s,e = map(int,input().split())

check = [False]*(e-s+1)
for i in range(2,int(e**0.5)+1):
    p = i*i
    s_idx = int(s/p)
    if s % p != 0:
        s_idx += 1
    for j in range(s_idx,int(e/p)+1):
        check[int(j*p)-s] = True
cnt = 0
for i in range(e-s+1):
    if not check[i]:
        cnt += 1

print(cnt)