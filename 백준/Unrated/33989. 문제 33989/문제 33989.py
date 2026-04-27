n = int(input())
d = input()
a = 0
b = d.count("B")
m = b
for i in range(n):
    if d[i] == "B":
        b -= 1
    else:
        a += 1
    m = min(m,a+b)
print(m)
