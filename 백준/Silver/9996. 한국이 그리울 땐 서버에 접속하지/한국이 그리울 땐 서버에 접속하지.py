import re
n=int(input())
s=input().replace("*",".*")
regex=re.compile(s)
for x in range(n):
    d=input()
    reg=regex.search(d)
    if not reg:
        print("NE")
    else:
        print('NDEA'[reg.group()==d::2])