s = input()

d = dict()
keys = sorted(list(set(s)))
odd = []
for key in keys:
    cnt = s.count(key)
    d[key] = cnt
    if cnt % 2:
        odd.append(key)

if len(odd) > 1:
    print("I'm Sorry Hansoo")

else:
    result = ''

    for key in keys:
        result += key * (d[key] // 2)
    
    tmp = result[::-1]
    if odd:
        result += odd[0]
    result +=  tmp

    print(result)