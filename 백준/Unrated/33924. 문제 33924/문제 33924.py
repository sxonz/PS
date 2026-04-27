a = [4,5,6,7,0,1,2,3]
b = [3,2,1,0,7,6,5,4]
c = [7,6,5,4,3,2,1,0]
d = [1,3,0,5,2,7,4,6]
n,m = map(int,input().split())
r = (n-1)*2+m-1
input()
s = input()
for i in s:
    if i == "A":
        r = a[r]
    if i == "B":
        r = b[r]
    if i == "C":
        r = c[r]
    if i == "D":
        r = d[r]
print(r//2+1,r%2+1)