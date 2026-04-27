n,m = map(int,input().split())
a = set(input() for i in range(n)) & set(input() for j in range(m))
print(len(a))
print(*sorted(a),sep='\n')