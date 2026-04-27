a,b = divmod((int(input())-1)*8 + sum(list(map(int,input().split()))),24)
print(a,b)