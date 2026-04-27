n = int(input())
d = input().replace(":",".").replace("|",".").replace("#",".").split(".")
print(sum([int(i) for i in d]))