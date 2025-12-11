a = input()
b = input()
s = ''
for i,j in zip(a,b):
    s += str(max(int(i),int(j)))
print(s)