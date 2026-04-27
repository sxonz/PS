n = int(input())
cost,tcost = map(int,input().split())
cal = int(input())
d = [int(input()) for i in range(n)]
d.sort(reverse=True)
for i in range(n):
    if (d[i]+cal) / (cost+tcost) > cal / cost:
        cal += d[i]
        cost += tcost
print(cal//cost)