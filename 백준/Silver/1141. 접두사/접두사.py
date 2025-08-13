n = int(input())
arr = [input() for _ in range(n)]
arr.sort(key=len)
ans = n
for i in range(n):
    for j in range(i+1, n):
        if arr[i] == arr[j][:len(arr[i])]:
            ans -= 1
            break
print(ans)