n = int(input())
s = input()
x=y=0
for i in range(n-1):
    if ord(s[i]) < ord(s[i+1]):
        y += 1
    else:
        x += 1
if abs(x-y) <= 1:
    print(n)
    print(s)
    exit()
if x > y:
    if 90-ord(s[-1])-sum([1 for i in range(ord(s[-1])+1,91) if chr(i) in s]) < x-y-1:
        x += 2
        for i in range(65,91):
            if chr(i) not in s:
                s += chr(i)
                n += 1
                y += 1
                if x-y <= 1:
                    break
        print(n)
        print(s)
    else:
        for i in range(ord(s[-1])+1,91):
            if chr(i) not in s:
                s += chr(i)
                n += 1
                y += 1
                if x-y <= 1:
                    break
        print(n)
        print(s)
else:
    if ord(s[-1]) - 65 - sum([1 for i in range(ord(s[-1])-1,64,-1) if chr(i) in s]) < y-x-1:
        y += 2
        for i in range(90,66,-1):
            if chr(i) not in s:
                s += chr(i)
                x += 1
                n += 1
                if y-x <= 1:
                    break
        print(n)
        print(s)
    else:
        for i in range(ord(s[-1])-1,64,-1):
            if chr(i) not in s:
                s += chr(i)
                x += 1
                n += 1
                if y-x <= 1:
                    break
        print(n)
        print(s)