n = int(input())
res =''
if n == 0:
    print(0)
    exit()
while n:
    res += str(-(n%-2))
    n = n//-2 - n%-2

print(res[::-1])