t = input().split("|")
s = [i[0] for i in t]
c = s.count("C") + s.count("G") + s.count("F")
a = s.count("A") + s.count("D") + s.count("E")
flag = 0
if a>c:
    flag = 1
if a == c and t[-1][-1] in "ADE":
    flag = 1
print("CA--mmaijnoorr"[flag::2])