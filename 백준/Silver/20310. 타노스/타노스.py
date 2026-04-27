d = list(input())
n = len(d)
a = d.count("0")//2
b = n//2-a

idx = 0
while b:
    if d[idx] == "1":
        d.pop(idx)
        b -= 1
    else:
        idx += 1

n = len(d)
idx = n-1
while a:
    if d[idx] == "0":
        d.pop(idx)
        a -= 1
    idx -= 1

print(''.join(d))