a,b = map(int,input().split())
c,d = map(int,input().split())
e,f = map(int,input().split())
hp = int(input())
i = 0
while hp > 0:
    if i % a == 0:
        hp -= b
    if i % c == 0:
        hp -= d
    if i % e == 0:
        hp -= f
    i += 1
i = i if not i else i-1
print(i)