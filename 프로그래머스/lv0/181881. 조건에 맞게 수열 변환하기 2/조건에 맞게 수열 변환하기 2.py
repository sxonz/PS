def solution(arr):
    before = arr[::]
    x = 0
    while True:
        x += 1
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] //= 2
            elif arr[i] < 50 and arr[i] % 2 != 0:
                arr[i] = arr[i] * 2 + 1
        if before == arr:
            return x-1
        before = arr[::]
            