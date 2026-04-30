def solution(arr):
    for i,j in enumerate(arr):
        if j >= 50 and j % 2 == 0:
            arr[i] //= 2
        elif j < 50 and j % 2 != 0:
            arr[i] *= 2
    return arr
        
    