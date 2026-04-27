t = int(input())
n = [int(input()) for _ in range(t)]
d = [1,1,1,2,2,3]
for i in range(6,max(n)+1):
    d.append(d[-1]+d[-5])
for i in n:
    print(d[i-1])