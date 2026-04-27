n=int(input())
a=list(map(int,input().split()))
d = [a[0]]

def binarySearch(e):
    start = 0
    end = len(d) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if d[mid] == e:
            return mid
        elif d[mid] < e:
            start = mid + 1
        else:
            end = mid - 1
            
    return start


for i in range(n):
    if a[i] > d[-1]:
        d.append(a[i])
    else:
        idx = binarySearch(a[i])
        d[idx] = a[i]

print(len(d))