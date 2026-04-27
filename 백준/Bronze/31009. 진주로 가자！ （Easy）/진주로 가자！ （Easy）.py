n = int(input())
d = []
for I in range(n):
    city,money = input().split()
    money = int(money)
    if city == 'jinju':
        j = money
    d.append(money)
print(j)
print(len([i for i in d if i>j]))