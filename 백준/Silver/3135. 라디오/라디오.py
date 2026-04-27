a,b = map(int,input().split())
n = int(input())
d =  [int(input()) for i in range(n)]

print(min(abs(b-a),min([abs(b-i)+1 for i in d])))