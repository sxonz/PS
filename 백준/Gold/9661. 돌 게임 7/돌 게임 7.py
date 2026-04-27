d = ['CY','SK','CY','SK','SK']
n = int(input())
if n < 4:
    print(['0','SK','CY','SK'][n])
else:    
    n %= 5
    print(d[n])