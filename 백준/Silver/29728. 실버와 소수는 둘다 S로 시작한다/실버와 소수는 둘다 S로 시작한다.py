def prime(n):
    array = [True for i in range(n + 1)]
    ans = set()
    ans.add(2)
    for i in range(2,n+1):
	    if array[i] == True:
              ans.add(i)
              j = 2
              while i * j <= n:
                  array[i*j] = False
                  j += 1
    return ans
n = int(input())
B,S = 0,0
before = ''
p = prime(n+1)
for i in range(1,n+1):
    if i not in p:
        before = 'b'
        B += 1
    else:
        if before == 'b':
            B -= 1
            S += 1
        S += 1
        before = 's'
print(B,S)