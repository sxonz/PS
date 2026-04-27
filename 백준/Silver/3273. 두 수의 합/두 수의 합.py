n = int(input())
d = set(list(map(int,input().split())))
x = int(input())
print(sum([1 for i in d if x-i in d])//2)