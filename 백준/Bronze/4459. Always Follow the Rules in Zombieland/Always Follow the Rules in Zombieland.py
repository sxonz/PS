n = int(input())
d = [input() for i in range(n)]

q = int(input())
for i in range(1,q+1):
    r = int(input())
    if r<=0 or r>n:
        tmp = "No such rule"
    else:
        tmp = d[r-1]
    print(f"Rule {r}: {tmp}")