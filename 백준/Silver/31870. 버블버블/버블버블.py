n = int(input())
d = list(map(int, input().split()))
tmp = d[::-1]
answer = 0
def merge_sort(start, end):
    global answer, d
    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid+1, end)
        temp = []
        x, y = start, mid+1
        while x <= mid and y <= end:
            if d[x] <= d[y]:
                temp.append(d[x])
                x += 1
            else:
                temp.append(d[y])
                y += 1
                answer += (mid-x)+1
        if x <= mid:
            temp = temp + d[x:mid+1]
        if y <= end:
            temp = temp + d[y:end+1]
        for i in range(len(temp)):
            d[start+i] = temp[i]
        
    
merge_sort(0, n-1)
m = answer

d = tmp[::]
answer = 0

merge_sort(0,n-1)
print(min(answer+1,m))