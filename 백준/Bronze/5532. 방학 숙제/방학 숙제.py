l,a,b,c,d = int(input()),int(input()),int(input()),int(input()),int(input())
print(l-max(a//c+bool(a%c),b//d+bool(b%d)))