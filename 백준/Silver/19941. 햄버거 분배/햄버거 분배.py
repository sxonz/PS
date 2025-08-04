n,k = map(int,input().split())
d = input()
visit = [0]*n
cnt = 0
for i in range(n):
    if d[i] == "P":
        for j in range(max(0,i-k), min(i+k+1,n)):
            if d[j] == "H":
                if not visit[j]:
                    visit[j] = True
                    cnt += 1
                    break
print(cnt)