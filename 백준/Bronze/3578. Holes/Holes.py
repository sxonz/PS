n = int(input())
if not n:
    print(1)
    exit()
if n == 1:
    print(0)
    exit()
s = "4"*(n%2)+"8"*(n//2)
print(s)