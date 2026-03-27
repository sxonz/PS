import sys
def p(s):
    print(s)
    sys.stdout.flush()
n = int(input())
a = []
p("? 1 * 2")
a.append(0)
if input() == "+":
    a.append(0)
    bef = 0
else:
    a.append(1)
    bef = 1

for i in range(2,n):
    p(f"? {i} * {i+1}")
    if input() == "+":
        a.append(bef)
    else:
        bef ^= 1
        a.append(bef)
if 0 in a[1:]:
    idx = a[1:].index(0)+2
    p(f"? 1 + {idx}")
    if input() == "+":
        a = ["+-"[i] for i in a]
    else:
        a = ["-+"[i] for i in a]
else:
    p(f"? 2 + 3")
    if input() == "+":
        a = ["-+"[i] for i in a]
    else:
        a = ["+-"[i] for i in a]
p(f"! {' '.join(a)}")
exit()