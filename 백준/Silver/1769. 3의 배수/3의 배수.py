s = input()
c = 0
while len(s) > 1:
    c += 1
    s = str(sum([int(i) for i in s]))
print(c)
print("YNEOS"[bool(int(s)%3)::2])