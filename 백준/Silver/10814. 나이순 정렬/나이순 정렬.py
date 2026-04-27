import sys
input = sys.stdin.readline

n = int(input())
d = []
for i in range(n):
    a,b = input().split()
    d.append((int(a),b,i))
for i in sorted(d,key = lambda x:(x[0],x[2])):
    print(i[0],i[1])