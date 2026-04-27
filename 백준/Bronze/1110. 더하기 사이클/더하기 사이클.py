n = int(input())
d = []
i=0
while n not in d:
    i+=1
    d.append(n)
    tmp = n //10 + n % 10
    n = (n % 10)*10 + tmp % 10
print(i)