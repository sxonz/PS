import sys
sys.setrecursionlimit(20000)
def gcd(a,b):
	return b if not a%b else gcd(b,a%b)

input()
a = list(map(int,input().split()))
input()
b = list(map(int,input().split()))
n = 1
m = 1
for i in a:
	n *= i
for i in b:
	m *= i

print(str(gcd(n,m))[-9:])