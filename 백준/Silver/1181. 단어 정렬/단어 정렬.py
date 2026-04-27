n = int(input())
d = set()
for i in range(n):
    d.add(input())
for i in sorted(list(d),key=lambda x:(len(x),x)):
    print(i)