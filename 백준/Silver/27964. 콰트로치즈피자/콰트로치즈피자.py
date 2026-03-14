n = int(input())
d = set()
for i in input().split():
    if i[::-1][:6] == "eseehC":
        d.add(i)
if len(d) >= 4:
    print("yummy")
else:
    print("sad")