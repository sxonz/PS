d = [0,1,3]
for i in range(2,30):
    d.append(d[-1]+2**i)
n = int(input())
idx = 0
for i in range(31):
    if d[i] <= n:
        idx = i
ans = ''
while idx:
    inc = (d[idx]+1)//2
    if n >= d[idx]+inc:
        n -= inc
        ans += '7'
    else:
        ans += '4'
    n -= d[idx]-d[idx-1]
    idx -= 1
print(ans)