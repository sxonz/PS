l,c = map(int,input().split())
d = input().split()
d.sort()
vowel = ["a","e","i","o","u"]

def code(depth,idx,lst):
    if idx+l-depth >= c:
        return
    if depth == l:
        v = 0
        nv = 0
        for i in lst:
            if i in vowel:
                v += 1
            else:
                nv += 1
        if v >= 1 and nv >= 2:
            print("".join(lst))
            return
    for i in range(idx+1,c):
        code(depth+1,i,lst+[d[i]])
for i in range(c):
    code(1,i,[d[i]])
        
