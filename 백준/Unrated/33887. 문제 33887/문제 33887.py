pal = [set() for i in range(31)]
pal[0] = set([""])
pal[1] = set(["0","1"])
def palindrome(cur):
    if cur >= 29:
        return
    for x in pal[cur]:
        pal[cur+2].add("0"+x+"0")
        pal[cur+2].add("1"+x+"1")
    palindrome(cur+2)
palindrome(0)
palindrome(1)
pals = set()
for i in pal:
    for j in i:
        if j and j[0] != '0':
            pals.add(int(j,2))
pals = list(pals)
pals.sort()

from bisect import *
for t in range(int(input())):
    n = int(input())
    idx = bisect_left(pals,n)
    if pals[idx] == n:
        print(0)
    else:
        print(min(pals[idx]-n,abs(pals[idx-1]-n)))