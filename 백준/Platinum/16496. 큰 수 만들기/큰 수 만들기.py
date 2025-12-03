n=int(input())
def r(y):
 if y==0:return 0
 while y>int(1e10):y//=10
 return -y
res = ''.join(map(str,sorted(map(int,input().split()),key=lambda x:r(sum(x*10**(i*len(str(x))) for i in range(15))))))
if res == len(res)*'0':
 print(0)
else:
 print(res)
