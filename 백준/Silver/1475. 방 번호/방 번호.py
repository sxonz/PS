n = input()
d = [0 for _ in range(10)]
for i in n:
    i = int(i)
    d[i] += 1

tmp = (d.pop()+d.pop(6))
if tmp %2 != 0:
    tmp += 1
tmp //= 2
print(max(max(d),tmp))