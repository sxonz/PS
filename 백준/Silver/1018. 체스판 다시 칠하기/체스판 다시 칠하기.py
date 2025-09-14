n,m = map(int,input().split())
d = [input() for i in range(n)]
Wf = (("WB"*4)+("BW"*4))*4
M = 65
for i in range(n-7):
    for j in range(m-7):
        M = min(M,t:=sum(k==l for k,l in zip(Wf,''.join([s[j:j+8] for s in d[i:i+8]]))),64-t)
print(M)
