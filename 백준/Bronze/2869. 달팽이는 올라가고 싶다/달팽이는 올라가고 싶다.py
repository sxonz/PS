a,b,v = map(int,input().split())
print((v-a)//(a-b)+1+int(bool((v-a)%(a-b))))