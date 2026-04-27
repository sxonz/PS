log = [10**(i-2) for i in range(12)]
log[0] = log[1] = 0
inc = [log[i+1]*i for i in range(-1,11)]
n = input()
res = [0]*10
for i,j in zip(range(len(n),0,-1),range(len(n))):
    if n[j] == '0':
        res[0] -= log[i+1]

    for k in range(0,10):
        res[k] += int(n[j])*inc[i]
    for k in range(1,int(n[j])):
        res[k] += log[i+1]
    if n[j+1:]:
        res[int(n[j])] += int(n[j+1:])+1
    else:
        res[int(n[j])] += 1
print(*res)