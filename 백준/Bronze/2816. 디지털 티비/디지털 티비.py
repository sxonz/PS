n = int(input())
d = [input() for i in range(n)]
a,b = d.index("KBS1"),d.index("KBS2")
res = "1"*a+"4"*a
if a>b:
    b += 1
res += "1"*b+"4"*(b-1)
print(res)