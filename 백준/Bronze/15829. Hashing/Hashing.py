n = int(input())
s = input()
r = sum([(ord(s[i])-96)*int(pow(31,i,1234567891)) for i in range(n)])%1234567891
print(r)
